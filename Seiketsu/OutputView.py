from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class OutputView(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("outputview")
        self.setStyleSheet(self.style())
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.vert = QVBoxLayout(self)
        self.label = QLabel(self, text="belyaev")
        self.vert.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
    def style(self):
        return """
        #outputview {
			background-color: #333333;
			margin: 10px;
			margin-top: 0px;
		}
        """
        