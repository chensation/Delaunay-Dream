# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 160)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(60, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.file_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.file_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(230, 20))
        self.file_lineEdit.setObjectName("file_lineEdit")
        self.horizontalLayout.addWidget(self.file_lineEdit)
        self.browse_button = QtWidgets.QPushButton(Dialog)
        self.browse_button.setMinimumSize(QtCore.QSize(80, 20))
        self.browse_button.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout.addWidget(self.browse_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.warning_msg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.warning_msg.setFont(font)
        self.warning_msg.setText("")
        self.warning_msg.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.warning_msg.setObjectName("warning_msg")
        self.verticalLayout.addWidget(self.warning_msg)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(141, 20))
        self.label_2.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.frame_rate_selector = QtWidgets.QComboBox(Dialog)
        self.frame_rate_selector.setMinimumSize(QtCore.QSize(80, 20))
        self.frame_rate_selector.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame_rate_selector.setFont(font)
        self.frame_rate_selector.setCurrentText("")
        self.frame_rate_selector.setFrame(True)
        self.frame_rate_selector.setObjectName("frame_rate_selector")
        self.horizontalLayout_2.addWidget(self.frame_rate_selector)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_3.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_3.addWidget(self.cancel_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select a File"))
        self.label.setText(_translate("Dialog", "Filename:"))
        self.browse_button.setText(_translate("Dialog", "Browse..."))
        self.label_2.setText(_translate("Dialog", "Select a Frame Rate:"))
        self.ok_button.setText(_translate("Dialog", "Ok"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
