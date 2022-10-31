from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSizeGrip
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from functools import partial
import sys
import ctypes
from design.Ui_main_admin import Ui_MainWindow
from classes.warning import Warning
from classes.information import Information
from classes.update_password import Update_password
from classes.confirm import Confirm
from classes.login_admin import Login
from classes.sql import *
from classes.image import saveImage


class Main_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        login = Login()
        login.exec()
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.toClose)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.moveFlag = False
        self.gripSize = 16
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        if login.login is None:
            sys.exit()
        self.id = login.adminid
        self.username, self.name, self.surname, self.phone, self.address, self.male = getAdminInfo(self.id)
        self.permissions = getAdminPermissions(self.id)
        self.label_admin.setText(self.name + " " + self.surname)

        # Tab Profile
        self.btn_cancelProfile.clicked.connect(self.cancelSetting)
        self.btn_saveProfile.clicked.connect(self.saveSetting)
        self.btn_removeAvatarProfile.clicked.connect(partial(self.updateAvatar, 'img/avatar/avatar.png', True))
        self.btn_templateAvatarProfile.clicked.connect(partial(self.templateAvatar, True))
        self.btn_nextAvatarProfile.clicked.connect(partial(self.nexttemplateAvatar, True))
        self.btn_previousAvatarProfile.clicked.connect(partial(self.previoustemplateAvatar, True))
        self.btn_editInfoProfile.clicked.connect(self.editProfile)
        self.btn_updatepasswordProfile.clicked.connect(self.updatePassword)
        self.cancelSetting()
        self.templateAvatarIndex = 0
        self.change = False
        self.avatar_src = f'data/data_avatar/admin/{self.id}.png'

        # Tab Admins
        self.btn_removeAvatarAdmin.clicked.connect(partial(self.updateAvatar, 'img/avatar/avatar.png', False))
        self.btn_templateAvatarAdmin.clicked.connect(partial(self.templateAvatar, False))
        self.btn_nextAvatarAdmin.clicked.connect(partial(self.nexttemplateAvatar, False))
        self.btn_previousAvatarAdmin.clicked.connect(partial(self.previoustemplateAvatar, False))
        self.btn_editInfoAdmin.clicked.connect(self.editAdminInfo)
        self.btn_addAdmin.clicked.connect(self.addAdmin)
        self.btn_saveAdmin.clicked.connect(self.saveAdminInfo)
        self.btn_cancelAdmin.clicked.connect(partial(self.cancelAdminInfo, True))
        self.btn_deleteAdmin.clicked.connect(self.deleteAdmin)
        self.addingAdmin = False
        self.adminAvatar_src = ""
        self.editingAdminId = None
        self.loadAdmins()
        self.cancelAdminInfo()

        # Tab Users
        self.btn_saveUser.clicked.connect(self.saveUserInfo)
        self.btn_cancelUser.clicked.connect(self.cancelUserInfo)
        self.btn_editInfoUser.clicked.connect(self.editUserInfo)
        self.btn_removeAvatarUser.clicked.connect(partial(self.updateUserAvatar, 'img/avatar/avatar.png'))
        self.btn_templateAvatarUser.clicked.connect(self.templateUserAvatar)
        self.btn_nextAvatarUser.clicked.connect(self.nexttemplateUserAvatar)
        self.btn_previousAvatarUser.clicked.connect(self.previoustemplateUserAvatar)
        self.templateUserAvatarIndex = 0
        self.editingUserId = None
        self.userAvatar_src = ""
        self.loadUsers()
        self.cancelUserInfo()

    # Tab Users
    def loadUsers(self):
        self.clearUsers()
        result = users()
        x = 0
        y = 0
        for data in result:
            label_photo = QLabel(data[1] + " " + data[2])
            label_photo.setPixmap(self.load_img(f"data/data_avatar/user/{data[0]}.png"))
            label_photo.setMinimumSize(205, 220)
            label_photo.setMaximumSize(205, 220)
            button_add = QPushButton("Batafsil")
            button_add.clicked.connect(partial(self.viewUserInfo, data[0]))
            button_add.setMinimumSize(200, 30)
            button_add.setMaximumSize(200, 30)
            label_name = QLabel(data[1] + " " + data[2])
            label_name.setMinimumSize(200, 30)
            label_name.setMaximumSize(200, 150)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setWordWrap(True)
            self.gridUsers.addWidget(label_photo, x, y)
            self.gridUsers.addWidget(label_name, x + 1, y)
            self.gridUsers.addWidget(button_add, x + 2, y)
            if y == 3:
                y = 0
                x += 3
            else:
                y += 1

    def clearUsers(self):
        for i in reversed(range(self.gridUsers.count())):
            self.gridUsers.itemAt(i).widget().deleteLater()

    def viewUserInfo(self, id):
        self.editingUserId = id
        info = getUserInfo(id)
        self.edit_nameUser.setText(info[0])
        self.edit_surnameUser.setText(info[1])
        self.edit_phoneUser.setText(info[2])
        self.edit_addressUser.setText(info[3])
        if info[4]:
            self.radio_maleUser.setChecked(True)
        else:
            self.radio_femaleUser.setChecked(True)
        self.avatarUser.setPixmap(self.load_img(f"data/data_avatar/user/{id}.png"))
        self.editingUserId = id

    def editUserInfo(self):
        if not self.permissions[3]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return
        self.edit_nameUser.setReadOnly(False)
        self.edit_surnameUser.setReadOnly(False)
        self.edit_phoneUser.setReadOnly(False)
        self.radio_maleUser.setEnabled(True)
        self.radio_femaleUser.setEnabled(True)
        self.edit_addressUser.setReadOnly(False)
        self.edit_passwordUser.setReadOnly(False)
        self.edit_passwordAgainUser.setReadOnly(False)
        self.userAvatar_src = f'data/data_avatar/user/{self.editingUserId}.png'

    def clearUserInfo(self):
        self.avatarUser.clear()
        self.edit_nameUser.clear()
        self.edit_surnameUser.clear()
        self.edit_phoneUser.clear()
        self.radio_maleUser.setChecked(False)
        self.radio_femaleUser.setChecked(False)
        self.edit_addressUser.clear()
        self.edit_passwordUser.clear()
        self.edit_passwordAgainUser.clear()

    def cancelUserInfo(self):
        self.clearUserInfo()

        self.edit_nameUser.setReadOnly(True)
        self.edit_surnameUser.setReadOnly(True)
        self.edit_phoneUser.setReadOnly(True)
        self.radio_maleUser.setEnabled(False)
        self.radio_femaleUser.setEnabled(False)
        self.edit_addressUser.setReadOnly(True)
        self.edit_passwordUser.setReadOnly(True)
        self.edit_passwordAgainUser.setReadOnly(True)
        self.editingUserId = None

    def saveUserInfo(self):
        if not self.permissions[3]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return

        if self.edit_nameUser.text() == "" or self.edit_surnameUser.text() == "" or \
                self.edit_phoneUser.text() == "" or self.edit_addressUser.toPlainText() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        elif self.edit_passwordUser.text() != self.edit_passwordAgainUser.text():
            Warning("Parollar mos emas").exec()
        else:
            if not checkPhone(self.edit_phoneUser.text()) and \
                    self.edit_phoneUser.text() != getUserInfo(self.editingUserId)[2]:
                Warning("Ushbu telefon raqam band").exec()
            else:
                saveImage(self.userAvatar_src, f'data/data_avatar/user/{self.editingUserId}.png')
                updateUserInfo(self.editingUserId, self.edit_nameUser.text(),
                               self.edit_surnameUser.text(), self.edit_phoneUser.text(),
                               self.edit_addressUser.toPlainText(), self.radio_maleUser.isChecked())
                if self.edit_passwordUser.text() != "":
                    updateUserPassword(self.editingUserId, self.edit_passwordUser.text())
                Information("User ma'lumotlari yangilandi").exec()
                self.cancelUserInfo()
                self.loadUsers()

    def updateUserAvatar(self, path):
        self.avatarUser.setPixmap(self.load_img(path))
        self.userAvatar_src = path

    def templateUserAvatar(self):
        self.updateUserAvatar(f'img/avatar/{str(int(self.radio_maleUser.isChecked()))}' +
                              f'{str(self.templateUserAvatarIndex)}.png')

    def nexttemplateUserAvatar(self):
        self.templateUserAvatarIndex += 1
        self.templateUserAvatarIndex %= 17
        self.updateUserAvatar(f'img/avatar/{str(int(self.radio_maleUser.isChecked()))}' +
                              f'{str(self.templateUserAvatarIndex)}.png')

    def previoustemplateUserAvatar(self):
        self.templateUserAvatarIndex -= 1
        self.templateUserAvatarIndex %= 17
        self.updateUserAvatar(f'img/avatar/{str(int(self.radio_maleUser.isChecked()))}' +
                              f'{str(self.templateUserAvatarIndex)}.png')

    # Tab Admins
    def deleteAdmin(self):
        if not self.permissions[2]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return

        if self.editingAdminId == 1:
            Warning("Kechirasiz superadminni o'chirish mumkin emas").exec()
            return

        if self.editingAdminId is None:
            Warning("O'chirish uchun admin tanlang").exec()
            return

        confirm = Confirm(f"{getAdminInfo(self.editingAdminId)[0]} adminni o'chirishni xohlaysizmi")
        confirm.exec()
        if confirm.confirmation:
            deleteAdmin(self.editingAdminId)
            self.loadAdmins()
            self.cancelAdminInfo()

    def clearAdmins(self):
        for i in reversed(range(self.gridAdmins.count())):
            self.gridAdmins.itemAt(i).widget().deleteLater()

    def addAdmin(self):
        if not self.permissions[1]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return
        self.clearAdminInfo()
        self.editAdminInfo()
        self.edit_usernameAdmin.setFocus()
        self.addingAdmin = True
        self.adminAvatar_src = 'img/avatar/avatar.png'
        self.updateAvatar(self.adminAvatar_src, False)

    def loadAdmins(self):
        self.clearAdmins()
        result = admins()
        x = 0
        y = 0
        for data in result:
            if data[0] == self.id:
                continue
            label_photo = QLabel(data[1] + " " + data[2])
            label_photo.setPixmap(self.load_img(f"data/data_avatar/admin/{data[0]}.png"))
            label_photo.setMinimumSize(205, 220)
            label_photo.setMaximumSize(205, 220)
            button_add = QPushButton("Batafsil")
            button_add.clicked.connect(partial(self.viewAdminInfo, data[0]))
            button_add.setMinimumSize(200, 30)
            button_add.setMaximumSize(200, 30)
            label_name = QLabel(data[1] + " " + data[2])
            label_name.setMinimumSize(200, 30)
            label_name.setMaximumSize(200, 150)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setWordWrap(True)
            self.gridAdmins.addWidget(label_photo, x, y)
            self.gridAdmins.addWidget(label_name, x + 1, y)
            self.gridAdmins.addWidget(button_add, x + 2, y)
            if y == 3:
                y = 0
                x += 3
            else:
                y += 1

    def viewAdminInfo(self, id):
        self.addingAdmin = False
        self.editingAdminId = id
        info = getAdminInfo(id)
        permissions = getAdminPermissions(id)
        self.edit_usernameAdmin.setText(info[0])
        self.edit_nameAdmin.setText(info[1])
        self.edit_surnameAdmin.setText(info[2])
        self.edit_phoneAdmin.setText(info[3])
        self.edit_addressAdmin.setText(info[4])
        if info[5]:
            self.radio_maleAdmin.setChecked(True)
        else:
            self.radio_femaleAdmin.setChecked(True)
        self.avatarAdmin.setPixmap(self.load_img(f"data/data_avatar/admin/{id}.png"))
        self.check_orders.setChecked(permissions[0])
        self.check_addAdmin.setChecked(permissions[1])
        self.check_editAdmin.setChecked(permissions[2])
        self.check_editUser.setChecked(permissions[3])
        self.check_addProduct.setChecked(permissions[4])
        self.check_editProduct.setChecked(permissions[5])
        self.editingAdminId = id

    def editAdminInfo(self):
        if not self.permissions[2]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return
        self.edit_usernameAdmin.setReadOnly(False)
        self.edit_nameAdmin.setReadOnly(False)
        self.edit_surnameAdmin.setReadOnly(False)
        self.edit_phoneAdmin.setReadOnly(False)
        self.radio_maleAdmin.setEnabled(True)
        self.radio_femaleAdmin.setEnabled(True)
        self.edit_addressAdmin.setReadOnly(False)
        self.edit_passwordAdmin.setReadOnly(False)
        self.edit_passwordAgainAdmin.setReadOnly(False)
        self.check_orders.setEnabled(True)
        self.check_addAdmin.setEnabled(True)
        self.check_editAdmin.setEnabled(True)
        self.check_editUser.setEnabled(True)
        self.check_addProduct.setEnabled(True)
        self.check_editProduct.setEnabled(True)
        self.adminAvatar_src = f'data/data_avatar/admin/{self.editingAdminId}.png'

    def clearAdminInfo(self):
        self.avatarAdmin.clear()
        self.edit_nameAdmin.clear()
        self.edit_surnameAdmin.clear()
        self.edit_phoneAdmin.clear()
        self.edit_usernameAdmin.clear()
        self.radio_maleAdmin.setChecked(False)
        self.radio_femaleAdmin.setChecked(False)
        self.edit_addressAdmin.clear()
        self.edit_passwordAdmin.clear()
        self.edit_passwordAgainAdmin.clear()
        self.check_orders.setChecked(False)
        self.check_addAdmin.setChecked(False)
        self.check_editAdmin.setChecked(False)
        self.check_editUser.setChecked(False)
        self.check_addProduct.setChecked(False)
        self.check_editProduct.setChecked(False)

    def cancelAdminInfo(self, clear=True):
        if clear:
            self.clearAdminInfo()

        self.edit_usernameAdmin.setReadOnly(True)
        self.edit_nameAdmin.setReadOnly(True)
        self.edit_surnameAdmin.setReadOnly(True)
        self.edit_phoneAdmin.setReadOnly(True)
        self.radio_maleAdmin.setEnabled(False)
        self.radio_femaleAdmin.setEnabled(False)
        self.edit_addressAdmin.setReadOnly(True)
        self.edit_passwordAdmin.setReadOnly(True)
        self.edit_passwordAgainAdmin.setReadOnly(True)
        self.check_orders.setEnabled(False)
        self.check_addAdmin.setEnabled(False)
        self.check_editAdmin.setEnabled(False)
        self.check_editUser.setEnabled(False)
        self.check_addProduct.setEnabled(False)
        self.check_editProduct.setEnabled(False)
        self.editingAdminId = None

    def saveAdminInfo(self):
        if not self.permissions[2]:
            Warning("Sizda ushbu operatsiyani bajarish huquqi yo'q").exec()
            return

        permissions = [self.check_orders.isChecked(), self.check_addAdmin.isChecked(),
                       self.check_editAdmin.isChecked(), self.check_editUser.isChecked(),
                       self.check_addProduct.isChecked(), self.check_editProduct.isChecked()]

        if self.edit_nameAdmin.text() == "" or self.edit_surnameAdmin.text() == "" or \
                self.edit_phoneAdmin.text() == "" or self.edit_addressAdmin.toPlainText() == "" or \
                self.edit_usernameAdmin.text() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        elif self.edit_passwordAdmin.text() != self.edit_passwordAgainAdmin.text():
            Warning("Parollar mos emas").exec()
        else:
            if self.addingAdmin:
                if not checkUsername(self.edit_usernameAdmin.text()):
                    Warning("Ushbu Username band").exec()
                elif self.edit_passwordAdmin.text() == "" or self.edit_passwordAgainAdmin.text() == "":
                    Warning("Iltimos maydonlarni to'ldiring").exec()
                else:
                    addAdmin(self.edit_usernameAdmin.text(), self.edit_nameAdmin.text(),
                             self.edit_surnameAdmin.text(), self.edit_phoneAdmin.text(),
                             self.radio_maleAdmin.isChecked(), self.edit_addressAdmin.toPlainText(),
                             self.edit_passwordAdmin.text(), tuple(permissions))
                    adminId = getAdminid(self.edit_usernameAdmin.text(), self.edit_passwordAdmin.text())
                    saveImage(self.adminAvatar_src, f'data/data_avatar/admin/{adminId}.png')
                    Information("Admin qo'shildi").exec()
                    self.cancelAdminInfo()
                    self.loadAdmins()
            else:
                if not checkUsername(self.edit_usernameAdmin.text()) and \
                        self.edit_usernameAdmin.text() != getAdminInfo(self.editingAdminId)[0]:
                    Warning("Ushbu Username band").exec()
                else:
                    saveImage(self.adminAvatar_src, f'data/data_avatar/admin/{self.editingAdminId}.png')
                    updateAdminInfo(self.editingAdminId, self.edit_usernameAdmin.text(), self.edit_nameAdmin.text(),
                                    self.edit_surnameAdmin.text(), self.edit_phoneAdmin.text(),
                                    self.edit_addressAdmin.toPlainText(), self.radio_maleAdmin.isChecked(),
                                    tuple(permissions))
                    if self.edit_passwordAdmin.text() != "":
                        updateAdminPassword(self.editingAdminId, self.edit_passwordAdmin.text())
                    Information("Admin ma'lumotlari yangilandi").exec()
                    self.cancelAdminInfo()
                    self.loadAdmins()

    def updatePassword(self):
        Update_password(self.id, True).exec()

    # Tab Profile
    def editProfile(self):
        self.edit_usernameProfile.setReadOnly(False)
        self.edit_nameProfile.setReadOnly(False)
        self.edit_surnameProfile.setReadOnly(False)
        self.edit_phoneProfile.setReadOnly(False)
        self.edit_addressProfile.setReadOnly(False)
        self.radio_maleProfile.setEnabled(True)
        self.radio_femaleProfile.setEnabled(True)

    def cancelSetting(self):
        self.edit_nameProfile.setText(self.name)
        self.edit_surnameProfile.setText(self.surname)
        self.edit_phoneProfile.setText(self.phone)
        self.edit_addressProfile.setText(self.address)
        self.edit_usernameProfile.setText(self.username)
        self.updateAvatar(f'data/data_avatar/admin/{self.id}.png', self.avatarProfile)
        if self.male:
            self.radio_maleProfile.setChecked(True)
        else:
            self.radio_femaleProfile.setChecked(True)
        self.edit_nameProfile.setReadOnly(True)
        self.edit_surnameProfile.setReadOnly(True)
        self.edit_phoneProfile.setReadOnly(True)
        self.edit_addressProfile.setReadOnly(True)
        self.edit_usernameProfile.setReadOnly(True)
        self.radio_maleProfile.setEnabled(False)
        self.radio_femaleProfile.setEnabled(False)

    def saveSetting(self):
        if not self.change and self.edit_nameProfile.text() == self.name and \
                self.edit_surnameProfile.text() == self.surname and \
                self.edit_phoneProfile.text() == self.phone and \
                self.edit_addressProfile.toPlainText() == self.address and \
                self.edit_usernameProfile.text() == self.username:
            Warning("Profil ma'lumotlari o'zgartirilmagan").exec()
        elif not self.change or self.edit_nameProfile.text() == "" or \
                self.edit_surnameProfile.text() == "" or \
                self.edit_phoneProfile.text() == "" or \
                self.edit_addressProfile.toPlainText() == "" or \
                self.edit_usernameProfile.text() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        else:
            saveImage(self.avatar_src, f'data/data_avatar/admin/{self.id}.png')
            updateAdminInfo(self.id, self.edit_usernameProfile.text(), self.edit_nameProfile.text(),
                            self.edit_surnameProfile.text(), self.edit_phoneProfile.text(),
                            self.edit_addressProfile.toPlainText(), self.radio_maleProfile.isChecked())
            self.name = self.edit_nameProfile.text()
            self.surname = self.edit_surnameProfile.text()
            self.phone = self.edit_phoneProfile.text()
            self.address = self.edit_addressProfile.toPlainText()
            self.male = int(self.radio_maleProfile.isChecked())
            self.username = self.edit_usernameProfile.text()
            self.label_admin.setText(self.name + " " + self.surname)
            self.cancelSetting()
            Information("Profil ma'lumotlari yangilandi").exec()

    # Avatar
    def updateAvatar(self, path, profile=True):
        if profile:
            self.avatarProfile.setPixmap(self.load_img(path))
            self.change = True
            self.avatar_src = path
        else:
            self.avatarAdmin.setPixmap(self.load_img(path))
            self.adminAvatar_src = path

    def templateAvatar(self, profile=True):
        self.templateAvatarIndex = 0
        if profile:
            self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png', profile)
        else:
            self.updateAvatar(f'img/avatar/{str(int(self.radio_maleAdmin.isChecked()))}' + \
                              f'{str(self.templateAvatarIndex)}.png', profile)

    def nexttemplateAvatar(self, profile=True):
        self.templateAvatarIndex += 1
        self.templateAvatarIndex %= 17
        if profile:
            self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png', profile)
        else:
            self.updateAvatar(f'img/avatar/{str(int(self.radio_maleAdmin.isChecked()))}' + \
                              f'{str(self.templateAvatarIndex)}.png', profile)

    def previoustemplateAvatar(self, profile=True):
        self.templateAvatarIndex -= 1
        self.templateAvatarIndex %= 17
        if profile:
            self.updateAvatar(f'img/avatar/{str(self.male)}{str(self.templateAvatarIndex)}.png', profile)
        else:
            self.updateAvatar(f'img/avatar/{str(int(self.radio_maleAdmin.isChecked()))}' + \
                              f'{str(self.templateAvatarIndex)}.png', profile)

    # Window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def load_img(self, path):
        pixmap = QPixmap(path)
        return pixmap

    def resizeEvent(self, event):
        self.moveFlag = False
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        self.grip.move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        event.accept()

    def toClose(self):
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
