from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

GLOBAL_STATE = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.centralwidget = QWidget(self)
        # self.centralwidget.setObjectName("centralwidget")

        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        # self.drop_shadow_layout.setObjectName("drop_shadow_layout")

        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 154, 131, 255), stop:0.521368 rgba(0, 115, 103, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        # self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.drop_shadow_frame.setGraphicsEffect(self.shadow)

        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        # self.title_bar.setObjectName("title_bar")

        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setMinimumSize(QSize(0, 50))

        font = QFont()
        font.setFamily("Inter Condensed Light")
        font.setPointSize(14)

        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        # self.frame_title.setObjectName("frame_title")

        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.icon = QLabel(self.frame_title)

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        # sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())

        self.icon.setSizePolicy(sizePolicy)
        pixmap = QPixmap(".\\resource\\icon.svg")
        self.icon.setPixmap(pixmap.scaled(QSize(48, 48), Qt.AspectRatioMode.KeepAspectRatio))
        # self.icon.setObjectName("icon")
        
        self.horizontalLayout_2.addWidget(self.icon)
        self.label_title = QLabel(self.frame_title)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(95)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)

        font = QFont()
        font.setFamily("Inter")
        font.setPointSize(14)

        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(250, 250, 250);")
        # self.label_title.setObjectName("label_title")

        self.horizontalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        # self.frame_btns.setObjectName("frame_btns")

        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(249, 196, 64);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(249, 196, 64, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(104, 183, 35);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(104, 183, 35, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(198, 38, 46);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(198, 38, 46, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.setCentralWidget(self.centralwidget)
        
        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet("#content_bar {\n"
# "    border: none;\n"
# "    border-radius: 8px;        \n"
"    background-color: #fafafa;\n"
"    margin: 10px;\n"
"    margin-top: 0px;\n"
# "    background-color: #fafafa;\n"
"}")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        
        self.content_layout = QVBoxLayout(self.content_bar)
        
        self.logo = QLabel(self.content_bar)
        # self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(".\\resource\\logo.svg")
        self.logo.setPixmap(pixmap.scaled(QSize(128, 128), Qt.AspectRatioMode.KeepAspectRatio))
        self.logo.setObjectName("logo")
        self.logo.setStyleSheet("background: none;")
        
        font = QFont()
        font.setFamily("Inter ExtraBold")
        font.setPointSize(52)

        self.app_label = QLabel(self.content_bar, text= "seiketsu")
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        self.app_label.setStyleSheet("#app_label {\n"
"    background: none;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        
        self.subtitle = QLabel(self.content_bar, text = '"Streamline your files with Seiketsu - The organized way to productivity."')
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setStyleSheet("#subtitle {\n"
"   background: none;\n"
"   color: rgb(0, 0, 0);\n"
"}")

        self.button_box = QLabel(self.content_bar)
        self.button_box.setObjectName("button_box")
        self.button_box.setStyleSheet("#button_box {\n"
"   background: none;\n"
"   color: rgb(0, 0, 0);\n"
"}")
        
        self.content_layout.addWidget(self.logo, stretch=20, alignment= Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.content_layout.addWidget(self.app_label, stretch=15, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.subtitle, stretch=5, alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.content_layout.addWidget(self.button_box, 60)

        self.verticalLayout.addWidget(self.content_bar)
        self.title_bar.mouseMoveEvent = self.moveWindow
        
        self.btn_maximize.clicked.connect(lambda: self.maximize_restore())
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.btn_close.clicked.connect(lambda: self.close())

        # ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.frame_grip)
        # self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")
        
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        #     # RESTORE BEFORE MOVE
        #     if UIFunctions.returnStatus() == 1:
        #         UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
                self.showMaximized()

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1

                # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
                self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
                # self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
                self.btn_maximize.setToolTip("Restore")
        else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.resize(self.width()+1, self.height()+1)
                self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
                # self.drop_shadow_frame.setStyleSheet("backgroundW-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
                self.btn_maximize.setToolTip("Maximize")

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Seiketsu"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wu = MainWindow()
    wu.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    wu.setAttribute(Qt.WA_TranslucentBackground)
    wu.show()
    
    app.exec()