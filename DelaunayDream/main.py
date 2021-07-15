import cv2
import sys
import time
import os
import numpy as np
from timeit import timeit


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from DelaunayDream.gui.gui import Ui_MainWindow
from DelaunayDream.gui.dialog import Ui_Dialog ####Octavio's Changes####
from DelaunayDream.gui.stylesheet import StyleSheet  ####Octavio's Changes####
from DelaunayDream.triangulation.triangulation import Triangulation
from DelaunayDream.videopipe.video import Video
from DelaunayDream.videopipe.process import Process




""" Thread for video player
"""
class video_worker(QThread):
    play_in_process = pyqtSignal(str)
    pause_sig = pyqtSignal(int)
    #update_curr_frame = pyqtSignal(QtGui.QImage)
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
        while i < len(self.video.result_frames):
            if self.pause:
                self.pause_sig.emit(self.curr_frame_idx)
                self.update_curr_frame.emit(self.curr_frame)
                return
            
            self.curr_frame_idx = i
            self.curr_frame = self.video.result_frames[i]
            #qt_curr_frame = self.frame_to_qt(self.curr_frame)
            #self.update_curr_frame.emit(qt_curr_frame)
            self.update_curr_frame.emit(self.curr_frame)
            i += 1
            time.sleep(1/self.video.output_fps)
        self.curr_frame_idx = 0
        #self.curr_frame = self.video.result_frames[self.curr_frame_idx]

        #for loop to play the from start to end
        # for frame in self.video.result_frames:
        #     if self.pause:
        #         self.pause_sig.emit(self.curr_frame, self.curr_frame_idx)
        #         return
        #     if self.resume:

        #     self.curr_frame = frame
        #     self.curr_frame_idx = self.video.result_frames.index(self.curr_frame)
        #     qt_curr_frame = self.frame_to_qt(self.curr_frame)
        #     self.update_curr_frame.emit(qt_curr_frame)
        #     time.sleep(1/self.video.output_fps)
    def run(self):
        self.play_in_process.emit("playing video")
        self.play_video(self.curr_frame_idx)


