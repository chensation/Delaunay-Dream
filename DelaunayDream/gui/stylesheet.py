class StyleSheet:

    def __init__(self):
        self.dark_mode = """
        #MainWindow {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 black, stop:1 #212121);
        }

        #video_player {
            background-color: black;
            border: 1px solid #4d4d4d;
        }

        QStatusBar {
            background-color: black;
            color: white;
        }

        QPushButton {
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #135680, stop:1 #4AB9AF);
            border: 1px solid #4d4d4d;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #4AB9AF;
        }

        QPushButton:pressed {
            background-color: #135680;
        }

        #play_button, #stop_button {
            border-radius: 20;
            border: 0px;
        }

        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px solid #4d4d4d;
            height: 10px;
            margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
            border-radius: 7px;
        }

        QSlider::add-page:qlineargradient {
            background: black;
            border-radius: 2px;
        }

        QSlider::sub-page:qlineargradient {
            background: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #135680, stop:1 #4AB9AF);
            border-radius: 2px;
        }

        QSpinBox { 
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #135680, stop:1 #4AB9AF);
            color: black; 
            border-radius: 3px;
        }

        QLabel { 
            color: white; 
        }

        QCheckBox {
            background-color: white;
            border: 0px solid #4d4d4d;
        }

        QRadioButton {
            color: white;
        }

        QRadioButton::indicator {
            border-radius: 7px;
        }

        QRadioButton::indicator:checked {
            background-color: #135680;
            border: 3px solid white;
        }

        QRadioButton::indicator:unchecked {
            background-color: white;
        }

        QDialog {
            background-color: #212121;
            border: 1px solid #4D4D4D;
            color: white;
        }

        QGroupBox {
            border: 1px solid #4d4d4d;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 black, stop:1 #212121);
            border-radius: 10;
            color: white;
            font-size: 10px;
        }

        QPushButton:disabled {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px solid #4d4d4d;
            color: #4d4d4d;
            border-radius: 5px;
        }

        QSlider::sub-page:disabled {
            background-color: #4D4D4D;
            border-radius: 2px;
        }

        QSpinBox:disabled { 
            background-color: #212121;
            border-radius: 3px;
            color: black;
        }

        QLabel:disabled { 
            color: #4d4d4d; 
        }

        QCheckBox:disabled {
            background-color: #4d4d4d;
        }

        QRadioButton:disabled {
            color: #4d4d4d;
        }

        QRadioButton::indicator:checked:disabled {
            background-color: black;
            border: 4px solid #4d4d4d;
        }

        QRadioButton::indicator:unchecked:disabled {
            background-color: #4d4d4d;
            border: 0px;
        }

        QComboBox:disabled {
            background-color: #4d4d4d;
            color: black;
        }
        """
        self.light_mode = """
        #MainWindow {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 white);
        }

        #video_player {
            background-color: white;
            border: 1px solid #DEDEDE;
        }

        QStatusBar {
            background-color: #e0e0e0;
            color: black;
        }

        QPushButton {
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #973680, stop:1 #EBCAB5);
            border: 1px solid #dedede;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #E2BDAF;
        }

        QPushButton:pressed {
            background-color: #973680;
        }

        #play_button, #stop_button {
            border-radius: 20;
            border: 0px;
        }

        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px solid #DEDEDE;
            height: 10px;
            margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
            border-radius: 7px;
        }

        QSlider::add-page:qlineargradient {
            background: white;
            border-radius: 2px;
        }

        QSlider::sub-page:qlineargradient {
            background: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #973680, stop:1 #E2BDAF);
            border-radius: 2px;
        }

        QSpinBox { 
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #973680, stop:1 #E2BDAF);
            color: white; 
            border-radius: 3px;
        }
        
        QLabel { 
            color: black; 
        }

        QCheckBox {
            background-color: #dedede;
            color: black;
        }

        QRadioButton {
            color: black;
        }

        QRadioButton::indicator:checked {
            background-color: #973680;
            border: 3px solid #EBCAB5;
        }

        QRadioButton::indicator:unchecked {
            background-color: #dedede;
        }

        QDialog {
            background-color: #e0e0e0;
            border: 1px solid white;
            color: black;
        }

        QGroupBox {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #EBEBEB, stop:1 white);
            border: 1px solid #dedede;
            border-radius: 10;
            color: black;
            font-size: 10px;
        }
        """