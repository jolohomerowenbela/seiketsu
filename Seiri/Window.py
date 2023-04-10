from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Seiri.Styles import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow = QMainWindow):
        MainWindow.resize(480, 360)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.centralwidget.setObjectName("centralWidget")

        icon = QPixmap(".\\resource\\system-file-manager.svg")

        self.logoIcon = QLabel(self.centralwidget)
        self.logoIcon.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred))
        self.logoIcon.setPixmap(icon.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio))
        self.logoIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(23)
        font.setWeight(50)
        
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setText("Welcome To Seiketsu")
        self.titleLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred))
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        
        self.subtitleLabel = QLabel(self.centralwidget)
        self.subtitleLabel.setText("Organize your files in a simple and pragmatic way, my favorite.")
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(10)

        self.organizeButton = QToolButton(self.centralwidget)
        self.organizeButton.setText("Organize Files")
        self.organizeButton.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.organizeButton.setFont(font)
        self.organizeButton.setObjectName("organizeButton")

        organizeIcon = QIcon()
        organizeIcon.addPixmap(QPixmap(".\\resource\\start.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.organizeButton.setIcon(organizeIcon)
        self.organizeButton.setIconSize(QSize(100, 100))
        self.organizeButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(10)

        self.customizeButton = QToolButton(self.centralwidget)
        self.customizeButton.setText("Customize Directories")
        self.customizeButton.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.customizeButton.setFont(font)
        self.customizeButton.setObjectName("customizeButton")

        customizeIcon = QIcon()
        customizeIcon.addPixmap(QPixmap(".\\resource\\setting.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.customizeButton.setIcon(customizeIcon)
        self.customizeButton.setIconSize(QSize(100, 100))
        self.customizeButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(10)

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setText("Close")
        self.closeButton.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.closeButton.setMinimumSize(QSize(100, 30))
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(10)

        self.showOutputButton = QPushButton(self.centralwidget)
        self.showOutputButton.setText("Output")
        self.showOutputButton.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.showOutputButton.setMinimumSize(QSize(100, 30))
        self.showOutputButton.setFont(font)
        self.showOutputButton.setObjectName("showOutputButton")

        self.mainButtonsLayout = QHBoxLayout()
        self.mainButtonsLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.mainButtonsLayout.setContentsMargins(40, 20, 40, 10)
        self.mainButtonsLayout.setSpacing(20)
        self.mainButtonsLayout.addWidget(self.organizeButton)
        self.mainButtonsLayout.addWidget(self.customizeButton)

        self.navigationLayout = QHBoxLayout()
        self.navigationLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationLayout.addWidget(self.closeButton, 0,Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.navigationLayout.addWidget(self.showOutputButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(-1, 10, -1, -1)
        self.mainLayout.addWidget(self.logoIcon)
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.subtitleLabel)
        self.mainLayout.addLayout(self.mainButtonsLayout)
        self.mainLayout.addLayout(self.navigationLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet(style())
        MainWindow.setWindowTitle("Seiri")
