from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Seiketsu.Titlebar

class SettingPopup(QDialog):
    def __init__(self, parent, clicker_button):
        super().__init__(parent)
        self.parent = parent
        self.clicker = clicker_button
        self.resize(800, 480)
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
        
        self.title_bar = Seiketsu.Titlebar.TitleBar(self.drop_shadow_frame, has_settings=False, has_minimize=False, has_maximize=False)
        
        font = QFont()
        font.setFamily("Inter ExtraBold")
        font.setPointSize(22)
        
        self.content = QWidget(self.drop_shadow_frame)
        self.content.setStyleSheet("background-color: #333333;margin-left: 10px;margin-bottom: 10px;margin-right: 10px;")
        self.content_layout = QGridLayout(self.content)
        
        self.icon = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\logo.svg")
        self.icon.setPixmap(pixmap.scaled(QSize(84, 84), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon.setStyleSheet("background: none;")

        self.title = QLabel(self.content, text="Seiketsu Settings", )
        self.title.setStyleSheet("background: none;color: #ffffff;")
        self.title.setFont(font)
        
        font.setPointSize(11)
        font.setFamily("Inter Medium")
        
        self.icon_auto = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\customize.svg")
        self.icon_auto.setPixmap(pixmap.scaled(QSize(84, 84), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon_auto.setStyleSheet("background: none;")
        
        self.setting_auto = SettingWidget(self.content, "Automatic Organization", "Set Automatic Organization.", "Organize files every:")
        self.setting_auto.add_combo_item("1 hour")
        
        self.icon_func = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\customize.svg")
        self.icon_func.setPixmap(pixmap.scaled(QSize(84, 84), Qt.AspectRatioMode.KeepAspectRatio))
        
        self.setting_func = SettingWidget(self.content, "Functionality", "Rename obscure filenames.", "Organize files by:")
        self.setting_func.add_combo_item("Document Analysis")
        
        self.icon_add = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\customize.svg")
        self.icon_add.setPixmap(pixmap.scaled(QSize(84, 84), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon_add.setStyleSheet("background: none;")
        
        self.setting_add = SettingWidget(self.content, "Additional Settings", "Disable quotes on homepage.", "")
        
        self.setting_title_layout = QHBoxLayout()
        self.setting_title_layout.addWidget(self.icon, stretch=33, alignment=Qt.AlignmentFlag.AlignRight)
        self.setting_title_layout.addWidget(self.title, stretch=67)
        
        self.content_layout.setHorizontalSpacing(0)
        self.content_layout.addLayout(self.setting_title_layout, 0, 0, 1, 5)
        self.content_layout.addWidget(self.icon_auto, 1, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.content_layout.addWidget(self.setting_auto, 1, 1, 1, 4, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addWidget(self.icon_func, 2, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.content_layout.addWidget(self.setting_func, 2, 1, 1, 4, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addWidget(self.icon_add, 3, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.content_layout.addWidget(self.setting_add, 3, 1, 1, 4, alignment=Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.title_bar)
        self.verticalLayout.addWidget(self.content)

        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.title_bar.btn_close.clicked.connect(self.close_setting)
        self.title_bar.button_box.setAlignment(self.title_bar.btn_close, Qt.AlignmentFlag.AlignRight)
        
        self.title_bar.mouseMoveEvent = self.moveWindow

    def close_setting(self):
        self.parent.show_settings()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        
class SettingWidget(QWidget):
    def __init__(self, parent, setting_title: str, checkbox_title: str, combobox_label: str):
        super().__init__(parent)
        
        self.grid_layout = QGridLayout(self)
        
        font = QFont()
        font.setPointSize(11)
        font.setFamily("Inter Medium")
        
        self.title = QLabel(self, text=setting_title)
        self.title.setStyleSheet("background: none;color: #ffffff;")
        self.title.setFont(font)
        
        font.setFamily("Inter Regular")
        font.setPointSize(9)
        self.checkbox = QCheckBox(self, text=checkbox_title)
        self.checkbox.setStyleSheet("background: none;color: #ffffff;")
        self.checkbox.setFixedWidth(240)
        self.checkbox.setFont(font)
        
        self.grid_layout.addWidget(self.title, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.checkbox, 1, 0, 1, 1)
        
        if combobox_label != "":
            self.combo_title = QLabel(self, text=combobox_label)
            self.combo_title.setStyleSheet("background: none; color: #ffffff;")
            self.combo_title.setFont(font)
            self.combo_title.setFixedWidth(160)
            
            self.interval_combobox = QComboBox(self)
            self.interval_combobox.setFixedWidth(200)
            self.interval_combobox.setStyleSheet("color: #ffffff; border: 1px solid #666666;border-radius: 0px;")
            self.interval_combobox.setFont(font)
            
            self.grid_layout.addWidget(self.combo_title, 1, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
            self.grid_layout.addWidget(self.interval_combobox, 1, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
    
    def add_combo_item(self, item: str):
        if self.interval_combobox is not None:
            self.interval_combobox.addItem(item)
        