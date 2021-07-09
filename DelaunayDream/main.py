import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from DelaunayDream.gui.gui import Ui_MainWindow
from DelaunayDream.triangulation.triangulation import Triangulation
from DelaunayDream.videopipe.video import Video
from DelaunayDream.videopipe.process import Process


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
        self.frame_rate_spinBox.setValue(5)

        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)

        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)
        self.max_points_spinBox.valueChanged['int'].connect(self.set_num_pts)
        self.threshold_spinBox.valueChanged['double'].connect(self.set_threshold)
        self.scale_factor_spinBox.valueChanged['int'].connect(self.set_image_scale)
        self.draw_line_checkBox.toggled['bool'].connect(self.set_line)
        self.thickness_spinBox.valueChanged['int'].connect(self.set_line_thickness)

        self.apply_button.clicked.connect(self.process_video)
        self.open_button.clicked.connect(self.load_video)
        self.export_button.clicked.connect(self.export_video)

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
        self.update_console_message('')
        image = self.process.apply_filters(self.frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.video_player.setPixmap(QtGui.QPixmap.fromImage(pic))

    def load_video(self):
        self.update_console_message(f"reading from file...give it some time")
        filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        if filename != '':
            # self.frame = cv2.imread(self.filename)
            # self.update()
            self.have_file = True
            self.video.filename = filename
            self.video.get_frames()

            self.frame = self.video.frame_list[0]
            self.update()
            self.update_console_message("All frames loaded and ready")

        else:
            self.update_console_message("")

    def process_video(self):

        self.update_console_message("Applying changes to all frames, please wait...")
        # TODO: temp solution until gui for selecting fps on open video is ready
        self.video.apply_output_framerate(self.video.output_fps)

        self.video.process_video(self.process.apply_filters)
        if self.process.triangulate:
            self.video.process_video(self.triangulation.apply_triangulation)

        self.update_console_message("All frames processed")

    def export_video(self):
        # output_filename = QtWidgets.QFileDialog.getSaveFileName(filter="Video files(*.*)")[0]
        # image = self.process.changeBrightness(self.frame)   setDefaultSuffix(".avi").
        # image = self.process.apply_filters(self.frame)
        # cv2.imwrite(output_filename, image)
        self.update_console_message(f"writing to file...it'll take a minute")
        output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(filter=self.tr(".avi"))
        if output_filename != '':

            self.video.export_video(output_filename + extension)
            #  self.video.generate_with_fps(output_filename + extension, self.user_fps)
            self.update_console_message("Write finished, go take a look")
        else:
            self.update_console_message("")

    def update_console_message(self, message):
        self.status_message.setText(message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
