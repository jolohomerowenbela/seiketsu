from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from ButtonEffect import ButtonEffect

class FoldersTree(QWidget):
    def __init__(self, window = QMainWindow):
        super().__init__()
        
        self.parentWindow = window
        self.listView = QListView()
        self.listView.setFixedHeight(100)
        self.listModel = QStandardItemModel()
        self.listView.setModel(self.listModel)
        self.listView.setGraphicsEffect(ButtonEffect(self, radius=20))
        
        self.addButton = QPushButton()
        self.addButton.setText("Add")
        self.addButton.setMinimumHeight(50)
        self.addButton.setFixedWidth(150)
        self.addButton.clicked.connect(self.addValues)
        self.addButton.setGraphicsEffect(ButtonEffect(self, radius=75))

        self.removeButton = QPushButton()
        self.removeButton.setText("Remove")
        self.removeButton.setMinimumHeight(50)
        self.removeButton.setFixedWidth(150)
        self.removeButton.clicked.connect(self.removeValues)
        self.removeButton.setGraphicsEffect(ButtonEffect(self, radius=75))
        
        layout = QGridLayout(self)
        
        layout.addWidget(self.listView, 0, 0, 1, 2)
        layout.addWidget(self.addButton, 1, 0, 1, 1)
        layout.addWidget(self.removeButton, 1, 1, 1, 1)
        layout.setAlignment(self.addButton, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(self.removeButton, Qt.AlignmentFlag.AlignCenter)

    def addValues(self):
        path = QFileDialog.getExistingDirectory(self.parentWindow, "Select Folder")
        if path != None and path != "":
            item = QStandardItem(path)
            item.setEditable(False)
            self.listModel.appendRow(item)
            self.removeButton.setEnabled(True)

    def removeValues(self):
        for index in self.listView.selectedIndexes():
            self.listModel.itemFromIndex(index)
            self.listModel.removeRow(index.row())

        if self.listModel.rowCount() <= 0:
            self.removeButton.setEnabled(False)

    def updateButtons(self):
        if self.listModel.rowCount() <= 0:
            self.removeButton.setEnabled(False)
        else:
            self.removeButton.setEnabled(True)