""" Thread for file loading
"""
class load_worker(QThread):
    load_in_process = pyqtSignal(str)
    load_finished = pyqtSignal(Video, str)
    def __init__(self, filename):
        QThread.__init__(self)
        self.video = Video()
        self.filename = filename

    def load_file(self, filename):
        if filename != '':
            self.video.filename = filename
            self.video.get_frames()

            #self.frame = self.video.frame_list[0]
    def run(self):
        self.load_in_process.emit(f"Loading frames from {os.path.basename(self.filename)}...")
        self.load_file(self.filename)
        self.load_finished.emit(self.video, f"All frames from {os.path.basename(self.filename)} loaded and ready")

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
        self.video.apply_output_framerate(self.video.output_fps)# reduce(1-30) this value for faster testing
        print("Time to apply filters:", timeit(lambda:self.video.process_video(self.process.apply_filters), number=1))
        if self.process.triangulate:
            print("Time to triangulate:", timeit(lambda:self.video.process_video(self.triangulation.apply_triangulation), number=1))

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
        self.triangulation = Triangulation(image_scale=self.scale_factor_spinBox.value()/100)
        self.have_file = False
        #self.frame = None
        # self.curr_frame_index = -1
        #self.original = None
        self.video = Video()
        self.playback_thread = video_worker(self.video)

        ####Octavio's Changes####
        self.play = True
        self.temp_filename = ""
        self.width = self.height = 0
        self.mode = False

        # Pop-up Dialog       
        self.dialog = QtWidgets.QDialog(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.browse_button.clicked.connect(self.set_filename)
        self.ui.file_lineEdit.textChanged[str].connect(self.onChanged)
        self.ui.frame_rate_selector.highlighted['QString'].connect(self.set_frame_rate)
        self.ui.confirm_cancel_button.accepted.connect(self.thread_load_video)
        self.ui.confirm_cancel_button.accepted.connect(self.dialog.close)
        self.ui.confirm_cancel_button.rejected.connect(self.dialog.close)
        
        #Video Playback
        self.play_button.clicked.connect(self.set_play_button)
        #self.stop_button.clicked.connect(self.dark_light_mode)
        #########################

        # TODO: remove these two once the gui is ready
        # self.frame_rate_spinBox.valueChanged['int'].connect(self.set_frame_rate)
        # self.frame_rate_spinBox.setValue(self.video.fps)

        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)

        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.max_points_spinBox.valueChanged['int'].connect(self.set_num_pts)
        self.threshold_spinBox.valueChanged['double'].connect(self.set_threshold)
        self.scale_factor_spinBox.valueChanged['int'].connect(self.set_image_scale)
        self.draw_line_checkBox.toggled['bool'].connect(self.set_line)
        self.thickness_spinBox.valueChanged['int'].connect(self.set_line_thickness)

        self.apply_button.clicked.connect(self.thread_process_video)
        self.open_button.clicked.connect(self.open_dialog) ####Octavio's Changes####
        self.export_button.setEnabled(False)
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

    @_update_func # TODO: remove this after gui is ready
    def set_frame_rate(self, frame_rate):
        return  # not functional until framerate changes are in

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
    def set_threshold(self, threshold):
        self.triangulation.threshold = threshold

    @_update_func
    def set_image_scale(self, scale):
        self.triangulation.image_scale = scale

    @_update_func
    def set_line(self, line):
        self.triangulation.draw_line = line

    @_update_func
    def set_line_thickness(self, thickness):
        self.triangulation.line_thickness = thickness

    
    # def update(self):
    #     #TODO:find another way to clear status message
    #     #currently removed for threading
    #     #self.update_console_message('')
    #     image = self.process.apply_filters(self.frame)
    #
    #     if self.process.triangulate:
    #         image = self.triangulation.apply_triangulation(image)
    #
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
    #     pic = to_qt.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio) ####Octavio's Changes####
    #     self.video_player.setPixmap(QtGui.QPixmap.fromImage(pic))
    
    def update_from_thread(self):
        image = self.process.apply_filters(self.playback_thread.curr_frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        # pic = to_qt.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        pic = self.frame_to_qt(image)
        self.video_player.setPixmap(QtGui.QPixmap.fromImage(pic))
    
    ####Octavio's Changes####
    def resizeEvent(self, event):
        self.width = self.video_player.width()
        self.height = self.video_player.height()

    def open_dialog(self):
        self.dialog.exec_()

    def set_filename(self):
        self.temp_filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        self.ui.file_lineEdit.setText(self.temp_filename)

    def onChanged(self, text):
        self.temp_filename = text

    def set_play_button(self):
        if self.play == True:
            self.play = False
            self.play_button.setText("Pause")
        else:
            self.play = True
            self.play_button.setText("Play")
    
    #def dark_light_mode(self):
       # if self.mode == True: 
            #self.setStyleSheet(StyleSheet().light_mode)
            #self.mode = False
        #else:
            #self.setStyleSheet(StyleSheet().dark_mode)
            #self.mode = True
    #########################


    def on_receving_msg(self, s):
        self.update_console_message(s)

    def on_loading(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(False)
        self.open_button.setEnabled(False)

    def on_applying(self, s):
        self.update_console_message(s)
        self.apply_button.setEnabled(False)
        self.open_button.setEnabled(False)
        self.export_button.setEnabled(False)

    def on_apply_finished(self, s, vid, proc):
        self.update_console_message(s)
        self.video = vid
        self.playback_thread.video = vid
        self.playback_thread.curr_frame = self.playback_thread.video.result_frames[self.playback_thread.curr_frame_idx]
        self.set_curr_frame(self.playback_thread.curr_frame)
        self.process = proc
        self.apply_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.export_button.setEnabled(True)
    
    def on_load_finished(self, v, s):
        self.video = v
        if len(self.video.frame_list) == 0:
            self.update_console_message("No file loaded")
            return
        
        # self.curr_frame_index = 0   #initialize frame index to the start of the video
        # self.curr
        
        self.playback_thread.video = self.video
        self.playback_thread.curr_frame_idx = 0
        self.playback_thread.curr_frame = self.playback_thread.video.result_frames[self.playback_thread.curr_frame_idx]
        self.set_curr_frame (self.playback_thread.curr_frame)
        self.have_file = True
        #self.update()
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)
        self.update_console_message(s)

    def on_exporting(self, s):
        self.update_console_message(s)
        self.open_button.setEnabled(False)
        self.export_button.setEnabled(False)

    def on_export_finished(self, s):
        self.update_console_message(s)
        self.export_button.setEnabled(True)
        self.open_button.setEnabled(True)

    # TODO: don't create a new object every time these functions are called

    def thread_load_video(self):
        # self.update_console_message("Choose a file to open")
        # filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        self.open_button.setEnabled(False) ####Octavio's Changes####
        filename = self.temp_filename ####Octavio's Changes####
        self.worker = load_worker(filename)
        self.worker.load_in_process.connect(self.on_loading)
        self.worker.load_finished.connect(self.on_load_finished)
        self.worker.start()

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
