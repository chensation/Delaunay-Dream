import cv2
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from DelaunayDream.gui.gui import Ui_MainWindow
from DelaunayDream.triangulation.triangulation import Triangulation
from DelaunayDream.videopipe.video import Video
from DelaunayDream.videopipe.process import Process


""" Thread for file loading
"""
class load_worker(QThread):
    load_in_process = pyqtSignal(str)
    load_finished = pyqtSignal(Video, str)
    def __init__(self, filename):
        QThread.__init__(self)
        self.video = Video()
        self.filename = filename
    def __del__(self):
        self.wait()
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
    def __del__(self):
        self.wait()
    def process_video(self):
        self.video.apply_output_framerate(5)# reduce(1-30) this value for faster testing
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
    def __del__(self):
        self.wait()
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
        self.frame = None
        self.original = None
        self.video = Video()

        # TODO: remove these two once the gui is ready
        self.frame_rate_spinBox.valueChanged['int'].connect(self.set_frame_rate)
        self.frame_rate_spinBox.setValue(self.video.fps)

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
        self.open_button.clicked.connect(self.thread_load_video)
        self.export_button.clicked.connect(self.thread_export_video)

    def _update_func(func, *args, **kwargs):
        def inner(self, *args, **kwargs):
            func(self, *args, *kwargs)
            if self.have_file:
                self.update()

        return inner

    @_update_func
    def set_triangulation(self, triangulate):
        self.process.triangulate = triangulate

    @_update_func # TODO: remove this after gui is ready
    def set_frame_rate(self, frame_rate):
        self.video.output_fps = frame_rate

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

    
    def update(self):
        #TODO:find another way to clear status message
        #currently removed for threading
        #self.update_console_message('')
        image = self.process.apply_filters(self.frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.video_player.setPixmap(QtGui.QPixmap.fromImage(pic))

    def on_receving_msg(self, s):
        self.update_console_message(s)

    def on_apply_finished(self, s, vid, proc):
        self.update_console_message(s)
        self.video = vid
        self.process = proc

    def on_load_finished(self, v, s):
        self.video = v
        self.have_file = True
        self.frame =self.video.frame_list[0]
        self.frame_rate_spinBox.setValue(self.video.fps)
        self.update()
        self.update_console_message(s)


    def thread_load_video(self):
        self.status_message.setText(f"Choose a file to open")
        filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        self.worker = load_worker(filename)
        self.worker.load_in_process.connect(self.on_receving_msg)
        self.worker.load_finished.connect(self.on_load_finished)
        self.worker.start()

    def thread_process_video(self):
        self.apply_worker = apply_worker(self.video, self.process, self.triangulation)
        self.apply_worker.apply_in_process.connect(self.on_receving_msg)
        self.apply_worker.apply_finished.connect(self.on_apply_finished)
        self.apply_worker.start()
        
    def thread_export_video(self):
        self.update_console_message("Enter filename and extension...")
        output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(filter=self.tr(".avi"))
        self.export_worker = export_worker(self.video, output_filename, extension)
        self.export_worker.export_in_process.connect(self.on_receving_msg)
        self.export_worker.export_finished.connect(self.on_receving_msg)
        self.export_worker.start()


    def update_console_message(self, message):
        self.status_message.setText(message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
