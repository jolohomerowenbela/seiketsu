from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.InspirationPane import *
from Seiketsu.CustomizerWindow import *

class HomePage(QFrame):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.window = main
        self.setObjectName(u"homepage")
        self.setStyleSheet(self.style())
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        
        self.content_layout = QVBoxLayout(self)
        
        self.logo = QLabel(self)
        pixmap = QPixmap(".\\resource\\logo.svg")
        self.logo.setPixmap(pixmap.scaled(QSize(128, 128), Qt.AspectRatioMode.KeepAspectRatio))
        self.logo.setObjectName("logo")
        
        font = QFont()
        font.setFamily("Inter ExtraBold")
        font.setPointSize(52)

        self.app_label = QLabel(self, text= "seiketsu")
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        
        self.subtitle = QLabel(self, text = '"Streamline your files with Seiketsu - The organized way to productivity."')
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")

        self.button_box = QWidget(self)
        self.button_box.setStyleSheet("background: none;")
        
        font.setPointSize(12)

        self.start_button = QToolButton(self.button_box, text="Start Organization")
        self.start_button.setIcon(QIcon(".\\resource\start-1.svg"))
        self.start_button.setIconSize(QSize(150, 150))
        self.start_button.setFont(font)
        self.start_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.start_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.start_button.setMinimumSize(QSize(250, 250))
        self.start_button.setObjectName("start_button")
        self.start_button.setStyleSheet("""
        #start_button {
        color: #43d6b5;
        background: rgba(67, 214, 181, 20);
        padding-top: 20px;
        border: 3px solid #43d6b5;
        }
        #start_button:hover {
        color: #43d6b5;
        background: rgba(67, 214, 181, 50%);
        padding-top: 20px;
        border: 3px solid #43d6b5;
        }""")
        
        self.customize_window = CustomizerWindow(self)
        
        self.customize_button = QToolButton(self.button_box, text="Customize Directories")
        self.customize_button.setIcon(QIcon(".\\resource\customize-1.svg"))
        self.customize_button.setIconSize(QSize(150, 150))
        self.customize_button.setFont(font)
        self.customize_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.customize_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.customize_button.setMinimumSize(QSize(250, 250))
        self.customize_button.setObjectName("customize_button")
        self.customize_button.setStyleSheet("""
        #customize_button {
        color: #9bdb4d;
        background: rgba(155, 219, 77, 20);
        padding-top: 20px;
        border: 3px solid #9bdb4d;
        }
        #customize_button:hover {
        color: #9bdb4d;
        background: rgba(155, 219, 77, 50%);
        padding-top: 20px;
        border: 3px solid #9bdb4d;
        }""")
        self.customize_button.clicked.connect(lambda: self.customize_window.show())

        self.button_box_layout = QHBoxLayout(self.button_box)
        self.button_box_layout.setSpacing(50)
        self.button_box_layout.addWidget(self.start_button, stretch=20, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        self.button_box_layout.addWidget(self.customize_button, stretch=20, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.inspiration_label = InspirationPane(self)
        
        font.setPointSize(10)

        self.show_output_button = QPushButton(self, text="Show Output")
        self.show_output_button.setObjectName("ShowOutputButton")
        self.show_output_button.setFont(font)
        self.show_output_button.setMinimumSize(QSize(200, 40))
        self.show_output_button.setStyleSheet("""
        #ShowOutputButton {
            background-color: rgba(100, 185, 255, 20);
            color: #ffffff;
            border: 2px solid #64baff;
        }
        #ShowOutputButton:hover {
            background-color: rgba(100, 185, 255, 50%);
            color: #ffffff;
            border: 2px solid #64baff;
        }""")
        
        self.content_layout.addWidget(self.logo, stretch=20, alignment= Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(self.app_label, stretch=15, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.subtitle, stretch=5, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.button_box, stretch=35)
        self.content_layout.addWidget(self.inspiration_label, stretch=5)
        self.content_layout.addWidget(self.show_output_button, stretch=15, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        self.start_button.clicked.connect(self.show_outputview)
        self.show_output_button.clicked.connect(self.show_outputview)
    
    def show_outputview(self):
        pixmap = QPixmap(".\\resource\\return.svg")
        font = self.window.title_bar.font()
        font.setPointSize(11)
        
        self.window.stackedWidget.slideToNextWidget()
        self.window.title_bar.icon.setIcon(QIcon(pixmap))
        self.window.title_bar.icon.setIconSize(QSize(24, 24))
        self.window.title_bar.label_title.setText("Return to Home Page")
        self.window.title_bar.label_title.setFont(font)
        self.window.title_bar.icon.setStyleSheet("""
        QPushButton {
            border: 2px solid #9bdb4d;
            margin-top: 5px;
            margin-bottom: 5px;
            background-color: rgba(155, 219, 77, 20);
        }
        QPushButton:hover {
            border: 2px solid #9bdb4d;
            margin-top: 5px;
            margin-bottom: 5px;
            background-color: rgba(155, 219, 77, 50%);
        }""")
    
    def style(self):
        return """
		#homepage {
			background-color: #333333;
			margin: 10px;
			margin-top: 0px;
		}

        #logo {
            background: none;
        }
        
        #app_label {
            background: none;
            color: rgb(255, 255, 255);
        }
        
        #subtitle {
            background: none;
            color: rgb(255, 255, 255);
        }
        
        #start_button {
            color: #43d6b5;
            background: rgba(67, 214, 181, 20);
            padding-top: 20px;
            border: 3px solid #43d6b5;
        }
        
        #customize_button {
            color: #9bdb4d;
            background: rgba(155, 219, 77, 20);
            padding-top: 20px;
            border: 3px solid #9bdb4d;
        }
        
        #ShowOutputButton {
            background-color: #64baff;
            color: #ffffff;
        }
    	"""