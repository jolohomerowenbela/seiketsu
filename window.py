from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from foldersTree import FoldersTree
from organizeFiles import OrganizeFiles
from ButtonEffect import ButtonEffect

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        style = """
            QToolButton {
                border-radius: 30px;
                background-color: #D1D8EC;
                padding-top: 20px;
                padding-bottom: 10px;
                margin-bottom: 30px;
            }
            
            QToolButton:pressed {
                border-radius: 30px;
                background-color: #b2b8c9;
                padding-top: 20px;
                padding-bottom: 10px;
                margin-bottom: 30px;
            }
            
            QMainWindow {
                background-color: #D1D8EC;
            }

            QPushButton {
                border-radius: 15px;
                background-color: #D1D8EC;
            }
            
            QListView {
                background: #F0F8FF;
                border-radius: 15px;
                border-width: 3px;
                border-color: #121212;
            }
        """
        
        self.goButton = QToolButton(self, text = "Organize Files", icon = QIcon("resource/start.png"))
        self.goButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.goButton.setMinimumHeight(180)
        self.goButton.setMinimumWidth(180)
        self.goButton.setIconSize(QSize(100, 100))
        self.goButton.clicked.connect(self.organizedClicked)
        self.goButton.setGraphicsEffect(ButtonEffect(self, radius=75))
        
        self.customButton = QToolButton(self, text = "Customize Directories", icon = QIcon("resource/customize.png"))
        self.customButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.customButton.setMinimumHeight(180)
        self.customButton.setMinimumWidth(180)
        self.customButton.setIconSize(QSize(100, 100))
        self.customButton.clicked.connect(self.clicked)
        self.customButton.setGraphicsEffect(ButtonEffect(self, radius=75))

        font = QFont()
        font.setPointSize(12)
        self.goButton.setFont(font)
        self.customButton.setFont(font)
        
        label = QLabel(self, text = "<font size=20><b>Welcome to Seiri</b>")
        label.setFixedHeight(50)
        label.setTextFormat(Qt.TextFormat.RichText)
        
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(50, 20, 50, 20)
        self.gridLayout.addWidget(label, 0, 0, 1, 2, alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout.addWidget(self.goButton, 1, 0)
        self.gridLayout.addWidget(self.customButton, 1, 1)
        
        self.chooser = FoldersTree(self)
        self.chooser.setFixedHeight(0)
        self.chooser.setContentsMargins(10, 15, 10, 15)
        self.gridLayout.addWidget(self.chooser, 2, 0, 1, 2)

        self.setWindowIcon(QIcon("resource/logo.png"))
        self.setWindowTitle("Seiri")

        self.setFixedSize(640, 480)
        self.setStyleSheet(style)
        self.closedState = True
        self.maxhgt = 215

        minimizeButton = QPushButton(icon = QIcon("resource/minimize.png"))
        minimizeButton.setFixedSize(QSize(30, 30))
        minimizeButton.clicked.connect(lambda:self.showMinimized())
        minimizeButton.setGraphicsEffect(ButtonEffect(self, radius=30))
        
        closeButton = QPushButton(icon = QIcon("resource/close.png"))
        closeButton.setFixedSize(QSize(30, 30))
        closeButton.clicked.connect(lambda:self.close())
        closeButton.setGraphicsEffect(ButtonEffect(self, radius=30))

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(minimizeButton, alignment = Qt.AlignmentFlag.AlignRight)
        titleLayout.addWidget(closeButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(titleLayout)
        mainLayout.addLayout(self.gridLayout)
        mainLayout.setAlignment(titleLayout, Qt.AlignmentFlag.AlignTop)
        mainLayout.setContentsMargins(10, 10, 10, 50)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setCentralWidget(container)
    
    def organizedClicked(self):
        self.organizeFiles = OrganizeFiles(self.chooser)
        self.organizeFiles.start()

    def clicked(self):
        anim = QVariantAnimation(self)
        anim.setDuration(250)
        if not self.closedState:
            anim.setStartValue(self.maxhgt)
            anim.setEndValue(0)
            self.closedState = True
        else:
            self.chooser.updateButtons()
            anim.setStartValue(0)
            anim.setEndValue(self.maxhgt)
            self.closedState = False
        anim.valueChanged.connect(self.animateHide)
        anim.start()
        
    
    def animateHide(self, val):
        h = int(val)
        self.chooser.setFixedHeight(h)
        