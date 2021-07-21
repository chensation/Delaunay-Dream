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


""" Thread for video player
"""
class video_worker(QThread):
    play_in_process = pyqtSignal(str)
    pause_sig = pyqtSignal(int)
    update_curr_frame = pyqtSignal(np.ndarray)
    def __init__(self, vid):
        QThread.__init__(self)
        self.pause = False
        self.video = vid
        self.curr_frame = None
        self.curr_frame_idx = -1

    def play_video(self, frame_index):
        #while loop to play from curr_frame to end
        i = frame_index
        self.pause = False
        while i < len(self.video.frames):
            if self.pause:
                self.pause_sig.emit(self.curr_frame_idx)
                self.update_curr_frame.emit(self.curr_frame)
                return
            
            self.curr_frame_idx = i
            self.curr_frame = self.video.frames[i]
            #qt_curr_frame = self.frame_to_qt(self.curr_frame)
            #self.update_curr_frame.emit(qt_curr_frame)
            self.update_curr_frame.emit(self.curr_frame)
            i += 1
            time.sleep(1/self.video.framerate)
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
        self.export_in_process.emit(f"Writing to {os.path.basename(self.filename + self. extension)}...")
        self.export_video()
        self.export_finished.emit("Write finished, go take a look")


class GuiWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.process = Process(triangulate=self.triangulation_check_box.isChecked())
        self.triangulation = Triangulation(image_scale=10/100)
        self.have_file = False

        self.video = Video()
        self.playback_thread = video_worker(self.video)

        ####Octavio's Changes####
        self.play = True
        # self.temp_filename = ""
        self.width = self.height = 0

        # Pop-up Dialog       
        self.file_dialogue = FileDialogue(self.video)
        self.file_dialogue.ok_button.clicked.connect(self.thread_load_video)

        #Video Playback
        self.play_button.clicked.connect(self.set_play_button)
        self.mode_toggle.toggled['bool'].connect(self.dark_light_mode)
        #########################

        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)

        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.max_points_spinBox.valueChanged['int'].connect(self.set_num_pts)
        self.poisson_disk_radioButton.toggled['bool'].connect(self.sampling_method)
        self.scale_factor_comboBox.highlighted['int'].connect(self.set_image_scale)
        self.draw_line_checkBox.toggled['bool'].connect(self.set_line)
        self.thickness_spinBox.valueChanged['int'].connect(self.set_line_thickness)

        self.apply_button.clicked.connect(self.thread_process_video)
        self.reset_button.clicked.connect(self.thread_load_video)
        self.open_button.clicked.connect(self.open_dialog)
        self.export_button.setEnabled(False)
        self.apply_button.setEnabled(False)
        self.export_button.clicked.connect(self.thread_export_video)
        self.play_button.clicked.connect(self.on_play_clicked)
        self.stop_button.clicked.connect(self.on_pause_clicked)

    def _update_func(func, *args, **kwargs):
        def inner(self, *args, **kwargs):
            func(self, *args, *kwargs)
            if self.have_file:
                #self.update()
                self.update_from_thread()

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
    def sampling_method(self, method):
        print(method)
        # self.triangulation.threshold = threshold

    @_update_func
    def set_image_scale(self, scale):
        if scale == 0:
            scale = 100
        elif scale == 1:
            scale = 50
        elif scale == 2:
            scale = 10
        else:
            scale = 1
        self.triangulation.image_scale = scale

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

    def update_from_thread(self):
        image = self.process.apply_filters(self.playback_thread.curr_frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        self.set_curr_frame(image)
    

    def open_dialog(self):
        self.file_dialogue.exec_()

    def set_play_button(self):
        if self.play == True:
            self.play = False
            self.play_button.setText("Pause")
        else:
            self.play = True
            self.play_button.setText("Play")
    
    def dark_light_mode(self, mode):
        if mode == False: 
            self.setStyleSheet(StyleSheet().light_mode)
        else:
            self.setStyleSheet(StyleSheet().dark_mode)

    def on_loading(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(False)
        self.open_button.setEnabled(False)
        self.apply_button.setEnabled(False)

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

    def on_load_finished(self, v, s):
        self.video = v
        if len(self.video.frames) == 0:
            self.update_console_message("No file loaded")
            return

        self.playback_thread.video = self.video
        self.playback_thread.curr_frame_idx = 0
        self.playback_thread.curr_frame = self.playback_thread.video.frames[self.playback_thread.curr_frame_idx]
        self.set_curr_frame (self.playback_thread.curr_frame)
        self.have_file = True
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.apply_button.setEnabled(True)
        self.reset_button.setEnabled(False)
        self.update_console_message(s)


    def on_export_finished(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.apply_button.setEnabled(True)


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
        self.update_console_message("Enter filename and extension...")
        file_filter = '.avi;; .wmv;; .mkv;; .mp4'
        output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(filter=file_filter)
        self.export_worker = export_worker(self.video, output_filename, extension)
        self.export_worker.export_in_process.connect(self.on_exporting)
        self.export_worker.export_finished.connect(self.on_export_finished)
        self.export_worker.start()

    def frame_to_qt(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
        return pic

    def set_curr_frame(self, img):
        p = self.frame_to_qt(img)
        self.video_player.setPixmap(QtGui.QPixmap.fromImage(p))

    def on_play_clicked(self):
        self.playback_thread.update_curr_frame.connect(self.set_curr_frame)
        self.playback_thread.start()

    #TODO: Connect to actual pause button
    #currently connected to stop button

    def on_pause_clicked(self):
        self.playback_thread.curr_frame = self.process.apply_filters(self.playback_thread.curr_frame)
        if self.process.triangulate:
            self.playback_thread.curr_frame = self.triangulation.apply_triangulation(self.playback_thread.curr_frame)
        self.playback_thread.pause = True

    def update_console_message(self, message):
        self.status_message.setText(message)



def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StyleSheet().light_mode)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
