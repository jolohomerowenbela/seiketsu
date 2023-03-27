from PyQt6.QtWidgets import QApplication
from window import Window
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    
    app.exec()