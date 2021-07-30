# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 679)
        MainWindow.setMinimumSize(QtCore.QSize(1257, 651))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setMinimumSize(QtCore.QSize(0, 25))
        self.open_button.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 0, 0, 1, 1)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setEnabled(False)
        self.export_button.setMinimumSize(QtCore.QSize(0, 25))
        self.export_button.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.gridLayout.addWidget(self.export_button, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.video_player = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_player.sizePolicy().hasHeightForWidth())
        self.video_player.setSizePolicy(sizePolicy)
        self.video_player.setMinimumSize(QtCore.QSize(854, 480))
        self.video_player.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.video_player.setStyleSheet("")
        self.video_player.setText("")
        self.video_player.setAlignment(QtCore.Qt.AlignCenter)
        self.video_player.setObjectName("video_player")
        self.verticalLayout_6.addWidget(self.video_player)
        self.video_slider = QtWidgets.QSlider(self.centralwidget)
        self.video_slider.setEnabled(False)
        self.video_slider.setMinimumSize(QtCore.QSize(854, 20))
        self.video_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.video_slider.setOrientation(QtCore.Qt.Horizontal)
        self.video_slider.setObjectName("video_slider")
        self.verticalLayout_6.addWidget(self.video_slider)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setEnabled(False)
        self.play_button.setMinimumSize(QtCore.QSize(40, 40))
        self.play_button.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.play_button.setFont(font)
        self.play_button.setText("")
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_13.addWidget(self.play_button)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setEnabled(False)
        self.stop_button.setMinimumSize(QtCore.QSize(40, 40))
        self.stop_button.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stop_button.setFont(font)
        self.stop_button.setText("")
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_13.addWidget(self.stop_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.mode_toggle = AnimatedToggle(self.centralwidget)
        self.mode_toggle.setMinimumSize(QtCore.QSize(58, 45))
        self.mode_toggle.setMaximumSize(QtCore.QSize(58, 45))
        self.mode_toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_toggle.setText("")
        self.mode_toggle.setObjectName("mode_toggle")
        self.horizontalLayout_18.addWidget(self.mode_toggle)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 5, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setEnabled(False)
        self.apply_button.setMinimumSize(QtCore.QSize(0, 25))
        self.apply_button.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.apply_button.setFont(font)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_14.addWidget(self.apply_button)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setEnabled(False)
        self.reset_button.setMinimumSize(QtCore.QSize(0, 25))
        self.reset_button.setMaximumSize(QtCore.QSize(62, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_14.addWidget(self.reset_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(17, 450, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 2, 1, 1)
        self.status_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.status_message.setMinimumSize(QtCore.QSize(300, 35))
        self.status_message.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_message.setFont(font)
        self.status_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_message.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.status_message.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status_message.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.status_message.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.status_message.setLineWrapColumnOrWidth(0)
        self.status_message.setObjectName("status_message")
        self.gridLayout_2.addWidget(self.status_message, 2, 3, 1, 1)
        self.all_options = QtWidgets.QGroupBox(self.centralwidget)
        self.all_options.setEnabled(True)
        self.all_options.setMinimumSize(QtCore.QSize(300, 0))
        self.all_options.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.all_options.setFont(font)
        self.all_options.setToolTip("")
        self.all_options.setAlignment(QtCore.Qt.AlignCenter)
        self.all_options.setObjectName("all_options")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.all_options)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hue_Label = QtWidgets.QLabel(self.all_options)
        self.hue_Label.setMinimumSize(QtCore.QSize(95, 15))
        self.hue_Label.setMaximumSize(QtCore.QSize(95, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.hue_Label.setFont(font)
        self.hue_Label.setObjectName("hue_Label")
        self.horizontalLayout_2.addWidget(self.hue_Label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hue_slider = QtWidgets.QSlider(self.all_options)
        self.hue_slider.setMinimumSize(QtCore.QSize(225, 20))
        self.hue_slider.setMaximumSize(QtCore.QSize(225, 20))
        self.hue_slider.setMaximum(179)
        self.hue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_slider.setObjectName("hue_slider")
        self.horizontalLayout.addWidget(self.hue_slider)
        self.hue_spinBox = QtWidgets.QSpinBox(self.all_options)
        self.hue_spinBox.setMinimumSize(QtCore.QSize(33, 20))
        self.hue_spinBox.setMaximumSize(QtCore.QSize(33, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.hue_spinBox.setFont(font)
        self.hue_spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hue_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hue_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.hue_spinBox.setMinimum(0)
        self.hue_spinBox.setMaximum(179)
        self.hue_spinBox.setProperty("value", 0)
        self.hue_spinBox.setObjectName("hue_spinBox")
        self.horizontalLayout.addWidget(self.hue_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saturation_label = QtWidgets.QLabel(self.all_options)
        self.saturation_label.setMinimumSize(QtCore.QSize(95, 15))
        self.saturation_label.setMaximumSize(QtCore.QSize(95, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.saturation_label.setFont(font)
        self.saturation_label.setObjectName("saturation_label")
        self.horizontalLayout_4.addWidget(self.saturation_label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saturation_slider = QtWidgets.QSlider(self.all_options)
        self.saturation_slider.setMinimumSize(QtCore.QSize(225, 20))
        self.saturation_slider.setMaximumSize(QtCore.QSize(225, 20))
        self.saturation_slider.setMaximum(200)
        self.saturation_slider.setSingleStep(1)
        self.saturation_slider.setPageStep(10)
        self.saturation_slider.setProperty("value", 100)
        self.saturation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_slider.setObjectName("saturation_slider")
        self.horizontalLayout_3.addWidget(self.saturation_slider)
        self.saturation_spinBox = QtWidgets.QSpinBox(self.all_options)
        self.saturation_spinBox.setMinimumSize(QtCore.QSize(33, 20))
        self.saturation_spinBox.setMaximumSize(QtCore.QSize(33, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.saturation_spinBox.setFont(font)
        self.saturation_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.saturation_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.saturation_spinBox.setMaximum(200)
        self.saturation_spinBox.setProperty("value", 100)
        self.saturation_spinBox.setObjectName("saturation_spinBox")
        self.horizontalLayout_3.addWidget(self.saturation_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.brightness_label = QtWidgets.QLabel(self.all_options)
        self.brightness_label.setMinimumSize(QtCore.QSize(95, 15))
        self.brightness_label.setMaximumSize(QtCore.QSize(95, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.brightness_label.setFont(font)
        self.brightness_label.setObjectName("brightness_label")
        self.horizontalLayout_6.addWidget(self.brightness_label)
        spacerItem11 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.brightness_slider = QtWidgets.QSlider(self.all_options)
        self.brightness_slider.setMinimumSize(QtCore.QSize(225, 20))
        self.brightness_slider.setMaximumSize(QtCore.QSize(225, 20))
        self.brightness_slider.setMaximum(150)
        self.brightness_slider.setProperty("value", 100)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.horizontalLayout_5.addWidget(self.brightness_slider)
        self.brightness_spinBox = QtWidgets.QSpinBox(self.all_options)
        self.brightness_spinBox.setMinimumSize(QtCore.QSize(33, 20))
        self.brightness_spinBox.setMaximumSize(QtCore.QSize(33, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.brightness_spinBox.setFont(font)
        self.brightness_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.brightness_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.brightness_spinBox.setMaximum(150)
        self.brightness_spinBox.setProperty("value", 100)
        self.brightness_spinBox.setObjectName("brightness_spinBox")
        self.horizontalLayout_5.addWidget(self.brightness_spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem13 = QtWidgets.QSpacerItem(8, 35, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.triangulate_label = QtWidgets.QLabel(self.all_options)
        self.triangulate_label.setMinimumSize(QtCore.QSize(115, 35))
        self.triangulate_label.setMaximumSize(QtCore.QSize(115, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.triangulate_label.setFont(font)
        self.triangulate_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.triangulate_label.setObjectName("triangulate_label")
        self.horizontalLayout_12.addWidget(self.triangulate_label)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.triangulation_check_box = Toggle(self.all_options)
        self.triangulation_check_box.setEnabled(True)
        self.triangulation_check_box.setMinimumSize(QtCore.QSize(48, 35))
        self.triangulation_check_box.setMaximumSize(QtCore.QSize(48, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.triangulation_check_box.setFont(font)
        self.triangulation_check_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.triangulation_check_box.setAutoFillBackground(True)
        self.triangulation_check_box.setText("")
        self.triangulation_check_box.setChecked(False)
        self.triangulation_check_box.setObjectName("triangulation_check_box")
        self.horizontalLayout_12.addWidget(self.triangulation_check_box)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        spacerItem15 = QtWidgets.QSpacerItem(37, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem15)
        self.groupBox = QtWidgets.QGroupBox(self.all_options)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(280, 240))
        self.groupBox.setMaximumSize(QtCore.QSize(280, 240))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.triangulate_options = QtWidgets.QWidget(self.groupBox)
        self.triangulate_options.setEnabled(False)
        self.triangulate_options.setGeometry(QtCore.QRect(10, 20, 260, 220))
        self.triangulate_options.setMinimumSize(QtCore.QSize(260, 220))
        self.triangulate_options.setMaximumSize(QtCore.QSize(260, 220))
        self.triangulate_options.setObjectName("triangulate_options")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.triangulate_options)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.max_points_label = QtWidgets.QLabel(self.triangulate_options)
        self.max_points_label.setMinimumSize(QtCore.QSize(95, 20))
        self.max_points_label.setMaximumSize(QtCore.QSize(95, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.max_points_label.setFont(font)
        self.max_points_label.setObjectName("max_points_label")
        self.horizontalLayout_7.addWidget(self.max_points_label)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.max_points_spinBox = QtWidgets.QSpinBox(self.triangulate_options)
        self.max_points_spinBox.setMinimumSize(QtCore.QSize(40, 20))
        self.max_points_spinBox.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.max_points_spinBox.setFont(font)
        self.max_points_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.max_points_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.max_points_spinBox.setMinimum(20)
        self.max_points_spinBox.setMaximum(10000)
        self.max_points_spinBox.setProperty("value", 2000)
        self.max_points_spinBox.setObjectName("max_points_spinBox")
        self.horizontalLayout_7.addWidget(self.max_points_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem17 = QtWidgets.QSpacerItem(240, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.method_label = QtWidgets.QLabel(self.triangulate_options)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.method_label.setFont(font)
        self.method_label.setObjectName("method_label")
        self.horizontalLayout_8.addWidget(self.method_label)
        self.threshold_radioButton = QtWidgets.QRadioButton(self.triangulate_options)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.threshold_radioButton.setFont(font)
        self.threshold_radioButton.setChecked(True)
        self.threshold_radioButton.setObjectName("threshold_radioButton")
        self.horizontalLayout_8.addWidget(self.threshold_radioButton)
        self.poisson_disk_radioButton = QtWidgets.QRadioButton(self.triangulate_options)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.poisson_disk_radioButton.setFont(font)
        self.poisson_disk_radioButton.setObjectName("poisson_disk_radioButton")
        self.horizontalLayout_8.addWidget(self.poisson_disk_radioButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem18 = QtWidgets.QSpacerItem(240, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem18)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scale_factor_label = QtWidgets.QLabel(self.triangulate_options)
        self.scale_factor_label.setMinimumSize(QtCore.QSize(100, 20))
        self.scale_factor_label.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.scale_factor_label.setFont(font)
        self.scale_factor_label.setObjectName("scale_factor_label")
        self.horizontalLayout_9.addWidget(self.scale_factor_label)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.scale_factor_comboBox = QtWidgets.QComboBox(self.triangulate_options)
        self.scale_factor_comboBox.setMinimumSize(QtCore.QSize(55, 18))
        self.scale_factor_comboBox.setMaximumSize(QtCore.QSize(55, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.scale_factor_comboBox.setFont(font)
        self.scale_factor_comboBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.scale_factor_comboBox.setObjectName("scale_factor_comboBox")
        self.scale_factor_comboBox.addItem("")
        self.scale_factor_comboBox.addItem("")
        self.scale_factor_comboBox.addItem("")
        self.scale_factor_comboBox.addItem("")
        self.scale_factor_comboBox.addItem("")
        self.horizontalLayout_9.addWidget(self.scale_factor_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem20 = QtWidgets.QSpacerItem(240, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem20)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.draw_line_checkBox = QtWidgets.QCheckBox(self.triangulate_options)
        self.draw_line_checkBox.setMinimumSize(QtCore.QSize(14, 14))
        self.draw_line_checkBox.setMaximumSize(QtCore.QSize(14, 14))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.draw_line_checkBox.setFont(font)
        self.draw_line_checkBox.setText("")
        self.draw_line_checkBox.setIconSize(QtCore.QSize(18, 18))
        self.draw_line_checkBox.setObjectName("draw_line_checkBox")
        self.horizontalLayout_10.addWidget(self.draw_line_checkBox)
        self.label = QtWidgets.QLabel(self.triangulate_options)
        self.label.setMinimumSize(QtCore.QSize(70, 20))
        self.label.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem21)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        spacerItem22 = QtWidgets.QSpacerItem(37, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem22)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.thickness_label = QtWidgets.QLabel(self.triangulate_options)
        self.thickness_label.setEnabled(False)
        self.thickness_label.setMinimumSize(QtCore.QSize(70, 20))
        self.thickness_label.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.thickness_label.setFont(font)
        self.thickness_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.thickness_label.setObjectName("thickness_label")
        self.horizontalLayout_11.addWidget(self.thickness_label)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem23)
        self.thickness_slider = QtWidgets.QSlider(self.triangulate_options)
        self.thickness_slider.setEnabled(False)
        self.thickness_slider.setMinimumSize(QtCore.QSize(130, 20))
        self.thickness_slider.setMaximumSize(QtCore.QSize(130, 20))
        self.thickness_slider.setMinimum(1)
        self.thickness_slider.setMaximum(5)
        self.thickness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.thickness_slider.setObjectName("thickness_slider")
        self.horizontalLayout_11.addWidget(self.thickness_slider)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem24)
        self.thickness_spinBox = QtWidgets.QSpinBox(self.triangulate_options)
        self.thickness_spinBox.setEnabled(False)
        self.thickness_spinBox.setMinimumSize(QtCore.QSize(20, 20))
        self.thickness_spinBox.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.thickness_spinBox.setFont(font)
        self.thickness_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.thickness_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.thickness_spinBox.setMinimum(1)
        self.thickness_spinBox.setMaximum(5)
        self.thickness_spinBox.setObjectName("thickness_spinBox")
        self.horizontalLayout_11.addWidget(self.thickness_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.gridLayout_2.addWidget(self.all_options, 0, 3, 2, 1)
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
        self.scale_factor_comboBox.setCurrentIndex(1)
        self.hue_slider.valueChanged['int'].connect(self.hue_spinBox.setValue)
        self.saturation_slider.valueChanged['int'].connect(self.saturation_spinBox.setValue)
        self.brightness_slider.valueChanged['int'].connect(self.brightness_spinBox.setValue)
        self.draw_line_checkBox.toggled['bool'].connect(self.thickness_slider.setEnabled)
        self.draw_line_checkBox.toggled['bool'].connect(self.thickness_spinBox.setEnabled)
        self.thickness_slider.valueChanged['int'].connect(self.thickness_spinBox.setValue)
        self.triangulation_check_box.toggled['bool'].connect(self.triangulate_options.setEnabled)
        self.draw_line_checkBox.toggled['bool'].connect(self.thickness_label.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delaunay\'s Dream"))
        MainWindow.setStatusTip(_translate("MainWindow", "Delaunay\'s Dream"))
        self.open_button.setToolTip(_translate("MainWindow", "New Project"))
        self.open_button.setStatusTip(_translate("MainWindow", "New Project"))
        self.open_button.setText(_translate("MainWindow", "New"))
        self.export_button.setToolTip(_translate("MainWindow", "Export Video"))
        self.export_button.setStatusTip(_translate("MainWindow", "Export Video"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.video_player.setStatusTip(_translate("MainWindow", "Video Playback"))
        self.video_slider.setToolTip(_translate("MainWindow", "Video Seek Bar"))
        self.video_slider.setStatusTip(_translate("MainWindow", "Video Seek Bar"))
        self.play_button.setToolTip(_translate("MainWindow", "Play/Pause Video"))
        self.play_button.setStatusTip(_translate("MainWindow", "Play/Pause Video"))
        self.stop_button.setToolTip(_translate("MainWindow", "Stop Video"))
        self.stop_button.setStatusTip(_translate("MainWindow", "Stop Video"))
        self.mode_toggle.setToolTip(_translate("MainWindow", "Dark/Light Mode Toggle"))
        self.mode_toggle.setStatusTip(_translate("MainWindow", "Dark/Light Mode Toggle"))
        self.apply_button.setToolTip(_translate("MainWindow", "Apply Changes to All Frames"))
        self.apply_button.setStatusTip(_translate("MainWindow", "Apply Changes to All Frames"))
        self.apply_button.setText(_translate("MainWindow", "Apply to All Frames"))
        self.reset_button.setToolTip(_translate("MainWindow", "Reset all changes applied to the video by reloading the video"))
        self.reset_button.setStatusTip(_translate("MainWindow", "Reset all changes applied to the video by reloading the video"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.status_message.setToolTip(_translate("MainWindow", "Status Messages"))
        self.status_message.setStatusTip(_translate("MainWindow", "Status Messages"))
        self.status_message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to Delaunay\'s Dream!</p></body></html>"))
        self.all_options.setTitle(_translate("MainWindow", "Options"))
        self.hue_Label.setStatusTip(_translate("MainWindow", "Hue"))
        self.hue_Label.setText(_translate("MainWindow", "  Hue"))
        self.hue_slider.setToolTip(_translate("MainWindow", "Adjust Hue (0 - 179)"))
        self.hue_slider.setStatusTip(_translate("MainWindow", "Adjust Hue (0 - 179)"))
        self.hue_spinBox.setToolTip(_translate("MainWindow", "Adjust Hue (0 - 179)"))
        self.hue_spinBox.setStatusTip(_translate("MainWindow", "Adjust Hue (0 - 179)"))
        self.saturation_label.setStatusTip(_translate("MainWindow", "Saturation"))
        self.saturation_label.setText(_translate("MainWindow", "  Saturation"))
        self.saturation_slider.setToolTip(_translate("MainWindow", "Adjust Saturation (0 - 200)"))
        self.saturation_slider.setStatusTip(_translate("MainWindow", "Adjust Saturation (0 - 200)"))
        self.saturation_spinBox.setToolTip(_translate("MainWindow", "Adjust Saturation (0 - 200)"))
        self.saturation_spinBox.setStatusTip(_translate("MainWindow", "Adjust Saturation (0 - 200)"))
        self.brightness_label.setStatusTip(_translate("MainWindow", "Brightness"))
        self.brightness_label.setText(_translate("MainWindow", "  Brightness"))
        self.brightness_slider.setToolTip(_translate("MainWindow", "Adjust Brightness (0 - 150)"))
        self.brightness_slider.setStatusTip(_translate("MainWindow", "Adjust Brightness (0 - 150)"))
        self.brightness_spinBox.setToolTip(_translate("MainWindow", "Adjust Brightness (0 - 150)"))
        self.brightness_spinBox.setStatusTip(_translate("MainWindow", "Adjust Brightness (0 - 150)"))
        self.triangulate_label.setStatusTip(_translate("MainWindow", "Triangulate Video"))
        self.triangulate_label.setText(_translate("MainWindow", "Triangulate Video"))
        self.triangulation_check_box.setToolTip(_translate("MainWindow", "Triangulate Video"))
        self.triangulation_check_box.setStatusTip(_translate("MainWindow", "Triangulate Video"))
        self.groupBox.setStatusTip(_translate("MainWindow", "Triangulate Options"))
        self.groupBox.setTitle(_translate("MainWindow", "Triangulate Options"))
        self.max_points_label.setStatusTip(_translate("MainWindow", "Max Points"))
        self.max_points_label.setText(_translate("MainWindow", "Max Points"))
        self.max_points_spinBox.setToolTip(_translate("MainWindow", "Adjust number of points used to triangulate (20 - 10000)"))
        self.max_points_spinBox.setStatusTip(_translate("MainWindow", "Adjust number of points used to triangulate (20 - 10000)"))
        self.method_label.setStatusTip(_translate("MainWindow", "Sampling Method"))
        self.method_label.setText(_translate("MainWindow", "Method:"))
        self.threshold_radioButton.setToolTip(_translate("MainWindow", "Threshold Sampling Method (quick, but with mediocre results)"))
        self.threshold_radioButton.setStatusTip(_translate("MainWindow", "Threshold Sampling Method (quick, but with mediocre results)"))
        self.threshold_radioButton.setText(_translate("MainWindow", "Threshold"))
        self.poisson_disk_radioButton.setToolTip(_translate("MainWindow", "Poisson Disk Sampling Method (slow, but with great results)"))
        self.poisson_disk_radioButton.setStatusTip(_translate("MainWindow", "Poisson Disk Sampling Method (slow, but with great results)"))
        self.poisson_disk_radioButton.setText(_translate("MainWindow", "Poisson Disk"))
        self.scale_factor_label.setStatusTip(_translate("MainWindow", "Scale Factor"))
        self.scale_factor_label.setText(_translate("MainWindow", "Scale Factor"))
        self.scale_factor_comboBox.setToolTip(_translate("MainWindow", "Scale Factor determines how accurate the colors of the triangulated images are (higher is slower)"))
        self.scale_factor_comboBox.setStatusTip(_translate("MainWindow", "Scale Factor determines how accurate the colors of the triangulated images are (higher is slower)"))
        self.scale_factor_comboBox.setCurrentText(_translate("MainWindow", "10%"))
        self.scale_factor_comboBox.setItemText(0, _translate("MainWindow", "5%"))
        self.scale_factor_comboBox.setItemText(1, _translate("MainWindow", "10%"))
        self.scale_factor_comboBox.setItemText(2, _translate("MainWindow", "20%"))
        self.scale_factor_comboBox.setItemText(3, _translate("MainWindow", "50%"))
        self.scale_factor_comboBox.setItemText(4, _translate("MainWindow", "100%"))
        self.draw_line_checkBox.setToolTip(_translate("MainWindow", "Draw Line"))
        self.draw_line_checkBox.setStatusTip(_translate("MainWindow", "Draw Line"))
        self.label.setText(_translate("MainWindow", "Draw Line"))
        self.thickness_label.setStatusTip(_translate("MainWindow", "Thickness"))
        self.thickness_label.setText(_translate("MainWindow", "Thickness"))
        self.thickness_slider.setToolTip(_translate("MainWindow", "Adjust Line Thickness (1 - 5)"))
        self.thickness_slider.setStatusTip(_translate("MainWindow", "Adjust Line Thickness (1 - 5)"))
        self.thickness_spinBox.setToolTip(_translate("MainWindow", "Adjust Line Thickness (1 - 5)"))
        self.thickness_spinBox.setStatusTip(_translate("MainWindow", "Adjust Line Thickness (1 - 5)"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
from qtwidgets import AnimatedToggle, Toggle
