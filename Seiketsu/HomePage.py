from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.InspirationPane import *

class HomePage(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName(u"homepage")
        self.setStyleSheet("#homepage {\n"
"    background-color: #333333;\n"
"    margin: 10px;\n"
"    margin-top: 0px;\n"
"}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        
        self.content_layout = QVBoxLayout(self)
        
        self.logo = QLabel(self)
        pixmap = QPixmap(".\\resource\\logo.svg")
        self.logo.setPixmap(pixmap.scaled(QSize(128, 128), Qt.AspectRatioMode.KeepAspectRatio))
        self.logo.setObjectName("logo")
        self.logo.setStyleSheet("background: none;")
        
        font = QFont()
        font.setFamily("Inter ExtraBold")
        font.setPointSize(52)

        self.app_label = QLabel(self, text= "seiketsu")
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        self.app_label.setStyleSheet("#app_label {\n"
"    background: none;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        
        self.subtitle = QLabel(self, text = '"Streamline your files with Seiketsu - The organized way to productivity."')
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setStyleSheet("#subtitle {\n"
"   background: none;\n"
"   color: rgb(255, 255, 255);\n"
"}")

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
        self.start_button.setStyleSheet("color: #43d6b5; background: rgba(67, 214, 181, 20);padding-top: 20px;border: 3px solid #43d6b5;")
        # "color: #43d6b5; background: none;padding-top: 20px;border: 3px solid #43d6b5;"
        
        self.customize_button = QToolButton(self.button_box, text="Customize Directories")
        self.customize_button.setIcon(QIcon(".\\resource\customize-1.svg"))
        self.customize_button.setIconSize(QSize(150, 150))
        self.customize_button.setFont(font)
        self.customize_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.customize_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.customize_button.setMinimumSize(QSize(250, 250))
        self.customize_button.setStyleSheet("color: #9bdb4d; background: rgba(155, 219, 77, 20);padding-top: 20px;border: 3px solid #9bdb4d;")

        self.button_box_layout = QHBoxLayout(self.button_box)
        self.button_box_layout.setSpacing(50)
        self.button_box_layout.addWidget(self.start_button, stretch=20, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        self.button_box_layout.addWidget(self.customize_button, stretch=20, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.inspiration_label = QLabel(self, text="\"You're braver than you believe, and stronger than you seem, and smarter than you think.\"")
        self.inspiration_label.setFont(font)
        self.inspiration_label.setStyleSheet("background:none;color: #ffffff")
        
        font.setPointSize(10)

        self.show_output_button = QPushButton(self, text="Show Output")
        self.show_output_button.setObjectName("ShowOutputButton")
        self.show_output_button.setFont(font)
        self.show_output_button.setStyleSheet("background-color: #64baff;color: #ffffff")
        self.show_output_button.setMinimumSize(QSize(200, 40))
        
        self.content_layout.addWidget(self.logo, stretch=20, alignment= Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.content_layout.addWidget(self.app_label, stretch=15, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.subtitle, stretch=5, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.button_box, stretch=35)
        self.content_layout.addWidget(self.inspiration_label, stretch=5, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.content_layout.addWidget(self.show_output_button, stretch=15, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)