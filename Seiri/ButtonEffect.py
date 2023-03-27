from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import typing

class ButtonEffect(QGraphicsDropShadowEffect):
    def __init__(self, parent: typing.Optional[QObject] = ..., radius = int) -> None:
        super().__init__(parent)
        self.setOffset(1, 1)
        self.setColor(QColor(178, 184, 201))
        self.setBlurRadius(radius)