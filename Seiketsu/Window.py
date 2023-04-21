from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.TitleBar import TitleBar
from Seiketsu.HomePage import HomePage

GLOBAL_STATE = 0

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1024, 768)
        
        # Window drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        self.centralwidget = QWidget(self)
        
        # Layout for the window
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)

        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4d4d4d, stop:0.521368 #666666);\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_frame.setGraphicsEffect(self.shadow)
        
        # Main Layout for the widgets
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        
        self.title_bar = TitleBar(self.drop_shadow_frame)
        
        self.home_page = HomePage(self.drop_shadow_frame)
        
        self.verticalLayout.addWidget(self.title_bar)
        self.verticalLayout.addWidget(self.home_page)

        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.setCentralWidget(self.centralwidget)
        
        self.title_bar.btn_maximize.clicked.connect(lambda: self.maximize_restore())
        self.title_bar.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.title_bar.btn_close.clicked.connect(lambda: self.close())
        self.title_bar.mouseMoveEvent = self.moveWindow
        self.title_bar.mouseDoubleClickEvent = self.doubleClickMaximization

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def doubleClickMaximization(self, event):
        if event.buttons() == Qt.LeftButton:
            self.maximize_restore()
        
            

    def moveWindow(self, event):
        #     # RESTORE BEFORE MOVE
        #     if UIFunctions.returnStatus() == 1:
        #         UIFunctions.maximize_restore(self)

        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
                self.showMaximized()

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1

                # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
                self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
                # self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
                self.title_bar.btn_maximize.setToolTip("Restore")
        else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.resize(self.width()+1, self.height()+1)
                self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
                # self.drop_shadow_frame.setStyleSheet("backgroundW-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
                self.title_bar.btn_maximize.setToolTip("Maximize")