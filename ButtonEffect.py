from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import typing

class ButtonEffect(QGraphicsDropShadowEffect):
    def __init__(self, parent: typing.Optional[QObject] = ..., radius = int) -> None:
        super().__init__(parent)
        self.setOffset(1, 1)
        self.setColor(QColor(178, 184, 201))
        self.setBlurRadius(radius)