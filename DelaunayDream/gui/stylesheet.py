class StyleSheet:

    def __init__(self):
        self.dark_mode = """
        #MainWindow {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 black, stop:1 #212121);
        }

        #video_player {
            background-color: black;
            border: 1px solid #4D4D4D;
        }

        #warning_label {
            color: red;
        }

        QToolTip {
            background-color: #212121;
            border: 1px solid #4D4D4D;
            color: #FFB38D;
        }

        QTextBrowser {
            background: transparent;
            color: #FFB38D;
            border: 1px solid; 
            border-radius: 5px;
        }

        QScrollBar {
            background: transparent;
            height: 8px;
            margin: 0;
        }

        QScrollBar::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px;
            border-radius: 4px;
        }

        QScrollBar::add-line:horizontal {
            height: 0px;
        }

        QScrollBar::sub-line:horizontal {
            height: 0px;
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            height: 0px;
        }
        
        QStatusBar {
            background-color: black;
            color: #FFB38D;
        }

        QPushButton {
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #135680, stop:1 #4AB9AF);
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
            border-radius: 7px;
        }

        QSlider::add-page {
            background: #212121;
            border-radius: 2px;
        }

        #thickness_slider::add-page, #video_slider::add-page {
            background: black;
        }

        QSlider::sub-page {
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
            color: #FFB38D;
            font-size: 10px;
        }

        QPushButton:disabled {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            color: #4d4d4d;
            border-radius: 5px;
        }

        QSlider::sub-page:disabled {
            background-color: #4D4D4D;
            border-radius: 2px;
        }

        QSlider::handle:horizontal:disabled {
            background: #4d4d4d;
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
            background-color: #212121;
            color: black;
        }
        """
        self.light_mode = """
        #MainWindow {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #EBCAB5, stop:1 white);
        }

        #video_player {
            background-color: white;
            border: 1px solid #DEDEDE;
        }

        #warning_label {
            color: red;
        }

        QToolTip {
            background: #EBCAB5;
            border: 1px solid white;
            color: black;
        }

        QTextBrowser {
            background-color: transparent;
            color: black;
            border: 1px solid #e0e0e0; 
            border-radius: 5px;
        }

        QScrollBar {
            background: transparent;
            height: 8px;
            margin: 0;
        }

        QScrollBar::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px;
            border-radius: 4px;
        }

        QScrollBar::add-line:horizontal {
            height: 0px;
        }

        QScrollBar::sub-line:horizontal {
            height: 0px;
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            height: 0px;
        }

        QStatusBar {
            background-color: #E0E0E0;
            color: black;
        }

        QPushButton {
            background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 #973680, stop:1 #EBCAB5);
            border-radius: 5px;
            color: white;
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
            border-radius: 7px;
        }

        QSlider::add-page {
            background: white;
            border-radius: 2px;
        }

        #thickness_slider::add-page, #video_slider::add-page {
            background: #e0e0e0;
        }

        QSlider::sub-page {
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

        QRadioButton::indicator {
            border-radius: 7px;
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

        QPushButton:disabled {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            color: #dedede;
            border-radius: 5px;
        }

        QSlider::sub-page:disabled {
            background-color: #e0e0e0;
            border-radius: 2px;
        }

        QSlider::handle:horizontal:disabled {
            background: #e0e0e0;
        }

        QSpinBox:disabled { 
            background-color: white;
            border-radius: 3px;
            color: #dedede;
        }

        QLabel:disabled { 
            color: #b4b4b4;
        }

        QCheckBox:disabled {
            background-color: white;
            color: #e0e0e0;
        }

        QRadioButton:disabled {
            color: #dedede;
        }

        QRadioButton::indicator:checked:disabled {
            background-color: white;
            border: 4px solid #dedede;
        }

        QRadioButton::indicator:unchecked:disabled {
            background-color: #dedede;
            border: 0px;
        }

        QComboBox:disabled {
            background-color: white;
            color:  #dedede;
        }
        """