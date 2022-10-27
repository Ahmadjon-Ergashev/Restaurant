from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QSystemTrayIcon, QSizeGrip
from PyQt5.QtCore import QPoint, Qt, QSize, QRect, QEvent
from PyQt5.QtGui import QPixmap, QIcon, QResizeEvent
import PyQt5.QtCore
import sys
import ctypes
from design.Ui_main_admin import Ui_MainWindow
from classes.warning import Warning
from classes.confirm import Confirm
# from classes.login import Login
# from classes.sql import *

class Main_user(QMainWindow):
    def __init__(self):
        # login = Login()
        # login.exec()
        super(Main_user, self).__init__()

        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.btn_close.clicked.connect(self.to_close)
        # self.btn_minimize.clicked.connect(self.showMinimized)

        self.window = QWidget(self)
        self.window.setStyleSheet("background: rgba(0,0,0,0.5);")

        # if you are not using qtmodern darkstyle, you can still make the QWidget resizeable and frameless by uncommenting the code below then commenting out the qtmodern code

        # flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # window.setWindowFlags(flags)
        # self.window.setGeometry(QRect(0, 0, 300, 300))  # arbitrary size/location

        self.window.installEventFilter(self)

    def eventFilter(self, watched, event):
        if self.window is watched:
            if event.type() == QEvent.Enter:
                self.window.resize(50, self.window.height())
            elif event.type() == QEvent.Leave:
                self.window.resize(100, self.window.height())
        return super(Main_user, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon()
    app_icon.addFile("img/main 128.png", QSize(128, 128))
    app_icon.addFile("img/main 64.png", QSize(64, 64))
    app_icon.addFile("img/main 48.png", QSize(48, 48))
    app_icon.addFile("img/main 32.png", QSize(32, 32))
    app_icon.addFile("img/main 16.png", QSize(16, 16))
    app.setWindowIcon(app_icon)

    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # tray = QSystemTrayIcon()
    # tray.setIcon(app_icon)
    # tray.setVisible(True)
    win = Main_user()
    win.show()
    sys.exit(app.exec_())