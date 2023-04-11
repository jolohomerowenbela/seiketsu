from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from Seiketsu.Window import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wu = MainWindow()
    wu.titleBar.raise_()
    wu.show()
    
    app.exec()