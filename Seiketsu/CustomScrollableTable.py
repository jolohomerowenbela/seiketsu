from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CustomScrollableTable(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background:none;background-color:#666666;")
        self.layout = QHBoxLayout(self)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setStyleSheet("background:none;background-color:#666666;")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        self.font = QFont()
        self.font.setFamily("Inter Regular")
        self.font.setPointSize(10)
        
        self.scrollArea.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            border-color: #abacae;
            border-width: 1px;
            border-style: solid;
            background-color: #fafafa;
            width: 20px;
            margin: 21px 0 21px 0;
        }
        QScrollBar::handle:vertical {
            background-color: #abacae;
            min-height: 25px;
        }
        QScrollBar::add-line:vertical {
            border: 3px solid #abacae;
            background-color: #abacae;
            height: 25px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
            border-radius: 5px;
        }
        QScrollBar::sub-line:vertical {
            border: 3px solid #abacae;
            background-color: #abacae;
            height: 25px;
            subcontrol-position: top;
            subcontrol-origin: margin;
            border-radius: 5px;
        }""")
    
    def setHeaders(self, headers: list[str]):
        font = QFont()
        font.setFamily("Inter SemiBold")
        font.setPointSize(12)
        
        for index,header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("color: #ffffff;background: none;")
            label.setFont(font)
            self.gridLayout.addWidget(label, 0, index, alignment=Qt.AlignmentFlag.AlignHCenter)
    
    def append(self, row: list[str]):
        current_index = self.gridLayout.rowCount()
        
        if len(row) > self.gridLayout.columnCount():
            print("Adding more than what have headers!")
        else:
            for index,column in enumerate(row):
                label = QLabel(column)
                label.setFont(self.font)
                label.setStyleSheet("color: #ffffff;background:none;background-color: #333333;border-radius: 2px;padding: 5px;qproperty-alignment: AlignCenter;")
                label.setFixedHeight(40)
                self.gridLayout.addWidget(label, current_index, index)
    
    def setSizeDistribution(self, sizes: list[int]):
        if len(sizes) > self.gridLayout.columnCount():
            print("More sizes than necessary")
        else:
            for index,size in enumerate(sizes):
                self.gridLayout.setColumnStretch(index, size)