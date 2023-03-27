from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from foldersTree import *
import os

class OrganizeFiles():
    def __init__(self, chooser = FoldersTree):
        self.chooser = chooser
    def start(self):
        if self.chooser.listModel.rowCount() == 0:
            self.organize("C:/Users/owend/")
        else:
            for index in range(self.chooser.listModel.rowCount()):
                item = self.chooser.listModel.index(index, 0)
                self.organize(item.data())
    def organize(self, path):
        try:
            access = os.access(path, os.W_OK) and os.access(path, os.R_OK)
            if access and os.path.basename(path)[0:] != '.':
                for files in os.listdir(path):
                    fullpath = path + files
                    if os.path.isdir(fullpath):
                        self.organize(fullpath)
                    else:
                        print(fullpath)
        except PermissionError:
            print(path, " cannot be opened due to permission issues.")