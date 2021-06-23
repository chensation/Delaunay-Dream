from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DelaunayDream.triangulation.triangulate import triangulate_frame
from DelaunayDream.triangulation.get_points import generate_sample_points

from DelaunayDream.videopipe.Video import Video
from DelaunayDream.videopipe.process import Process
import sys, cv2
from DelaunayDream.gui.gui import Ui_MainWindow

class GUI_Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.process = Process()
        self.filename = ''
        self.frame = None
        self.original = None

        #### WIDGET FUNCTIONS ####
        self.retranslateUi(self)

        #frame_rate
        self.frame_rate_spinBox.valueChanged['int'].connect(self.frame_rate_slider.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.frame_rate_spinBox.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.setFrameRate)

        #hue
        self.hue_slider.valueChanged['int'].connect(self.hue_spinBox.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.hue_slider.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.setHue)

        #saturation
        self.saturation_slider.valueChanged['int'].connect(self.saturation_spinBox.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.saturation_slider.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.setSaturation)

        #brightness
        self.brightness_slider.valueChanged['int'].connect(self.brightness_spinBox.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.brightness_slider.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.setBrightness)

        #triangulate
        self.triangulation_check_box.toggled['bool'].connect(self.setTriangulation)
        
        self.open_button.clicked.connect(self.loadVideo)
        self.export_button.clicked.connect(self.exportVideo)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def setTriangulation(self, triangulate):
        self.process.triangulate = triangulate    
    
    def setFrameRate(self, frame_rate):
        self.process.frame_rate = frame_rate
        if self.filename != '':
            self.update()

    def setHue(self, hue):
        self.process.hue = hue
        if self.filename != '':
            self.update()

    def setSaturation(self, saturation):
        self.process.saturation = saturation
        if self.filename != '':
            self.update()

    def setBrightness(self, brightness):
        self.process.brightness = brightness
        if self.filename != '':
            self.update()

    def update(self):
        #image = self.process.changeBrightness(self.frame)
        image = self.process.applyFilters(self.frame)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        to_qt = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        pic = to_qt.scaled(700, 700, Qt.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(pic))
        
    def loadVideo(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        if self.filename != '':
            self.frame = cv2.imread(self.filename)
            self.update()

    def exportVideo(self):
        output_filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        if output_filename != '':    
            # image = self.process.changeBrightness(self.frame)
            image = self.process.applyFilters(self.frame)
            cv2.imwrite(output_filename, image)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI_Window()
    gui.show()
    sys.exit(app.exec_())