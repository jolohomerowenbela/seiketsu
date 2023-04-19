from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from Seiketsu.Window import Window
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wu = Window()
    wu.show()
    
    app.exec()