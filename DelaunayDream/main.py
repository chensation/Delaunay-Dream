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
        self.process = Process()
        self.triangulation = Triangulation(image_scale=0.1)
        self.have_file = False
        self.frame = None
        self.original = None
        self.video = Video()

        self.frame_rate_slider.valueChanged['int'].connect(self.set_frame_rate)
        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)
        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)

        self.open_button.clicked.connect(self.load_video)
        self.export_button.clicked.connect(self.export_video)

    def set_triangulation(self, triangulate):
        self.process.triangulate = triangulate
        if self.have_file:
            self.update()

    def set_frame_rate(self, frame_rate):
        self.process.frame_rate = frame_rate
        if self.have_file:
            self.update()

    def set_hue(self, hue):
        self.process.hue = hue
        if self.have_file:
            self.update()

    def set_saturation(self, saturation):
        self.process.saturation = saturation
        if self.have_file:
            self.update()

    def set_brightness(self, brightness):
        self.process.brightness = brightness
        if self.have_file:
            self.update()

    def update(self):
        self.status_message.setText('')
        image = self.process.apply_filters(self.frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.image_preview.setPixmap(QtGui.QPixmap.fromImage(pic))

    def load_video(self):
        self.status_message.setText(f"reading from file...give it some time")
        filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        if filename != '':
            # self.frame = cv2.imread(self.filename)
            # self.update()
            self.have_file = True
            self.video.filename = filename
            self.video.get_frames()

            self.frame = self.video.frame_list[0]
            self.update()
            self.status_message.setText("All frames loaded and ready")

        else:
            self.status_message.setText("")

    def export_video(self):
        # output_filename = QtWidgets.QFileDialog.getSaveFileName(filter="Video files(*.*)")[0]
        # image = self.process.changeBrightness(self.frame)   setDefaultSuffix(".avi").
        # image = self.process.apply_filters(self.frame)
        # cv2.imwrite(output_filename, image)
        self.status_message.setText(f"writing to file...it'll take a minute")
        output_filename, extension = QtWidgets.QFileDialog.getSaveFileName(filter=self.tr(".avi"))
        if output_filename != '':

            self.video.process_video(self.process.apply_filters, True)
            if self.process.triangulate:
                self.video.process_video(self.triangulation.apply_triangulation, process_original=False)
            self.video.generate_color(output_filename + extension)
            self.status_message.setText("Write finished, go take a look")
        else:
            self.status_message.setText("")


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
