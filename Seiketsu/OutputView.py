from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.CustomScrollableTable import CustomScrollableTable

class OutputView(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("outputview")
        self.setStyleSheet(self.style())
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.vert = QVBoxLayout(self)
        self.vert.setContentsMargins(0, 0, 0, 0)
        self.vert.setSpacing(0)
        self.table = CustomScrollableTable(self)
        self.table.setHeaders(["Source", "Method", "Output"])
        self.table.setSizeDistribution([45,10,45])
        self.table.setMinimumSize(800, 500)
        
        for r in range(60):
            self.table.append([f"From {r}", f"Using {r}", f"To {r}"])
        
        self.vert.addWidget(self.table, stretch=1)
        
    def style(self):
        return """
        #outputview {
			background-color: #333333;
			margin: 10px;
			margin-top: 0px;
            padding: 50px;
		}
        """
        