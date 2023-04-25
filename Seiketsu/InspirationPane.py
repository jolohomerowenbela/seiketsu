from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class InspirationPane(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setStyleSheet(self.style())
        
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        
        self.label = QLabel(self, text="\"You're braver than you believe, and stronger than you seem, and smarter than you think.\"")
        self.label.setFont(font)
        self.label.setObjectName("inspirational")
        
        self.simpleLayout = QVBoxLayout(self)
        self.simpleLayout.addWidget(self.label)
        
    def style(self):
        return """
        #inspirational {
            background:none;
            color: #ffffff;
            border: 2px solid #666666;
            padding-top: 10px;
            padding-bottom: 10px;
            qproperty-alignment: AlignCenter;
        }
        """