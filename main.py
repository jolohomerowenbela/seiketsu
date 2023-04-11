from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from Seiketsu.Window import Ui_MainWindow
from qframelesswindow import FramelessMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FramelessMainWindow()
    wu = Ui_MainWindow()
    wu.setupUi(w)
    w.titleBar.raise_()
    w.show()
    
    app.exec()