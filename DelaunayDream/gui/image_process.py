# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("film.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sample_700.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.triangulation_check_box = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.triangulation_check_box.setFont(font)
        self.triangulation_check_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.triangulation_check_box.setAutoFillBackground(True)
        self.triangulation_check_box.setObjectName("triangulation_check_box")
        self.verticalLayout.addWidget(self.triangulation_check_box, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_rate_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.frame_rate_label.setFont(font)
        self.frame_rate_label.setObjectName("frame_rate_label")
        self.verticalLayout.addWidget(self.frame_rate_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_rate_slider = QtWidgets.QSlider(self.centralwidget)
        self.frame_rate_slider.setOrientation(QtCore.Qt.Horizontal)
        self.frame_rate_slider.setObjectName("frame_rate_slider")
        self.horizontalLayout.addWidget(self.frame_rate_slider)
        self.frame_rate_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.frame_rate_spinBox.setFont(font)
        self.frame_rate_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_rate_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.frame_rate_spinBox.setMaximum(99)
        self.frame_rate_spinBox.setObjectName("frame_rate_spinBox")
        self.horizontalLayout.addWidget(self.frame_rate_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hue_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.hue_Label.setFont(font)
        self.hue_Label.setObjectName("hue_Label")
        self.verticalLayout.addWidget(self.hue_Label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hue_slider = QtWidgets.QSlider(self.centralwidget)
        self.hue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_slider.setObjectName("hue_slider")
        self.horizontalLayout_2.addWidget(self.hue_slider)
        self.hue_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.hue_spinBox.setFont(font)
        self.hue_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hue_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.hue_spinBox.setMaximum(99)
        self.hue_spinBox.setObjectName("hue_spinBox")
        self.horizontalLayout_2.addWidget(self.hue_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.saturation_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.saturation_label.setFont(font)
        self.saturation_label.setObjectName("saturation_label")
        self.verticalLayout.addWidget(self.saturation_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saturation_slider = QtWidgets.QSlider(self.centralwidget)
        self.saturation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_slider.setObjectName("saturation_slider")
        self.horizontalLayout_3.addWidget(self.saturation_slider)
        self.saturation_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.saturation_spinBox.setFont(font)
        self.saturation_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.saturation_spinBox.setMaximum(99)
        self.saturation_spinBox.setObjectName("saturation_spinBox")
        self.horizontalLayout_3.addWidget(self.saturation_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.brightness_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.brightness_label.setFont(font)
        self.brightness_label.setObjectName("brightness_label")
        self.verticalLayout.addWidget(self.brightness_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.brightness_slider = QtWidgets.QSlider(self.centralwidget)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.horizontalLayout_4.addWidget(self.brightness_slider)
        self.brightness_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.brightness_spinBox.setFont(font)
        self.brightness_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.brightness_spinBox.setMaximum(99)
        self.brightness_spinBox.setObjectName("brightness_spinBox")
        self.horizontalLayout_4.addWidget(self.brightness_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_5.addWidget(self.open_button)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout_5.addWidget(self.export_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        self.hue_slider.valueChanged['int'].connect(self.hue_spinBox.setValue)
        self.saturation_spinBox.valueChanged['int'].connect(self.saturation_slider.setValue)
        self.brightness_slider.valueChanged['int'].connect(self.brightness_spinBox.setValue)
        self.saturation_slider.valueChanged['int'].connect(self.saturation_spinBox.setValue)
        self.brightness_spinBox.valueChanged['int'].connect(self.brightness_slider.setValue)
        self.hue_spinBox.valueChanged['int'].connect(self.hue_slider.setValue)
        self.frame_rate_spinBox.valueChanged['int'].connect(self.frame_rate_slider.setValue)
        self.frame_rate_slider.valueChanged['int'].connect(self.frame_rate_spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delaunay\'s Dream"))
        MainWindow.setStatusTip(_translate("MainWindow", "Delaunay\'s Dream"))
        self.triangulation_check_box.setText(_translate("MainWindow", "Delauney\'s Triangulation"))
        self.frame_rate_label.setText(_translate("MainWindow", "Blurriness"))
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
        self.open_button.setStatusTip(_translate("MainWindow", "Open File"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.export_button.setStatusTip(_translate("MainWindow", "Save As..."))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
