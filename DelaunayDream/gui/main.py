# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dream.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 625)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\film.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1194, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1058, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(20, 538, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.video_playback_layout = QtWidgets.QVBoxLayout()
        self.video_playback_layout.setObjectName("video_playback_layout")
        self.video = QtWidgets.QLabel(self.layoutWidget)
        self.video.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.video.setText("")
        self.video.setPixmap(QtGui.QPixmap(".\\image.jpg"))
        self.video.setObjectName("video")
        self.video_playback_layout.addWidget(self.video)
        self.playback_slider = QtWidgets.QSlider(self.layoutWidget)
        self.playback_slider.setToolTip("")
        self.playback_slider.setMaximum(99)
        self.playback_slider.setOrientation(QtCore.Qt.Horizontal)
        self.playback_slider.setObjectName("playback_slider")
        self.video_playback_layout.addWidget(self.playback_slider)
        self.video_buttons_layout = QtWidgets.QHBoxLayout()
        self.video_buttons_layout.setObjectName("video_buttons_layout")
        spacerItem2 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.video_buttons_layout.addItem(spacerItem2)
        self.pause_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pause_button.setFont(font)
        self.pause_button.setObjectName("pause_button")
        self.video_buttons_layout.addWidget(self.pause_button)
        self.play_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.video_buttons_layout.addWidget(self.play_button)
        self.stop_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.video_buttons_layout.addWidget(self.stop_button)
        spacerItem3 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.video_buttons_layout.addItem(spacerItem3)
        self.video_playback_layout.addLayout(self.video_buttons_layout)
        self.horizontalLayout_8.addLayout(self.video_playback_layout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 498, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.side_panel_layout = QtWidgets.QVBoxLayout()
        self.side_panel_layout.setObjectName("side_panel_layout")
        self.triangulation_check_box = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.triangulation_check_box.setFont(font)
        self.triangulation_check_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.triangulation_check_box.setIconSize(QtCore.QSize(16, 16))
        self.triangulation_check_box.setTristate(False)
        self.triangulation_check_box.setObjectName("triangulation_check_box")
        self.side_panel_layout.addWidget(self.triangulation_check_box)
        spacerItem5 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem5)
        self.frame_rate_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.frame_rate_label.setFont(font)
        self.frame_rate_label.setObjectName("frame_rate_label")
        self.side_panel_layout.addWidget(self.frame_rate_label)
        self.frame_rate_layout = QtWidgets.QHBoxLayout()
        self.frame_rate_layout.setObjectName("frame_rate_layout")
        self.frame_rate_slider = QtWidgets.QSlider(self.layoutWidget)
        self.frame_rate_slider.setOrientation(QtCore.Qt.Horizontal)
        self.frame_rate_slider.setObjectName("frame_rate_slider")
        self.frame_rate_layout.addWidget(self.frame_rate_slider)
        self.frame_rate_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.frame_rate_spinBox.setFont(font)
        self.frame_rate_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_rate_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.frame_rate_spinBox.setMaximum(99)
        self.frame_rate_spinBox.setObjectName("frame_rate_spinBox")
        self.frame_rate_layout.addWidget(self.frame_rate_spinBox)
        self.side_panel_layout.addLayout(self.frame_rate_layout)
        spacerItem6 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem6)
        self.hue_Label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.hue_Label.setFont(font)
        self.hue_Label.setObjectName("hue_Label")
        self.side_panel_layout.addWidget(self.hue_Label)
        self.hue_layout = QtWidgets.QHBoxLayout()
        self.hue_layout.setObjectName("hue_layout")
        self.hue_slider = QtWidgets.QSlider(self.layoutWidget)
        self.hue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_slider.setObjectName("hue_slider")
        self.hue_layout.addWidget(self.hue_slider)
        self.hue_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.hue_spinBox.setFont(font)
        self.hue_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hue_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.hue_spinBox.setMaximum(99)
        self.hue_spinBox.setObjectName("hue_spinBox")
        self.hue_layout.addWidget(self.hue_spinBox)
        self.side_panel_layout.addLayout(self.hue_layout)
        spacerItem7 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem7)
        self.saturation_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.saturation_label.setFont(font)
        self.saturation_label.setObjectName("saturation_label")
        self.side_panel_layout.addWidget(self.saturation_label)
        self.saturation_layout = QtWidgets.QHBoxLayout()
        self.saturation_layout.setObjectName("saturation_layout")
        self.saturation_slider = QtWidgets.QSlider(self.layoutWidget)
        self.saturation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_slider.setObjectName("saturation_slider")
        self.saturation_layout.addWidget(self.saturation_slider)
        self.saturation_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.saturation_spinBox.setFont(font)
        self.saturation_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.saturation_spinBox.setMaximum(99)
        self.saturation_spinBox.setObjectName("saturation_spinBox")
        self.saturation_layout.addWidget(self.saturation_spinBox)
        self.side_panel_layout.addLayout(self.saturation_layout)
        spacerItem8 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem8)
        self.brightness_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.brightness_label.setFont(font)
        self.brightness_label.setObjectName("brightness_label")
        self.side_panel_layout.addWidget(self.brightness_label)
        self.brightness_layout = QtWidgets.QHBoxLayout()
        self.brightness_layout.setObjectName("brightness_layout")
        self.brightness_slider = QtWidgets.QSlider(self.layoutWidget)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.brightness_layout.addWidget(self.brightness_slider)
        self.brightness_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.brightness_spinBox.setFont(font)
        self.brightness_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.brightness_spinBox.setMaximum(99)
        self.brightness_spinBox.setObjectName("brightness_spinBox")
        self.brightness_layout.addWidget(self.brightness_spinBox)
        self.side_panel_layout.addLayout(self.brightness_layout)
        spacerItem9 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem10)
        self.apply_changes_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.apply_changes_button.setFont(font)
        self.apply_changes_button.setObjectName("apply_changes_button")
        self.side_panel_layout.addWidget(self.apply_changes_button)
        spacerItem11 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.side_panel_layout.addItem(spacerItem12)
        self.open_export_layout = QtWidgets.QHBoxLayout()
        self.open_export_layout.setObjectName("open_export_layout")
        self.open_button = QtWidgets.QPushButton(self.layoutWidget)
        self.open_button.setObjectName("open_button")
        self.open_export_layout.addWidget(self.open_button)
        self.export_button = QtWidgets.QPushButton(self.layoutWidget)
        self.export_button.setObjectName("export_button")
        self.open_export_layout.addWidget(self.export_button)
        self.side_panel_layout.addLayout(self.open_export_layout)
        self.horizontalLayout_8.addLayout(self.side_panel_layout)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem13 = QtWidgets.QSpacerItem(20, 538, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem14 = QtWidgets.QSpacerItem(1058, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")

        self.retranslateUi(MainWindow)
        self.frame_rate_spinBox.valueChanged['int'].connect(self.frame_rate_slider.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.frame_rate_spinBox.setValue)
        #self.frame_rate_spinBox.valueChanged['int'].connect(self.test)
        self.hue_slider.valueChanged['int'].connect(self.hue_spinBox.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.hue_slider.setValue)
        self.saturation_slider.valueChanged['int'].connect(self.saturation_spinBox.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.saturation_slider.setValue)
        self.brightness_slider.valueChanged['int'].connect(self.brightness_spinBox.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.brightness_slider.setValue)
        self.apply_changes_button.toggled['bool'].connect(self.video.clear)
        self.open_button.clicked.connect(self.loadVideo)
        self.export_button.toggled['bool'].connect(self.video.clear)
        self.triangulation_check_box.toggled['bool'].connect(self.apply_changes_button.setChecked)
        self.playback_slider.valueChanged['int'].connect(self.video.setNum)
        self.pause_button.clicked.connect(self.stopVideo)
        self.play_button.clicked.connect(self.playVideo)
        self.stop_button.clicked.connect(self.stopVideo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delaunay\'s Dream"))
        MainWindow.setStatusTip(_translate("MainWindow", "Delaunay\'s Dream"))
        self.video.setStatusTip(_translate("MainWindow", "filename.mp4"))
        self.playback_slider.setStatusTip(_translate("MainWindow", "0:00"))
        self.pause_button.setStatusTip(_translate("MainWindow", "Pause"))
        self.pause_button.setText(_translate("MainWindow", "Pause"))
        self.play_button.setStatusTip(_translate("MainWindow", "Play"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.stop_button.setStatusTip(_translate("MainWindow", "Stop"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.triangulation_check_box.setStatusTip(_translate("MainWindow", "Triangulate Filter"))
        self.triangulation_check_box.setText(_translate("MainWindow", "Delaunay Triangulation "))
        self.frame_rate_label.setText(_translate("MainWindow", "Frame Rate"))
        self.frame_rate_slider.setStatusTip(_translate("MainWindow", "Adjust Frame Rate"))
        self.frame_rate_spinBox.setStatusTip(_translate("MainWindow", "Adjust Frame Rate"))
        self.hue_Label.setText(_translate("MainWindow", "Hue"))
        self.hue_slider.setStatusTip(_translate("MainWindow", "Adjust Hue"))
        self.hue_spinBox.setStatusTip(_translate("MainWindow", "Adjust Hue"))
        self.saturation_label.setText(_translate("MainWindow", "Saturation"))
        self.saturation_slider.setStatusTip(_translate("MainWindow", "Adjust Saturation"))
        self.saturation_spinBox.setStatusTip(_translate("MainWindow", "Adjust Saturation"))
        self.brightness_label.setText(_translate("MainWindow", "Brightness"))
        self.brightness_slider.setStatusTip(_translate("MainWindow", "Adjust Brightness"))
        self.brightness_spinBox.setStatusTip(_translate("MainWindow", "Adjust Brightness"))
        self.apply_changes_button.setStatusTip(_translate("MainWindow", "Apply Changes"))
        self.apply_changes_button.setText(_translate("MainWindow", "Apply Changes"))
        self.open_button.setStatusTip(_translate("MainWindow", "Open File"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.export_button.setStatusTip(_translate("MainWindow", "Save As..."))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))

        self.filename = None # Will hold the image address location
        self.stop = False
    
    # def test(self, testing):
    #     print(testing)

    def playVideo(self):
        self.stop = False
        
        if self.filename != None:
            vid = cv2.VideoCapture(self.filename)
            fps = vid.get(cv2.CAP_PROP_FPS)
            print(fps)
            while(vid.isOpened()):
                ret, frame = vid.read()
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    to_qt = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
                    pic = to_qt.scaled(854, 480, Qt.KeepAspectRatio)
                    self.video.setPixmap(QtGui.QPixmap.fromImage(pic))
                cv2.waitKey(25)    #25 = time of each frame in ms
                if self.stop == True:
                    self.video.setPixmap(QtGui.QPixmap(".\\image.jpg"))
                    break

            vid.release()

    def stopVideo(self):
        self.stop = True
    
    def loadVideo(self):
        self.filename = QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
