from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt

import sys
import pickle as pc

from design.Ui_Login_admin import Ui_Login
from classes.registration import Registration
from classes.warning import Warning
from classes.sql import logIn_admin, getAdminid

class Login(QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_sign.clicked.connect(self.sign)

        self.login = None
        self.adminid = None

        try:
            with open('userPickles/lastlog.pc', 'rb') as file:
                log = pc.load(file)
                if len(log) > 0:
                    self.remember_me.setChecked(True)
                    self.username.setText(log[0])
                    self.password.setText(log[1])
        except:
            pass

    def sign(self):
        if len(self.username.text()) < 6 or len(self.password.text()) < 6:
            Warning("Foydalanovchi nomi yoki parol 6 ta belgidan kam bo'lmasligi kerak").exec_()
        else:
            if logIn_admin(self.username.text(), self.password.text()):
                self.login = True
                self.adminid = getAdminid(self.username.text(), self.password.text())
                self.Remember()
                self.close()
            else:
                Warning("Foydalanuvchi nomi yoki parol xato").exec()

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
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())