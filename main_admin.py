from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QLabel, QHBoxLayout, QSystemTrayIcon, QSizeGrip
from PyQt5.QtCore import QPoint, Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from functools import partial
import sys
import ctypes
from design.Ui_main_admin import Ui_MainWindow
from classes.warning import Warning
from classes.information import Information
from classes.update_password import Update_password
from classes.confirm import Confirm
from classes_admin.login import Login
from classes.sql import *
from classes.image import saveImage

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

        # self.btn_updatepassword.clicked.connect(self.updatePassword)

        if login.login is None:
            sys.exit()
        self.id = login.adminid
        self.name, self.surname, self.phone, self.address, self.male = getAdminInfo(login.adminid)
        self.label_admin.setText(self.name + " " + self.surname)

        self.btn_remove.clicked.connect(partial(self.updateAvatar, 'img/avatar/avatar.png'))
        self.btn_template.clicked.connect(self.templateAvatar)
        self.btn_next.clicked.connect(self.nexttemplateAvatar)
        self.btn_previous.clicked.connect(self.previoustemplateAvatar)
        self.btn_edit_2.clicked.connect(self.edit_profile)
        self.btn_updatepassword.clicked.connect(self.updatePassword)

        self.cancel_setting()
        self.moveFlag = False
        self.gripSize = 16
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.templateAvatarIndex = 0
        self.change = False
        self.avatar_src = f'data/data_avatar/{self.id}.png'

    def updatePassword(self):
        Update_password(self.id, True).exec()

    def edit_profile(self):
        self.edit_name.setReadOnly(False)
        self.edit_surname.setReadOnly(False)
        self.edit_phone.setReadOnly(False)
        self.edit_address.setReadOnly(False)
        self.radio_male.setEnabled(True)
        self.radio_female.setEnabled(True)

    def cancel_setting(self):
        self.edit_name.setText(self.name)
        self.edit_surname.setText(self.surname)
        self.edit_phone.setText(self.phone)
        self.edit_address.setText(self.address)
        self.updateAvatar(f'data/data_avatar/{self.id}.png')
        if self.male:
            self.radio_male.setChecked(True)
        else:
            self.radio_female.setChecked(True)
        self.edit_name.setReadOnly(True)
        self.edit_surname.setReadOnly(True)
        self.edit_phone.setReadOnly(True)
        self.edit_address.setReadOnly(True)
        self.radio_male.setEnabled(False)
        self.radio_female.setEnabled(False)

    def save_setting(self):
        if not self.change and self.edit_name.text() == self.name and self.edit_surname.text() == self.surname and \
                self.edit_phone.text() == self.phone and self.edit_address.toPlainText() == self.address:
            Warning("Profil ma'lumotlari o'zgartirilmagan").exec()
        elif not self.change and self.edit_name.text() == "" or self.edit_surname.text() == "" or \
                self.edit_phone.text() == "" or self.edit_address.toPlainText() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        else:
            saveImage(self.avatar_src, f'data/data_avatar/{self.id}.png')
            updateAdminInfo(self.id, self.edit_name.text(), self.edit_surname.text(),
                           self.edit_phone.text(), self.edit_address.toPlainText(), self.male)
            self.name = self.edit_name.text()
            self.surname = self.edit_surname.text()
            self.phone = self.edit_phone.text()
            self.address = self.edit_address.toPlainText()
            self.label_admin.setText(self.name + " " + self.surname)
            self.edit_name.setReadOnly(True)
            self.edit_surname.setReadOnly(True)
            self.edit_phone.setReadOnly(True)
            self.btnCancel_2.setText("Taxrirlash")
            Information("Profil ma'lumotlari yangilandi").exec()

    def updateAvatar(self, path):
        self.avatar.setPixmap(self.load_img(path))
        self.change = True
        self.avatar_src = path

    def templateAvatar(self):
        self.templateAvatarIndex = 0
        self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png')

    def nexttemplateAvatar(self):
        self.templateAvatarIndex += 1
        self.templateAvatarIndex %= 17
        self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png')

    def previoustemplateAvatar(self):
        self.templateAvatarIndex -= 1
        self.templateAvatarIndex %= 17
        self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def load_img(self, path):
        pixmap = QPixmap(path)
        return pixmap

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

