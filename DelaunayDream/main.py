import cv2
import sys
import time
import os
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from DelaunayDream.gui.gui import Ui_MainWindow
from DelaunayDream.gui.stylesheet import StyleSheet
from DelaunayDream.triangulation.triangulation import Triangulation
from DelaunayDream.videopipe.video import Video
from DelaunayDream.videopipe.process import Process
from DelaunayDream.file_dialogue import FileDialogue
from DelaunayDream.warning_dialogue import WarningDialogue


def reconnect(signal, new_handler=None):
    """
    helper function for reconnecting pyqt slots
    :param signal: qt signal
    :param new_handler: new function to be connected to it
    :return:
    """
    try:
        while True:
            signal.disconnect()
    except TypeError:
        pass
    if new_handler is not None:
        signal.connect(new_handler)


class GeneralWorker(QThread):
    """
    general use QtThread worker
    """
    in_process = pyqtSignal(str)
    finished = pyqtSignal(str)
    errored = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.func = None
        self.in_process_str = ""
        self.finished_str = ""

    def run(self):
        try:
            self.in_process.emit(self.in_process_str)
            self.func()
            self.finished.emit(self.finished_str)
        except Exception as err:
            self.errored.emit(str(err))

class VideoWorker(QThread):
    """ Thread for video player
    """

    play_in_process = pyqtSignal(str)
    update_slider_index = pyqtSignal(int)
    update_curr_frame = pyqtSignal(np.ndarray)

    def __init__(self, vid):
        QThread.__init__(self)
        self.play = True
        self.video = vid
        self.curr_frame = None
        self.curr_frame_idx = 0

    def play_video(self, frame_index):
        # while loop to play from curr_frame to end
        i = frame_index
        while i < len(self.video.frames):
            if not self.play:
                return
            self.curr_frame_idx = i
            self.curr_frame = self.video.frames[i]
            self.update_slider_index.emit(self.curr_frame_idx)
            self.update_curr_frame.emit(self.curr_frame)
            i = (i + 1) % len(self.video.frames)
            time.sleep(1 / self.video.framerate)
        self.curr_frame_idx = 0

    def run(self):
        self.play_in_process.emit("playing video")
        self.play_video(self.curr_frame_idx)


class GuiWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.process = Process(triangulate=self.triangulation_check_box.isChecked())
        self.triangulation = Triangulation(image_scale=10 / 100)
        self.worker = GeneralWorker()
        self.have_file = False
        self.applied_changes = True
        self.allow_preview_update = True
        self.dark_mode = True
        self.curr_frame = None

        # video setup
        self.video = Video()
        self.playback_thread = VideoWorker(self.video)
        self.playback_thread.update_slider_index.connect(self.update_video_slider)
        self.playback_thread.update_curr_frame.connect(self.set_curr_frame)
        self.play = False

        # preview set up
        self.preview_worker = GeneralWorker()
        self.preview_worker.in_process.connect(self.on_preview_updating)
        self.preview_worker.finished.connect(self.enable_options)
        self.preview_worker.func = self.display_preview_from_playback
        self.preview_worker.in_process_str = "PROCESSING PREVIEW..."

        # Video Playback ui
        self.video_slider.setPageStep(0)
        self.play_button.clicked.connect(self.on_play_clicked)
        self.video_slider.valueChanged['int'].connect(self.update_playback_index)
        self.video_slider.sliderPressed.connect(self.on_slider_pressed)
        self.video_slider.sliderReleased.connect(self.on_slider_released)
        self.stop_button.clicked.connect(self.on_stop)

        # GUI Setup
        self.triangulation_check_box._handle_checked_brush.setColor(QtGui.QColor('#b4b4b4'))
        self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#135680'))
        self.mode_toggle._bar_brush.setColor(QtGui.QColor('#135680'))
        self.mode_toggle._handle_brush.setColor(QtGui.QColor('#b4b4b4'))
        self.mode_toggle._bar_checked_brush.setColor(QtGui.QColor('#973680'))
        self.mode_toggle._handle_checked_brush.setColor(QtGui.QColor('#b4b4b4'))
        self.mode_toggle._pulse_unchecked_animation = QtGui.QBrush(QtGui.QColor('#444AB9AF'))
        self.mode_toggle._pulse_checked_animation = QtGui.QBrush(QtGui.QColor('#44EBCAB5'))
        self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.stop_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.width = self.height = 0

        self.mode_toggle.toggled['bool'].connect(self.dark_light_mode)

        # Pop-up Dialog  
        self.warning_dialogue = WarningDialogue()
        self.file_dialogue = FileDialogue(self.video)
        self.file_dialogue.finished.connect(self.thread_load_video)

        # filter options
        self.hue_spinBox.editingFinished.connect(self.set_hue)
        self.saturation_spinBox.editingFinished.connect(self.set_saturation)
        self.brightness_spinBox.editingFinished.connect(self.set_brightness)
        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.hue_slider.sliderReleased.connect(self.set_hue)
        self.saturation_slider.sliderReleased.connect(self.set_saturation)
        self.brightness_slider.sliderReleased.connect(self.set_brightness)
        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.max_points_spinBox.editingFinished.connect(self.set_num_pts)
        self.max_points_spinBox.editingFinished.connect(self.set_num_pts)
        self.poisson_disk_radioButton.toggled['bool'].connect(self.set_sampling_method)
        self.scale_factor_comboBox.currentTextChanged['QString'].connect(self.set_image_scale)
        self.draw_line_checkBox.toggled['bool'].connect(self.set_line)
        self.thickness_slider.sliderReleased.connect(self.set_line_thickness)
        self.thickness_spinBox.editingFinished.connect(self.set_line_thickness)

        # file options
        self.apply_button.clicked.connect(self.thread_process_video)
        self.reset_button.clicked.connect(self.thread_load_video)
        self.open_button.clicked.connect(self.open_dialog)
        self.export_button.clicked.connect(self.thread_export_video)

        self.all_options.setEnabled(False)
        
    # setter functions

    def _update_func(func, *args, **kwargs):
        def inner(self, *args, **kwargs):
            func(self, *args, *kwargs)
            if self.allow_preview_update:
                self.applied_changes = False
                self.reset_button.setEnabled(True)
            if self.have_file and not self.play and self.allow_preview_update:
                self.thread_update_preview()

        return inner

    @_update_func
    def set_triangulation(self, triangulate):
        self.process.triangulate = triangulate

    @_update_func
    def set_hue(self):
        self.process.hue = self.hue_spinBox.value()
        self.hue_slider.setValue(self.hue_spinBox.value())

    @_update_func
    def set_saturation(self):
        self.process.saturation = self.saturation_spinBox.value()
        self.saturation_slider.setValue(self.saturation_spinBox.value())

    @_update_func
    def set_brightness(self):
        self.process.brightness = self.brightness_spinBox.value()
        self.brightness_slider.setValue(self.brightness_spinBox.value())

    @_update_func
    def set_num_pts(self):
        self.triangulation.num_points = self.max_points_spinBox.value()

    @_update_func
    def set_sampling_method(self, method):
        # Open Warning Dialogue if Poisson Disk is selected
        if method:
            self.warning_dialogue.warning_message.setText(
                "Although Poisson Disk Sampling results in better output, \n"
                "it significantly slows down the triangulation\n\n"
                "Are you sure you want to select this option?")
            self.warning_dialogue.exec_()
        
        # If Cancel is clicked, warning_dialogue.cancel_changes is set to False thus resetting radio button and warning_dialogue.cancel_changes
        if self.warning_dialogue.cancel_changes:
            self.triangulation.pds = method
        else:
            self.threshold_radioButton.setChecked(True)
            self.warning_dialogue.cancel_changes = True


    @_update_func
    def set_image_scale(self, scale):
        scale_num = int(scale[:-1])                         #Scale Factor is used when downsizes the image for colors sampling
        if scale_num >= 50:                               #Factor by which the image is downsized when sampling colors
                                                           #Higher values increase color accuracy at the expense of speed
            self.warning_dialogue.warning_message.setText("This determines the size of frames used when sampling colors.\n"
                                                          "Higher values increase color accuracy but decrease speed.\n\n"
                                                          f"Are you sure you want the scale factor to be {scale}?")
            self.warning_dialogue.exec_()

        if self.warning_dialogue.cancel_changes:
            self.triangulation.image_scale = scale_num
        else:
            self.scale_factor_comboBox.setCurrentText(f'{int(self.triangulation.image_scale)}%')
            self.warning_dialogue.cancel_changes = True

    @_update_func
    def set_line(self, line):
        self.triangulation.draw_line = line

    @_update_func
    def set_line_thickness(self):
        self.triangulation.line_thickness = self.thickness_spinBox.value()
        self.thickness_slider.setValue(self.thickness_spinBox.value())

    def resizeEvent(self, event):
        self.width = self.video_player.width()
        self.height = self.video_player.height()
        if self.have_file and not self.play and self.allow_preview_update and self.video_player.pixmap() != None:
            self.set_curr_frame(self.curr_frame)

    ### filter functions ###

    def reset_filters(self):
        self.allow_preview_update = False
        
        self.hue_spinBox.setValue(0)
        self.saturation_spinBox.setValue(100)
        self.brightness_spinBox.setValue(100)
        self.max_points_spinBox.setValue(2000)
        self.triangulation_check_box.setChecked(False)
        self.threshold_radioButton.setChecked(True)
        self.poisson_disk_radioButton.setChecked(False)
        self.scale_factor_comboBox.setCurrentIndex(1)
        self.draw_line_checkBox.setChecked(False)
        self.thickness_spinBox.setValue(1)

        self.set_hue()
        self.set_saturation()
        self.set_brightness()
        self.set_num_pts()
        self.set_line_thickness()

        self.allow_preview_update = True

    def disable_options(self, s):
        if self.dark_mode == True:
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#4D4D4D'))
        else:
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#E0E0E0'))
        self.update_console_message(s)
        self.export_button.setEnabled(False)
        self.open_button.setEnabled(False)
        self.apply_button.setEnabled(False)
        self.video_slider.setEnabled(False)
        self.play_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.reset_button.setEnabled(False)
        self.all_options.setEnabled(False)

    def enable_options(self):
        if self.dark_mode == True:
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#135680'))
        else:
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#973680'))
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.apply_button.setEnabled(True)
        self.video_slider.setEnabled(True)
        self.play_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.all_options.setEnabled(True)

    # appearance functions

    def dark_light_mode(self, mode):
        if mode == True:
            self.dark_mode = False
            self.setStyleSheet(StyleSheet().light_mode)
            self.file_dialogue.setStyleSheet(StyleSheet().light_mode)
            self.warning_dialogue.setStyleSheet(StyleSheet().light_mode)
            if self.triangulation_check_box.isEnabled() == True:
                self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#973680'))
            else:
                self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#E0E0E0'))
        else:
            self.dark_mode = True
            self.file_dialogue.setStyleSheet(StyleSheet().dark_mode)
            self.warning_dialogue.setStyleSheet(StyleSheet().dark_mode)
            self.setStyleSheet(StyleSheet().dark_mode)
            if self.triangulation_check_box.isEnabled() == True:
                self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#135680'))
            else:
                self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#4D4D4D'))

    ### video functions ###

    def set_curr_frame(self, img):
        p = self.frame_to_qt(img)
        self.video_player.setPixmap(QtGui.QPixmap.fromImage(p))

    def update_video_slider(self, index):
        self.video_slider.setValue(index)

    def on_slider_pressed(self):
        
        self.playback_thread.play = False

    def on_slider_released(self):
        self.playback_thread.play = self.play
        if self.play:
            self.playback_thread.start()
        else:
            self.thread_update_preview()

    def update_playback_index(self, index):
        self.playback_thread.curr_frame_idx = index
        self.playback_thread.curr_frame = self.video.frames[index]
        self.set_curr_frame(self.video.frames[index])

    def on_play_clicked(self):
        if self.have_file:
            self.play = not self.play
            self.playback_thread.play = self.play
            if self.play:
                self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
                self.playback_thread.start()
            else:
                self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
                self.thread_update_preview()

    def on_stop(self):
        if self.have_file:
            self.play = False
            self.playback_thread.play = False

            self.playback_thread.curr_frame_idx = 0
            self.playback_thread.curr_frame = self.video.frames[0]

            self.video_slider.setValue(0)
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            self.thread_update_preview()

    def thread_update_preview(self):
        if not self.applied_changes:
            self.preview_worker.start()

    def on_preview_updating(self, s):
        self.video_player.setText(s)
        self.disable_options('');

    ### file functions ###

    def open_dialog(self):
        self.file_dialogue.exec_()

    def process_video(self):
        self.video.process_video(self.process.apply_filters)
        if self.process.triangulate:
            self.video.process_video(self.triangulation.apply_triangulation)

    def thread_load_video(self):
        try:
            if self.play and self.have_file:
                self.play = False
                self.playback_thread.play = False
                self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

            reconnect(self.worker.in_process, self.disable_options)
            reconnect(self.worker.finished, self.on_load_finished)
            reconnect(self.worker.errored, self.on_load_errored)

            self.worker.func = self.video.load_frames
            self.width = self.video_player.width()
            self.height = self.video_player.height()
            self.worker.in_process_str = f"Loading frames from {os.path.basename(self.video.filename)}..."
            self.worker.finished_str = f"All frames from {os.path.basename(self.video.filename)} loaded and ready"
            self.worker.start()

        except Exception:
            self.on_load_errored("Failed to load video")

    def thread_process_video(self):
        if self.play and self.have_file:
                self.play = False
                self.playback_thread.play = False
                self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

        reconnect(self.worker.in_process, self.disable_options)
        reconnect(self.worker.finished, self.on_process_finished)
        reconnect(self.worker.errored, self.on_process_finished)

        self.worker.func = self.process_video
        self.worker.in_process_str = "Applying changes to all frames, please wait..."
        self.worker.finished_str = "All frames processed"
        self.worker.start()

    def thread_export_video(self):
        if not self.applied_changes:
            self.warning_dialogue.warning_message.setText("The currently previewed changes have not been\n"
                                                          "applied to the actual video.\n\n"
                                                            "Are you sure you would like to proceed?")
            self.warning_dialogue.exec_()  

        if not self.warning_dialogue.cancel_changes:
            self.warning_dialogue.cancel_changes = True
            return
        else:
            file_filter = '.avi;; .mov;; .mkv;; .mp4'
            output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(parent=self, filter=file_filter)
            if output_filename is None or output_filename == "":
                self.update_console_message("")
                return

            def export():
                self.video.export_video(output_filename + extension)

            reconnect(self.worker.in_process, self.on_exporting)
            reconnect(self.worker.finished, self.on_export_finished)
            reconnect(self.worker.errored, self.on_export_finished)

            self.worker.func = export
            self.worker.in_process_str = f"Writing to {os.path.basename(output_filename + extension)}..."
            self.worker.finished_str = "Write finished, go take a look"
            self.worker.start()

    def on_exporting(self, s):
        self.update_console_message(s)
        self.open_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.apply_button.setEnabled(False)
        self.reset_button.setEnabled(False)

    def on_process_finished(self, s):
        self.update_console_message(s)
        self.reset_filters()
        self.enable_options()
        self.applied_changes = True
        self.update_playback_index(self.playback_thread.curr_frame_idx)
        self.curr_frame = self.playback_thread.curr_frame

    def on_load_finished(self, s):
        if len(self.video.frames) == 0:
            self.update_console_message("No file loaded")
            self.open_button.setEnabled(True)
            if self.have_file:
                self.export_button.setEnabled(True)
                self.apply_button.setEnabled(True)
                self.video_slider.setEnabled(True)
                self.play_button.setEnabled(True)
                self.stop_button.setEnabled(True)

            return

        self.applied_changes = True
        self.reset_filters()
        self.playback_thread.curr_frame_idx = 0
        self.playback_thread.curr_frame = self.playback_thread.video.frames[self.playback_thread.curr_frame_idx]
        self.have_file = True
        self.video_slider.setMaximum(len(self.video.frames) - 1)
        self.video_slider.setMinimum(0)
        self.video_slider.setValue(0)
        self.enable_options()
        self.reset_button.setEnabled(False)
        self.update_console_message(s)
        self.display_preview_from_playback()

    def on_load_errored(self, s):
        if not self.have_file:
            self.update_console_message(s)
            self.open_button.setEnabled(True)
        else:
            self.on_load_finished(s)
            self.reset_button.setEnabled(True)

    def on_export_finished(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.apply_button.setEnabled(True)
        self.reset_button.setEnabled(True)

    ### helper functions ###
    def update_console_message(self, message):
        self.status_message.setText(message)

    def display_preview_from_playback(self):
        image = self.process.apply_filters(self.playback_thread.curr_frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        self.curr_frame = image
        self.set_curr_frame(image)

    def frame_to_qt(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
        return pic

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StyleSheet().dark_mode)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
