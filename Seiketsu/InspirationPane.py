from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class InspirationPane(QVBoxLayout):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()