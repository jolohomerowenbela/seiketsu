# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Seiketsu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 620)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: #ffffff;")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setStyleSheet(u"border-color: white;\n"
"border-radius: 0px;")
        icon = QIcon()
        icon.addFile(u"system-file-manager.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Inter")
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(70, 30, 70, 80)
        self.organizeButton = QToolButton(self.centralwidget)
        self.organizeButton.setObjectName(u"organizeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.organizeButton.sizePolicy().hasHeightForWidth())
        self.organizeButton.setSizePolicy(sizePolicy2)
        self.organizeButton.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"STXinwei")
        font2.setPointSize(15)
        self.organizeButton.setFont(font2)
        self.organizeButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.organizeButton.setStyleSheet(u"#organizeButton {\n"
"	background-color: #43d6b5;\n"
"	border-radius: 30px;\n"
"	color: white;\n"
"	padding-top: 30%;\n"
"}\n"
"\n"
"#organizeButton:pressed {\n"
"	background-color: #28bca3;\n"
"	border-radius: 30px;\n"
"	color: white;\n"
"	padding-top: 30%;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.organizeButton.setIcon(icon1)
        self.organizeButton.setIconSize(QSize(100, 100))
        self.organizeButton.setCheckable(False)
        self.organizeButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.organizeButton.setAutoRaise(False)
        self.organizeButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.organizeButton)

        self.customizeButton = QToolButton(self.centralwidget)
        self.customizeButton.setObjectName(u"customizeButton")
        sizePolicy2.setHeightForWidth(self.customizeButton.sizePolicy().hasHeightForWidth())
        self.customizeButton.setSizePolicy(sizePolicy2)
        self.customizeButton.setFont(font2)
        self.customizeButton.setStyleSheet(u"#customizeButton {\n"
"background-color: #9bdb4d;\n"
"border-radius: 30px;\n"
"color: white;\n"
"padding-top: 30%;\n"
"}\n"
"\n"
"#customizeButton:pressed {\n"
"background-color: #68b723;\n"
"border-radius: 30px;\n"
"color: white;\n"
"padding-top: 30%;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customizeButton.setIcon(icon2)
        self.customizeButton.setIconSize(QSize(100, 100))
        self.customizeButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.customizeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy3)
        self.closeButton.setMinimumSize(QSize(150, 50))
        font3 = QFont()
        font3.setFamily(u"Inter")
        font3.setPointSize(12)
        self.closeButton.setFont(font3)
        self.closeButton.setStyleSheet(u"border-radius: 0px;")

        self.horizontalLayout_2.addWidget(self.closeButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.openButton = QPushButton(self.centralwidget)
        self.openButton.setObjectName(u"openButton")
        sizePolicy3.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy3)
        self.openButton.setMinimumSize(QSize(150, 50))
        self.openButton.setFont(font3)
        self.openButton.setStyleSheet(u"border-radius: 0px;")

        self.horizontalLayout_2.addWidget(self.openButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome To Seiri", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Organize your files in a simple and pragmatic way, my favorite.", None))
        self.organizeButton.setText(QCoreApplication.translate("MainWindow", u"Organize Files", None))
        self.customizeButton.setText(QCoreApplication.translate("MainWindow", u"Customize Directories", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
    # retranslateUi

