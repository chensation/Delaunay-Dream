class StyleSheet:

    def __init__(self):
        self.dark_mode = """
        #MainWindow {
            background-color: black;
        }

        #video_player {
            border: 1px solid white;
        }

        #frame_viewer {
            border: 1px solid white;
        }

        QLabel { 
            color: white; 
        }

        QCheckBox {
            background-color: black;
            color: white;
        }

        QRadioButton {
            color: white;
        }
    
        QDialog {
            background: black;
            color: white;
        }

        QGroupBox {
            border: 1px solid white;
            color: white;
            font-size: 12px;
        }

        """
        self.light_mode = """
        #MainWindow {
            background-color: white;
        }

        #video_player {
            border: 1px solid black;
        }

        #frame_viewer {
            border: 1px solid black;
        }

        QLabel { 
            color: black; 
        }

        QCheckBox {
            background-color: white;
            color: black;
        }

        QDialog {
            background: white;
            color: black;
        }

        QGroupBox {
            border: 1px solid black;
            color: black;
            font-size: 12px;
        }
        """