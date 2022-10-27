from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QLabel, QHBoxLayout, QSystemTrayIcon, QSizeGrip
from PyQt5.QtCore import QPoint, Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
import sys
import ctypes
from design.Ui_main_admin import Ui_MainWindow
from classes.warning import Warning
from classes.confirm import Confirm
from classes_admin.login import Login
from classes.sql import *

class Main_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        login = Login()
        login.exec()
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.to_close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btnCancel_2.clicked.connect(self.cancel_setting)
        self.btnOk_2.clicked.connect(self.save_setting)
        self.btn_updatepassword.clicked.connect(self.updatePassword)
        if login.login is None:
            sys.exit()
        self.id = login.adminid
        self.name, self.surname, self.phone, self.address = getAdminInfo(login.adminid)
        self.label_admin.setText(self.name + " " + self.surname)
        self.cancel_setting()
        self.moveFlag = False
        self.gripSize = 16
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

    def cancel_setting(self):
        if self.btnCancel_2.text() == "Bekor qilish":
            self.edit_name.setText(self.name)
            self.edit_surname.setText(self.surname)
            self.edit_phone.setText(self.phone)
            self.edit_address.setText(self.address)
            self.edit_name.setReadOnly(True)
            self.edit_surname.setReadOnly(True)
            self.edit_phone.setReadOnly(True)
            self.edit_address.setReadOnly(True)

            self.btnCancel_2.setText("Taxrirlash")
        else:
            self.edit_name.setReadOnly(False)
            self.edit_surname.setReadOnly(False)
            self.edit_phone.setReadOnly(False)
            self.edit_address.setReadOnly(False)
            self.btnCancel_2.setText("Bekor qilish")

    def save_setting(self):
        if self.edit_name.text() == self.name and self.edit_surname.text() == self.surname and \
                self.edit_phone.text() == self.phone and self.edit_address.toPlainText() == self.address:
            Warning("Profil ma'lumotlari o'zgartirilmagan").exec()
        elif self.edit_name.text() == "" or self.edit_surname.text() == "" or \
                self.edit_phone.text() == "" or self.edit_address.toPlainText() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        else:
            updateAdminInfo(self.id, self.edit_name.text(), self.edit_surname.text(),
                           self.edit_phone.text(), self.edit_address.toPlainText())
            self.name = self.edit_name.text()
            self.surname = self.edit_surname.text()
            self.phone = self.edit_phone.text()
            self.address = self.edit_address.toPlainText()
            self.label_admin.setText(self.name + " " + self.surname)
            self.edit_name.setReadOnly(True)
            self.edit_surname.setReadOnly(True)
            self.edit_phone.setReadOnly(True)
            self.btnCancel_2.setText("Taxrirlash")
            Warning("Profil ma'lumotlari yangilandi").exec()

    def updatePassword(self):
        if (checkAdminPassword(self.id, self.old_password.text())) is False:
            Warning("Eski parol xato kiritildi").exec()
        elif len(self.password_1.text()) < 6:
            Warning("Yangi parol 6 yoki undan ortiq belgidan iborat bo'lishi lozim").exec()
        elif self.password_1.text() != self.password_2.text():
            Warning("Yangi parol tasdiqlanmadi").exec()
        else:
            updateAdminPassword(self.id, self.password_1.text())
            self.old_password.setText(self.password_1.text())
            self.password_1.clear()
            self.password_2.clear()
            Warning("Parol Yangilandi").exec()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def resizeEvent(self, event):
        self.moveFlag = False
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        self.grip.move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        event.accept()

    def to_close(self):
        confirm = Confirm("Chiqishni xohlaysizmi?")
        confirm.exec()
        if confirm.confirmation:
            self.close()

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

