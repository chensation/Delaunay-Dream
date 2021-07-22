from PyQt5 import QtWidgets
from DelaunayDream.gui.warning import Ui_Dialog_Warning 

class WarningDialogue(Ui_Dialog_Warning, QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
