# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/warning.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Warning(object):
    def setupUi(self, Dialog_Warning):
        Dialog_Warning.setObjectName("Dialog_Warning")
        Dialog_Warning.resize(430, 130)
        Dialog_Warning.setMinimumSize(QtCore.QSize(430, 130))
        Dialog_Warning.setMaximumSize(QtCore.QSize(430, 130))
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog_Warning)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.warning_label = QtWidgets.QLabel(Dialog_Warning)
        self.warning_label.setMinimumSize(QtCore.QSize(0, 20))
        self.warning_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.warning_label.setFont(font)
        self.warning_label.setObjectName("warning_label")
        self.gridLayout_2.addWidget(self.warning_label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.warning_message = QtWidgets.QLabel(Dialog_Warning)
        self.warning_message.setMinimumSize(QtCore.QSize(0, 30))
        self.warning_message.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.warning_message.setFont(font)
        self.warning_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.warning_message.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_message.setObjectName("warning_message")
        self.horizontalLayout.addWidget(self.warning_message)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        self.ok_warning_button = QtWidgets.QPushButton(Dialog_Warning)
        self.ok_warning_button.setMinimumSize(QtCore.QSize(75, 20))
        self.ok_warning_button.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ok_warning_button.setFont(font)
        self.ok_warning_button.setObjectName("ok_warning_button")
        self.gridLayout.addWidget(self.ok_warning_button, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog_Warning)
        self.ok_warning_button.clicked.connect(Dialog_Warning.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Warning)

    def retranslateUi(self, Dialog_Warning):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Warning.setWindowTitle(_translate("Dialog_Warning", "Dialog"))
        self.warning_label.setText(_translate("Dialog_Warning", "Warning!"))
        self.warning_message.setText(_translate("Dialog_Warning", "[Message Goes Here]"))
        self.ok_warning_button.setText(_translate("Dialog_Warning", "OK"))
