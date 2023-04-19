from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HomePage(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName(u"homepage")
        self.setStyleSheet("#homepage {\n"
"    background-color: #fafafa;\n"
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
"    color: rgb(0, 0, 0);\n"
"}")
        
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        
        self.subtitle = QLabel(self, text = '"Streamline your files with Seiketsu - The organized way to productivity."')
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setStyleSheet("#subtitle {\n"
"   background: none;\n"
"   color: rgb(0, 0, 0);\n"
"}")

        self.button_box = QLabel(self)
        self.button_box.setObjectName("button_box")
        self.button_box.setStyleSheet("#button_box {\n"
"   background: none;\n"
"   color: rgb(0, 0, 0);\n"
"}")
        
        self.content_layout.addWidget(self.logo, stretch=20, alignment= Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.content_layout.addWidget(self.app_label, stretch=15, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.subtitle, stretch=5, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.button_box, 60)