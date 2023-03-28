from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import *
from Seiri.Window import Ui_MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
    wu = Ui_MainWindow()
    wu.setupUi(w)
    w.show()
    
    app.exec()