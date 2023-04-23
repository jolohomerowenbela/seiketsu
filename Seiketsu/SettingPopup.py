from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiketsu.SettingWidget import SettingWidget
import Seiketsu.Titlebar
import Seiketsu.Settings

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
        pixmap = QPixmap(".\\resource\\automate.svg")
        self.icon_auto.setPixmap(pixmap.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon_auto.setStyleSheet("background: none;border: 2px solid #9bdb4d;padding-left: 10px; padding-right: 10px;")
        
        self.setting_auto = SettingWidget(self.content, "Automatic Organization", "Set Automatic Organization.", "Organize files every:")
        self.setting_auto.add_items(["1 week", "4 hours", "12 hours", "1 day", "1 month", "3 months"], False)
        
        self.icon_func = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\function.svg")
        self.icon_func.setPixmap(pixmap.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon_func.setStyleSheet("background: none;border: 2px solid #9bdb4d;padding-left: 10px; padding-right: 10px;")
        
        self.setting_func = SettingWidget(self.content, "Functionality", "Rename obscure filenames.", "Organize files by:")
        self.setting_func.add_items(["Filename Analysis", "Document Analysis", "Photo Analysis"], True)
        
        self.icon_add = QLabel(self.content)
        pixmap = QPixmap(".\\resource\\quote.svg")
        self.icon_add.setPixmap(pixmap.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio))
        self.icon_add.setStyleSheet("background: none;border: 2px solid #9bdb4d;padding-left: 10px; padding-right: 10px;")
        
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
        
        self.setStartupConditions()
        self.setting_auto.checkbox.stateChanged.connect(self.automatic_changed)
        self.setting_auto.combobox.currentTextChanged.connect(self.automated_interval_changed)
        self.setting_add.checkbox.stateChanged.connect(self.quote_disable_changed)
        self.setting_func.checkbox.stateChanged.connect(self.rename_obscure_changed)
        self.setting_func.combobox.model().itemChanged.connect(self.methods_enabled)

    def close_setting(self):
        self.parent.show_settings()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def methods_enabled(self, item: QStandardItem):
        methods = list(Seiketsu.Settings.getMethods())
        if item.checkState():
            if item.text() not in methods:
                methods.insert(item.index().row(), item.text())
                Seiketsu.Settings.setMethods(methods)
        else:
            if item.text() in methods:
                methods.remove(item.text())
                Seiketsu.Settings.setMethods(methods)
    
    def rename_obscure_changed(self, value):
        Seiketsu.Settings.setRenameObscure(bool(value))
    
    def automated_interval_changed(self, interval):
        Seiketsu.Settings.setAutomatedInterval(interval)

    def automatic_changed(self, value):
        Seiketsu.Settings.setAutomatic(bool(value))
        if bool(value):
            self.setting_auto.combobox.setEnabled(True)
            self.setting_auto.combo_title.setStyleSheet("background: none; color: #ffffff;")
            self.setting_auto.combobox.setStyleSheet("color: #ffffff; border: 1px solid #666666;border-radius: 0px;")
        else:
            self.setting_auto.combobox.setEnabled(False)
            self.setting_auto.combo_title.setStyleSheet("background: none;color: rgba(255, 255, 255, 127)")
            self.setting_auto.combobox.setStyleSheet("color: rgba(255, 255, 255, 127);border: 1px solid #666666;border-radius: 0px;")
    
    def quote_disable_changed(self, value):
        Seiketsu.Settings.setQuotesDisabled(bool(value))

    def setStartupConditions(self):
        if Seiketsu.Settings.getAutomatic():
            self.setting_auto.checkbox.setChecked(True)
        else:
            self.setting_auto.checkbox.setChecked(False)
            self.setting_auto.combobox.setEnabled(False)
            self.setting_auto.combo_title.setStyleSheet("background: none;color: rgba(255, 255, 255, 127)")
            self.setting_auto.combobox.setStyleSheet("color: rgba(255, 255, 255, 127);border: 1px solid #666666;border-radius: 0px;")
        
        if Seiketsu.Settings.getRenameObscure():
            self.setting_func.checkbox.setChecked(True)
        else:
            self.setting_func.checkbox.setChecked(False)

        if Seiketsu.Settings.getQuotesDisabled():
            self.setting_add.checkbox.setChecked(True)
        else:
            self.setting_add.checkbox.setChecked(False)
        
        methods = Seiketsu.Settings.getMethods()
        for index in range(self.setting_func.combobox.model().rowCount()):
            item = self.setting_func.combobox.model().item(index, 0)
            if item.text() in methods:
                item.setCheckState(True)
                item.setSelectable(False)
        
        interval = Seiketsu.Settings.getAutomatedInterval()
        for index in range(self.setting_auto.combobox.model().rowCount()):
            item = self.setting_auto.combobox.model().item(index, 0)
            if item.text() == interval:
                self.setting_auto.combobox.setCurrentIndex(index)
                

    def moveWindow(self, event):
        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()