from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.Titlebar import TitleBar
from Seiketsu.HomePage import HomePage
from Seiketsu.OutputView import OutputView
from Custom_Widgets.Widgets import QCustomStackedWidget
import Seiketsu.Settings

GLOBAL_STATE = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1024, 768)
        
        setting = Seiketsu.Settings.init()
        
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
        
        self.title_bar = TitleBar(self.drop_shadow_frame, has_settings=True, has_minimize=True, has_maximize=True)
        
        self.stackedWidget = QCustomStackedWidget(self.drop_shadow_frame)
        self.stackedWidget.setTransitionDirection(Qt.Horizontal)
        self.stackedWidget.setTransitionSpeed(250)
        self.stackedWidget.setTransitionEasingCurve(QEasingCurve.Linear)
        self.stackedWidget.setSlideTransition(True)
        
        self.home_page = HomePage(self.stackedWidget, self)
        self.outputview = OutputView(self.stackedWidget)
        
        self.stackedWidget.addWidget(self.home_page)
        self.stackedWidget.addWidget(self.outputview)
        
        self.verticalLayout.addWidget(self.title_bar)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.setCentralWidget(self.centralwidget)
        
        self.title_bar.btn_maximize.clicked.connect(lambda: self.maximize_restore())
        self.title_bar.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.title_bar.btn_close.clicked.connect(lambda: self.close())
        self.title_bar.mouseMoveEvent = self.moveWindow
        self.title_bar.mouseDoubleClickEvent = self.doubleClickMaximization
        self.title_bar.icon.clicked.connect(self.return_to_homepage)
    
    def return_to_homepage(self):
        if self.stackedWidget.currentIndex() == 1:
            pixmap = QPixmap(".\\resource\\icon.svg")
            font = self.title_bar.label_title.font()
            font.setPointSize(14)

            self.stackedWidget.slideToPreviousWidget()
            self.title_bar.icon.setIcon(QIcon(pixmap))
            self.title_bar.icon.setIconSize(QSize(48, 48))
            self.title_bar.icon.setStyleSheet("")
            self.title_bar.label_title.setText("Seiketsu")
            self.title_bar.label_title.setFont(font)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def doubleClickMaximization(self, event):
        if event.buttons() == Qt.LeftButton:
            self.maximize_restore()

    def moveWindow(self, event):
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
                self.title_bar.btn_maximize.setToolTip("Restore")
        else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.resize(self.width()+1, self.height()+1)
                self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
                self.title_bar.btn_maximize.setToolTip("Maximize")