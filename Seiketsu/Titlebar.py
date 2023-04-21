from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TitleBar(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMaximumHeight(50)
        self.setStyleSheet(self.style())
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("titlebar")
        
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        font = QFont()
        font.setFamily("Inter Condensed Light")
        font.setPointSize(14)

        self.frame_title = QFrame(self)
        self.frame_title.setMinimumHeight(50)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title.setObjectName("frame_title")

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        
        pixmap = QPixmap(".\\resource\\icon.svg")
        
        self.icon = QLabel(self.frame_title)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setPixmap(pixmap.scaled(QSize(48, 48), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon.setObjectName("icon")
        
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_2.addWidget(self.icon)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(95)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setText("Seiketsu")

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(14)

        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        self.horizontalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self)
        self.frame_btns.setMaximumWidth(100)
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setFixedSize(QSize(16, 16))
        self.btn_minimize.setObjectName("minimize_button")

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setObjectName("maximize_button")

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setObjectName("close_button")
        
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)

    def style(self):
        return """
        #titlebar {
                background: none;
        }
        
        #minimize_button {
                border: none;
                border-radius: 8px;
                background-color: rgb(249, 196, 64);
        }
        
        #minimize_button:hover {
                background-color: rgba(249, 196, 64, 150);
        }
        
        #maximize_button {
                border: none;
                border-radius: 8px;
                background-color: rgb(104, 183, 35);
        }

        #maximize_button:hover {
                background-color: rgba(104, 183, 35, 150);
        }
        
        #close_button {
                border: none;
                border-radius: 8px;
                background-color: rgb(198, 38, 46);
        }

        #close_button:hover {
                background-color: rgba(198, 38, 46, 150);
        }
        
        #frame_btns {
                background: none;
        }
        
        #frame_title {
                background: none;
        }
        
        #icon {
                background: none;
        }
        
        #label_title {
                background: none;
                color: rgb(250, 250, 250);
        }
        """