from PyQt5 import QtWidgets, QtCore
from DelaunayDream.gui.warning import Ui_Dialog_Warning 

class WarningDialogue(Ui_Dialog_Warning, QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cancel_changes = True
        self.setupUi(self)

    def closeEvent(self, event):
        self.cancel_changes = False