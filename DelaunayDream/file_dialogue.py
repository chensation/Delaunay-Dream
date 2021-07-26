from PyQt5 import QtWidgets
from DelaunayDream.gui.dialog import Ui_Dialog 

class FileDialogue(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, video, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._video = video
        self._filename = ""

        self.browse_button.clicked.connect(self.set_filename)
        
        self.file_lineEdit.textChanged[str].connect(self.file_text_changed)
        self.file_lineEdit.editingFinished.connect(self.confirm_file)

        self.frame_rate_selector.currentTextChanged['QString'].connect(self.set_frame_rate)
        self.ok_button.clicked.connect(self.close)
        self.cancel_button.clicked.connect(self.close)

    def set_filename(self):
        self.warning_msg.setText('')
        self._filename = QtWidgets.QFileDialog.getOpenFileName(filter="Video files(*.*)")[0]
        self.file_lineEdit.setText(self._filename)
        self.confirm_file()

    def file_text_changed(self, text):
        self.warning_msg.setText('')
        self._filename = text

    def confirm_file(self):
        try:
            self._video.filename = self._filename
            original_fps = self._video.get_fps_from_file()

            self.frame_rate_selector.clear()
            options = [str(int(original_fps/i)) for i in range(1, 4)]
            self.frame_rate_selector.addItems(options)
            self.ok_button.setEnabled(True)

        except Exception as err:
            self.warning_msg.setText(str(err))

    def set_frame_rate(self, fps):

        if fps:
            self._video.framerate = int(fps)
