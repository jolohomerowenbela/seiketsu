from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Seiketsu.Titlebar
import Seiketsu.Settings
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
        
        self.table = CustomScrollableTable(self.content, has_checkbox=True)
        self.table.gridLayout.setSpacing(0)
        self.table.setFixedHeight(420)
        self.table.setHeaders(["Folders"])
        
        self.folderpaths = list(Seiketsu.Settings.getScannableFolders())
        for folder in self.folderpaths:
            self.table.append([folder])
            
        font = QFont()
        font.setFamily("Inter Regular")
        font.setPointSize(10)
        
        self.add_button = QPushButton(parent=self.content, text="Add Folder")
        self.add_button.setFixedHeight(50)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("""
        QPushButton {
            color: #ffffff;
            background: rgba(249, 196, 64, 20);
            border: 3px solid #f9c440;
        }
        QPushButton:hover {
            color: #ffffff;
            background: rgba(249, 196, 64, 50%);
            border: 3px solid #f9c440;
        }""")
        self.add_button.clicked.connect(self.add_to_folders)
        
        self.remove_button = QPushButton(parent=self.content, text="Remove Folder")
        self.remove_button.setFixedHeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setStyleSheet("""
        QPushButton {
            color: #ffffff;
            background: rgba(243, 115, 41, 20);
            border: 3px solid #f37329;
        }
        QPushButton:hover {
            color: #ffffff;
            background: rgba(243, 115, 41, 50%);
            border: 3px solid #f37329;
        }""")
        self.remove_button.clicked.connect(self.remove_selected)
        
        self.buttons = QWidget(self.content)
        
        self.buttons_layout = QHBoxLayout(self.buttons)
        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.remove_button)
        
        self.content_layout.addWidget(self.table)
        self.content_layout.addWidget(self.buttons)   
        
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
        
    def remove_selected(self):
        if self.table.selectedBoxes is not None and len(self.table.selectedBoxes) > 0:
            for row in self.table.selectedBoxes:
                self.folderpaths.remove(self.table.gridLayout.itemAtPosition(row, 0).widget().text())
                self.table.selectedBoxes.remove(row)
                for col in range(self.table.gridLayout.columnCount()):
                    self.table.gridLayout.itemAtPosition(row, col).widget().setParent(None)
                Seiketsu.Settings.setScannableFolders(self.folderpaths)
    
    def add_to_folders(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath not in self.folderpaths:
            self.folderpaths.append(folderpath)
            self.table.append([folderpath])
            Seiketsu.Settings.setScannableFolders(self.folderpaths)
        else:
            print("Already here")