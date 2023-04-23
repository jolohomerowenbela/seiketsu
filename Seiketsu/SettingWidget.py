from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
            
            self.combobox = QComboBox(self)
            self.combobox.setFixedWidth(200)
            self.combobox.setStyleSheet("color: #ffffff; border: 1px solid #666666;border-radius: 0px;")
            self.combobox.setFont(font)
            
            self.grid_layout.addWidget(self.combo_title, 1, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
            self.grid_layout.addWidget(self.combobox, 1, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
    
    def add_items(self, items: list[str], checkable: bool):
        if self.combobox is not None:
            for index, item in enumerate(items):
                self.combobox.addItem(item)
                if checkable:
                    model_item = self.combobox.model().item(index, 0)
                    model_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    model_item.setCheckState(Qt.Unchecked)