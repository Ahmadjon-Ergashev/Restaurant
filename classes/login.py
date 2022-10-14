from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import sys
import pickle as pc
import os

from design.Ui_Login import Ui_Login
from classes.registration import Registration
from classes.warning import Warning

class Login(QDialog, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.btn_newAccount.clicked.connect(self.newAccount)
        self.btn_sign.clicked.connect(self.sign)

        # print(str(os.getcwd()))
        # os.path.dirname(os.path.dirname(__file__)) + "\\userPickles\\lastlog.pc"

        try:
            with open('userPickles/lastlog.pc', 'rb') as file:
                log = pc.load(file)
                if len(log)>0:
                    self.remember_me.setChecked(True)
                    self.username.setText(log[0])
                    self.password.setText(log[1])
        except:
            pass

    def sign(self):
        if len(self.username.text())<6 or len(self.password.text())<6:
            Warning("Foydalanovchi nomi yoki parol 6 ta belgidan kam bo'lmasligi kerak").exec_()
        self.Remember()

    def Remember(self):
        if self.remember_me.isChecked():
            try:
                with open('userPickles/lastlog.pc', 'wb') as file:
                    pc.dump([self.username.text(), self.password.text()], file)
            except:
                pass
        else:
            try:
                with open('userPickles/lastlog.pc', 'wb') as file:
                    file.truncate()
            except:
                pass


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def newAccount(self):
        Registration().exec()

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Login()
    win.show()
    sys.exit(app.exec())