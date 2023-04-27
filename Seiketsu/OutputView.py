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

        font = QFont()
        font.setFamily("Inter Regular")
        font.setPointSize(9)
        
        self.vert = QVBoxLayout(self)
        self.vert.setContentsMargins(0, 0, 0, 0)
        self.vert.setSpacing(0)
        
        self.table = QTextEdit(self)
        self.table.setStyleSheet("padding: 20px;color: #ffffff;")
        self.table.setMinimumSize(800, 500)
        self.table.setFont(font)
        # self.table.verticalScrollBar().setStyleSheet("""
        # QScrollBar:vertical {
        #     border-color: #abacae;
        #     border-width: 1px;
        #     border-style: solid;
        #     background-color: #fafafa;
        #     width: 20px;
        #     margin: 21px 0 21px 0;
        # }
        # QScrollBar::handle:vertical {
        #     background-color: #000000;
        #     min-height: 25px;
        # }
        # QScrollBar::add-line:vertical {
        #     border: 3px solid #abacae;
        #     background-color: #abacae;
        #     height: 25px;
        #     subcontrol-position: bottom;
        #     subcontrol-origin: margin;
        #     border-radius: 5px;
        # }
        # QScrollBar::sub-line:vertical {
        #     border: 3px solid #abacae;
        #     background-color: #abacae;
        #     height: 25px;
        #     subcontrol-position: top;
        #     subcontrol-origin: margin;
        #     border-radius: 5px;
        # }""")
        
        font.setPointSize(10)

        self.current_file = QLabel(self, text="")
        self.current_file.setWordWrap(True)
        self.current_file.setFont(font)
        self.current_file.setStyleSheet("background:none;color: #ffffff;qproperty-alignment: AlignCenter;")
        
        self.progressbar = QProgressBar(self)
        # self.progressbar.setTextVisible(False)
        self.progressbar.setStyleSheet("""
            QProgressBar {
                color: #ffffff;
                text-align:center;
            }
            
            QProgressBar:chunk {
                border-radius: 5px;
                background-color: #a56de2;
            }
        """)
        self.progressbar.setFont(font)
        self.progressbar.setMaximum(100)
        
        self.vert.addWidget(self.table, stretch=90)
        self.vert.addWidget(self.current_file, stretch=5)
        self.vert.addWidget(self.progressbar, stretch=5)
        
    def style(self):
        return """
        #outputview {
			background-color: #333333;
			margin: 10px;
			margin-top: 0px;
            padding: 50px;
		}
        """
        