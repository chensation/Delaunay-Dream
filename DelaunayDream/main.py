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
        self.filename = ''
        self.frame = None
        self.original = None

        # WIDGET FUNCTIONS
        self.retranslateUi(self)

        # frame_rate
        self.frame_rate_spinBox.valueChanged['int'].connect(self.frame_rate_slider.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.frame_rate_spinBox.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.set_frame_rate)

        # hue
        self.hue_slider.valueChanged['int'].connect(self.hue_spinBox.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.hue_slider.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.set_hue)

        # saturation
        self.saturation_slider.valueChanged['int'].connect(self.saturation_spinBox.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.saturation_slider.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.set_saturation)

        # brightness
        self.brightness_slider.valueChanged['int'].connect(self.brightness_spinBox.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.brightness_slider.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.set_brightness)

        # triangulate
        self.triangulation_check_box.toggled['bool'].connect(self.set_triangulation)

        self.open_button.clicked.connect(self.load_video)
        self.export_button.clicked.connect(self.export_video)
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_triangulation(self, triangulate):
        self.process.triangulate = triangulate
        if self.filename != '':
            self.update()

    def set_frame_rate(self, frame_rate):
        self.process.frame_rate = frame_rate
        if self.filename != '':
            self.update()

    def set_hue(self, hue):
        self.process.hue = hue
        if self.filename != '':
            self.update()

    def set_saturation(self, saturation):
        self.process.saturation = saturation
        if self.filename != '':
            self.update()

    def set_brightness(self, brightness):
        self.process.brightness = brightness
        if self.filename != '':
            self.update()

    def update(self):

        image = self.process.apply_filters(self.frame)

        if self.process.triangulate:
            image = self.triangulation.apply_triangulation(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        to_qt = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_RGB888)
        pic = to_qt.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(pic))

    def load_video(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        if self.filename != '':
            self.frame = cv2.imread(self.filename)
            self.update()

    def export_video(self):
        output_filename = QtWidgets.QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        if output_filename != '':
            # image = self.process.changeBrightness(self.frame)
            image = self.process.apply_filters(self.frame)
            cv2.imwrite(output_filename, image)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GuiWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
