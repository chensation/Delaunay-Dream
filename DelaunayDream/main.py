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

""" Thread for video player
"""


class video_worker(QThread):
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


""" Thread for file loading
"""


class load_worker(QThread):
    load_in_process = pyqtSignal(str)
    load_finished = pyqtSignal(Video, str)

    def __init__(self, video):
        QThread.__init__(self)
        self.video = video

    def run(self):
        self.load_in_process.emit(f"Loading frames from {os.path.basename(self.video.filename)}...")
        self.video.load_frames()
        self.load_finished.emit(self.video, f"All frames from {os.path.basename(self.video.filename)} loaded and ready")


""" Thread for apply all changes
"""


class apply_worker(QThread):
    apply_in_process = pyqtSignal(str)
    apply_finished = pyqtSignal(str, Video, Process)

    def __init__(self, v, proc, tri):
        QThread.__init__(self)
        self.video = v
        self.process = proc
        self.triangulation = tri

    def process_video(self):
        self.video.process_video(self.process.apply_filters)
        if self.process.triangulate:
            self.video.process_video(self.triangulation.apply_triangulation)

    def run(self):
        self.apply_in_process.emit("Applying changes to all frames, please wait...")
        self.process_video()
        self.apply_finished.emit("All frames processed", self.video, self.process)


""" Thread for writing
"""


class export_worker(QThread):
    export_in_process = pyqtSignal(str)
    export_finished = pyqtSignal(str)

    def __init__(self, vid, filename, ex):
        QThread.__init__(self)
        self.video = vid
        self.filename = filename
        self.extension = ex

    def export_video(self):
        self.video.export_video(self.filename + self.extension)

    def run(self):
        self.export_in_process.emit(f"Writing to {os.path.basename(self.filename + self.extension)}...")
        self.export_video()
        self.export_finished.emit("Write finished, go take a look")


class GuiWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.process = Process(triangulate=self.triangulation_check_box.isChecked())
        self.triangulation = Triangulation(image_scale=10 / 100)
        self.have_file = False
        self.applied_changes = False

        # video setup
        self.video = Video()
        self.playback_thread = video_worker(self.video)
        self.playback_thread.update_slider_index.connect(self.update_video_slider)
        self.playback_thread.update_curr_frame.connect(self.set_curr_frame)
        self.play = False

        # Video Playback ui
        self.play_button.clicked.connect(self.on_play_clicked)
        self.video_slider.valueChanged['int'].connect(self.update_thread_index)
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
        self.play_button.setIcon(self.play_button.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.stop_button.setIcon(self.play_button.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.width = self.height = 0

        self.mode_toggle.toggled['bool'].connect(self.dark_light_mode)

        # Pop-up Dialog  
        self.warning_dialogue = WarningDialogue()
        self.file_dialogue = FileDialogue(self.video)
        self.file_dialogue.ok_button.clicked.connect(self.thread_load_video)

        # filter options
        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)
        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.max_points_spinBox.valueChanged['int'].connect(self.set_num_pts)
        self.poisson_disk_radioButton.toggled['bool'].connect(self.set_sampling_method)
        self.scale_factor_comboBox.currentTextChanged['QString'].connect(self.set_image_scale)
        self.draw_line_checkBox.toggled['bool'].connect(self.set_line)
        self.thickness_spinBox.valueChanged['int'].connect(self.set_line_thickness)

        # file options
        self.apply_button.clicked.connect(self.thread_process_video)
        self.reset_button.clicked.connect(self.on_reset_clicked)
        self.open_button.clicked.connect(self.open_dialog)
        self.export_button.setEnabled(False)
        self.apply_button.setEnabled(False)
        self.export_button.clicked.connect(self.thread_export_video)

    # setter functions

    def _update_func(func, *args, **kwargs):
        def inner(self, *args, **kwargs):
            func(self, *args, *kwargs)
            if self.have_file and not self.play:
                self.display_preview_from_playback()

        return inner

    @_update_func
    def set_triangulation(self, triangulate):
        self.process.triangulate = triangulate

    @_update_func
    def set_hue(self, hue):
        self.process.hue = hue

    @_update_func
    def set_saturation(self, saturation):
        self.process.saturation = saturation

    @_update_func
    def set_brightness(self, brightness):
        self.process.brightness = brightness

    @_update_func
    def set_num_pts(self, num):
        self.triangulation.num_points = num

    @_update_func
    def set_sampling_method(self, method):
        if method:
            self.warning_dialogue.warning_message.setText(
                "Poisson Disk significant slows down processing but results to \nbetter output")
            self.warning_dialogue.exec_()
        self.triangulation.pds = method

    @_update_func
    def set_image_scale(self, scale):
        scale_num = int(scale[:-1])
        if scale_num >= 50:
            self.warning_dialogue.warning_message.setText("Although a higher image scale allows more accurate colors, "
                                                          "it cause the triangulation to be much slower\n"
                                                          f"Are you sure you want the image scale to be {scale}?")
            self.warning_dialogue.exec_()

        self.triangulation.image_scale = int(scale[:-1])

    @_update_func
    def set_line(self, line):
        self.triangulation.draw_line = line

    @_update_func
    def set_line_thickness(self, thickness):
        self.triangulation.line_thickness = thickness

    @_update_func
    def resizeEvent(self, event):
        self.width = self.video_player.width()
        self.height = self.video_player.height()

    # appearance functions

    def dark_light_mode(self, mode):
        if mode == True:
            self.setStyleSheet(StyleSheet().light_mode)
            self.file_dialogue.setStyleSheet(StyleSheet().light_mode)
            self.warning_dialogue.setStyleSheet(StyleSheet().light_mode)
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#973680'))
        else:
            self.file_dialogue.setStyleSheet(StyleSheet().dark_mode)
            self.warning_dialogue.setStyleSheet(StyleSheet().dark_mode)
            self.setStyleSheet(StyleSheet().dark_mode)
            self.triangulation_check_box._bar_checked_brush.setColor(QtGui.QColor('#135680'))

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
            self.display_preview_from_playback()

    def update_thread_index(self, index):
        self.playback_thread.curr_frame_idx = index
        self.playback_thread.curr_frame = self.video.frames[index]
        self.set_curr_frame(self.video.frames[index])

    def on_play_clicked(self):
        if self.have_file:
            self.play = not self.play
            self.playback_thread.play = self.play
            if self.play:
                self.play_button.setIcon(self.play_button.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
                self.playback_thread.start()
            else:
                self.play_button.setIcon(self.play_button.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
                self.display_preview_from_playback()

    def on_stop(self):
        if self.have_file:
            self.play = False
            self.playback_thread.play = False

            self.playback_thread.curr_frame_idx = 0
            self.playback_thread.curr_frame = self.video.frames[0]

            self.video_slider.setValue(0)
            self.play_button.setIcon(self.play_button.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            self.display_preview_from_playback()

    ### file functions ###

    def open_dialog(self):
        self.file_dialogue.exec_()

    # TODO: don't create a new object every time these functions are called
    def thread_load_video(self):
        try:
            self.worker = load_worker(self.video)
            self.worker.load_in_process.connect(self.on_loading)
            self.worker.load_finished.connect(self.on_load_finished)
            self.worker.start()

        except Exception:
            self.update_console_message("Failed to load video")
            self.export_button.setEnabled(True)
            self.open_button.setEnabled(True)

    def thread_process_video(self):
        self.apply_worker = apply_worker(self.video, self.process, self.triangulation)
        self.apply_worker.apply_in_process.connect(self.on_applying)
        self.apply_worker.apply_finished.connect(self.on_apply_finished)
        self.apply_worker.start()

    def thread_export_video(self):
        if not self.applied_changes:
            message = "The \"Apply To All Frames\" button has not been clicked.\nNo options have been applied."
            self.warning_dialogue.warning_message.setText(message)
            self.warning_dialogue.exec_()
        file_filter = '.avi;; .wmv;; .mkv;; .mp4'
        output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(filter=file_filter)
        if output_filename is None or output_filename == "":
            self.update_console_message("")
            return

        self.export_worker = export_worker(self.video, output_filename, extension)
        self.export_worker.export_in_process.connect(self.on_exporting)
        self.export_worker.export_finished.connect(self.on_export_finished)
        self.export_worker.start()

    def on_loading(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(False)
        self.open_button.setEnabled(False)
        self.apply_button.setEnabled(False)
        self.video_slider.setEnabled(False)

    def on_applying(self, s):
        self.update_console_message(s)
        self.apply_button.setEnabled(False)
        self.open_button.setEnabled(False)
        self.export_button.setEnabled(False)

    def on_exporting(self, s):
        self.update_console_message(s)
        self.open_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.apply_button.setEnabled(False)

    def on_apply_finished(self, s, vid, proc):
        self.update_console_message(s)
        self.video = vid
        self.playback_thread.video = vid
        self.playback_thread.curr_frame = self.playback_thread.video.frames[self.playback_thread.curr_frame_idx]
        self.set_curr_frame(self.playback_thread.curr_frame)
        self.process = proc
        self.apply_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.export_button.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.reset_filters()

    def on_load_finished(self, v, s):
        self.video = v
        if len(self.video.frames) == 0:
            self.update_console_message("No file loaded")
            return

        self.playback_thread.video = self.video
        self.playback_thread.curr_frame_idx = 0
        self.playback_thread.curr_frame = self.playback_thread.video.frames[self.playback_thread.curr_frame_idx]
        self.set_curr_frame(self.playback_thread.curr_frame)
        self.have_file = True
        self.video_slider.setEnabled(True)
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.video_slider.setMaximum(len(self.video.frames) - 1)
        self.video_slider.setMinimum(0)
        self.video_slider.setValue(0)
        self.apply_button.setEnabled(True)
        self.reset_button.setEnabled(False)
        self.update_console_message(s)

    def on_export_finished(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.apply_button.setEnabled(True)

    ### helper functions ###

    def update_console_message(self, message):
        self.status_message.setText(message)

    def display_preview_from_playback(self):
        image = self.process.apply_filters(self.playback_thread.curr_frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        self.set_curr_frame(image)

    def frame_to_qt(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
        return pic

    def on_reset_clicked(self):
        self.reset_filters()
        self.thread_load_video()

    def reset_filters(self):
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StyleSheet().dark_mode)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
