from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Seiketsu.Titlebar
from Seiketsu.CustomScrollableTable import *

class CustomizerWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.resize(800, 600)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        # Layout for the window
        self.drop_shadow_layout = QVBoxLayout(self)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)

        self.drop_shadow_frame = QFrame(self)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4d4d4d, stop:0.521368 #666666);\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_frame.setFixedSize(self.width() - 20, self.height() - 20)
        self.drop_shadow_frame.setGraphicsEffect(self.shadow)

        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        
        self.title_bar = Seiketsu.Titlebar.TitleBar(self.drop_shadow_frame, has_settings=False, has_minimize=False, has_maximize=False, label="Folders to scan")
        
        font = QFont()
        font.setFamily("Inter ExtraBold")
        font.setPointSize(22)
        
        self.content = QWidget(self.drop_shadow_frame)
        self.content.setStyleSheet("background-color: #333333;margin-left: 10px;margin-bottom: 10px;margin-right: 10px;")
        self.content_layout = QVBoxLayout(self.content)
        
        self.table = CustomScrollableTable(self.content)
        self.table.gridLayout.setSpacing(0)
        self.table.setHeaders(["Folders"])
        
        for r in range(30):
            self.table.append([f"Folder named {r}"])

        self.content_layout.addWidget(self.table)        
        
        font.setPointSize(11)
        font.setFamily("Inter Medium")

        self.verticalLayout.addWidget(self.title_bar)
        self.verticalLayout.addWidget(self.content)

        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.title_bar.button_box.setAlignment(self.title_bar.btn_close, Qt.AlignmentFlag.AlignRight)
        
        self.title_bar.mouseMoveEvent = self.moveWindow
        
        self.title_bar.btn_close.clicked.connect(lambda: self.close())
    
    def moveWindow(self, event):
        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()