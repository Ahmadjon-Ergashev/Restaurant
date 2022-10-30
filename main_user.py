from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QLabel, QHBoxLayout, QSystemTrayIcon
from PyQt5.QtCore import QPoint, Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from functools import partial
import sys
import ctypes
from design.Ui_main_user import Ui_Asosiy
from classes.warning import Warning
from classes.confirm import Confirm
from classes.information import Information
from classes.image import saveImage
from classes.update_password import Update_password
from classes.login import Login
from classes.sql import *

class Main_user(QMainWindow, Ui_Asosiy):
    def __init__(self):
        login = Login()
        login.exec()
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.to_close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btnCancel_2.clicked.connect(self.cancel_setting)
        self.btnCancel.clicked.connect(lambda: self.clear_order())
        self.btnOk_2.clicked.connect(self.save_setting)
        self.btn_updatepassword.clicked.connect(self.updatePassword)
        self.btnOk.clicked.connect(self.add_order)
        self.check_1.clicked.connect(self.load_history)
        self.check_2.clicked.connect(self.load_history)
        self.check_3.clicked.connect(self.load_history)
        self.check_4.clicked.connect(self.load_history)

        if login.login is None:
            sys.exit()
        self.id = login.userid
        self.name, self.surname, self.phone, self.address, self.male = getUserInfo(login.userid)
        self.label_user.setText(self.name + " " + self.surname)

        self.change = False
        self.avatar_src = f'data/data_avatar/user/{self.id}.png'
        self.templateAvatarIndex = 0

        self.btn_remove.clicked.connect(partial(self.updateAvatar, 'img/avatar/avatar.png'))
        self.btn_template.clicked.connect(self.templateAvatar)
        self.btn_next.clicked.connect(self.nexttemplateAvatar)
        self.btn_previous.clicked.connect(self.previoustemplateAvatar)
        # self.btn_edit.clicked.connect(self.edit_profile)
        self.btn_updatepassword.clicked.connect(self.updatePassword)

        self.orders = dict()
        self.cancel_setting()
        self.load(self.grid_Foods, products("Ovqatlar"))
        self.load(self.grid_Salads, products("Salatlar"))
        self.load(self.grid_Sweets, products("Shirinliklar"))
        self.load(self.grid_Drinks, products("Ichimliklar"))

        self.load_history()

        if self.address is None:
            Warning("Iltimos buyurtma berish uchun manzilingizni kiriting").exec()


    def load(self, layout, result):
        x = 0
        y = 0
        for data in result:
            label_photo = QLabel()
            label_photo.setPixmap(self.load_img(data[4]))
            label_photo.setMinimumSize(200, 200)
            label_photo.setMaximumSize(200, 200)
            button_add = QPushButton("Qo'shish")
            # button_add.setObjectName("b_"+str(data[0]))
            button_add.clicked.connect(partial(self.add, data[0]))
            button_add.setMinimumSize(200, 30)
            button_add.setMaximumSize(200, 30)
            label_name = QLabel(data[2])
            label_name.setMinimumSize(200, 30)
            label_name.setMaximumSize(200, 150)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setWordWrap(True)
            label_price = QLabel(self.formatPrice(data[3]) + " so'm")
            label_price.setMinimumSize(200, 30)
            label_price.setMaximumSize(200, 150)
            label_price.setAlignment(Qt.AlignCenter)
            layout.addWidget(label_photo, x, y)
            layout.addWidget(label_name, x + 1, y)
            layout.addWidget(label_price, x + 2, y)
            layout.addWidget(button_add, x + 3, y)

            if y == 3:
                y = 0
                x += 4
            else:
                y += 1

    def load_history(self):
        while self.formHistory.rowCount():
            self.formHistory.removeRow(0)

        result = getOrderHistory(self.id, self.check_1.isChecked(), self.check_2.isChecked(), self.check_3.isChecked(), self.check_4.isChecked())
        for order in result:
            layout = QHBoxLayout()

            label_date = QLabel(order[2][:16])
            label_date.setAlignment(Qt.AlignCenter)

            label_status = QLabel(order[3])
            label_status.setAlignment(Qt.AlignCenter)
            label_status.setMinimumSize(120, 35)
            label_status.setMaximumSize(120, 35)
            style = "QLabel{\n"
            if order[3] == "Yuborilgan":
                style += "color: rgb(107,196,237);\n"
            elif order[3] == "Yo'lda":
                style += "color: rgb(230,181,237);\n"
            elif order[3] == "Qabul qilingan":
                style += "color: rgb(163,237,179);\n"
            else:
                style += "color: rgb(237,121,142);\n"
            style += "}"
            label_status.setStyleSheet(style)
            button_more = QPushButton("")
            button_more.setStyleSheet("QPushButton:hover{\n"
                                      "background: rgba(0,0,0, 0.5);\n"
                                      "}")
            icon3 = QIcon()
            icon3.addPixmap(QPixmap(":/images/img/eye.png"), QIcon.Normal, QIcon.Off)
            button_more.setIcon(icon3)
            button_more.setIconSize(QSize(25, 25))
            button_more.setToolTip("Batafsil")
            button_more.setMinimumSize(35, 35)
            button_more.setMaximumSize(35, 35)

            layout.addWidget(label_date)
            layout.addWidget(label_status)
            layout.addWidget(button_more)
            self.formHistory.addRow(layout)

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

    def updatePassword(self):
        Update_password(self.id, False)

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
            self.updateAvatar(f'data/data_avatar/user/{self.id}.png')
        else:
            self.edit_name.setReadOnly(False)
            self.edit_surname.setReadOnly(False)
            self.edit_phone.setReadOnly(False)
            self.edit_address.setReadOnly(False)
            self.btnCancel_2.setText("Bekor qilish")


    def save_setting(self):
        if not self.change and self.edit_name.text() == self.name and self.edit_surname.text() == self.surname and \
                self.edit_phone.text() == self.phone and self.edit_address.toPlainText() == self.address:
            Warning("Profil ma'lumotlari o'zgartirilmagan").exec()
        elif not self.change and self.edit_name.text() == "" or self.edit_surname.text() == "" or \
                self.edit_phone.text() == "" or self.edit_address.toPlainText() == "":
            Warning("Iltimos maydonlarni to'ldiring").exec()
        else:
            saveImage(self.avatar_src, f'data/data_avatar/user/{self.id}.png')
            updateUserInfo(self.id, self.edit_name.text(), self.edit_surname.text(),
                           self.edit_phone.text(), self.edit_address.toPlainText(), self.male)
            self.name = self.edit_name.text()
            self.surname = self.edit_surname.text()
            self.phone = self.edit_phone.text()
            self.address = self.edit_address.toPlainText()
            self.label_user.setText(self.name + " " + self.surname)
            self.edit_name.setReadOnly(True)
            self.edit_surname.setReadOnly(True)
            self.edit_phone.setReadOnly(True)
            self.btnCancel_2.setText("Taxrirlash")
            Information("Profil ma'lumotlari yangilandi").exec()


    def load_img(self, path):
        pixmap = QPixmap(path)
        return pixmap

    def clear_order(self, confirm=True):
        if confirm is False:
            self.orders = dict()
            self.counting()
            while self.formLayout.rowCount():
                self.formLayout.removeRow(0)
            return
        confirm = Confirm("Buyurtmalarni bekor qilishni xohlaysizmi?")
        confirm.exec()
        if confirm.confirmation:
            self.orders = dict()
            self.counting()
            while self.formLayout.rowCount():
                self.formLayout.removeRow(0)

    def counting(self):
        count = 0
        sum = 0
        for product in self.orders.values():
            count += product["count"]
            sum += product["count"] * product["price"]

        self.label_count.setText(str(count))
        self.label_sum.setText(self.formatPrice(sum) + " so'm")

    def toobject(self, product):
        return {"price": product[3],
                "count": 1}

    def add(self, id):
        # for i in range(self.formLayout.rowCount()):
        #     if text == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(0).widget().text():
        #         self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) + 1))
        #         self.orders[id]["count"] += 1
        #         self.counting()
        #         return
        label = self.findChild(QLabel, "count_" + str(id))
        if label:
            self.incCount(id)
            self.orders[id]["count"] += 1
            self.counting()
            return
        object = getproductByID(id)[0]
        text = object[2]
        temp = self.toobject(object)

        self.orders[id] = temp
        self.counting()
        layout = QHBoxLayout()
        label_name = QLabel(text)
        label_name.setAlignment(Qt.AlignCenter)

        button_plus = QPushButton("+", clicked=partial(self.incCount, id))
        # button_plus.setObjectName("inc_" + str(id))
        button_plus.setStyleSheet("QPushButton:hover{\n"
                                    "background: rgba(82,120,21, 0.7);\n"
                                    "}")
        button_plus.setMinimumSize(35, 35)
        button_plus.setMaximumSize(35, 35)

        button_minus = QPushButton("-", clicked=partial(self.decCount, id))
        # button_minus.setObjectName("dec_"+str(id))
        button_minus.setStyleSheet("QPushButton:hover{\n"
                                    "background: rgba(195,63,11,0.6);\n"
                                    "}")
        button_minus.setMinimumSize(35, 35)
        button_minus.setMaximumSize(35, 35)

        label_count = QLabel("1")
        label_count.setObjectName("count_"+str(id))
        label_count.setAlignment(Qt.AlignCenter)
        label_count.setMinimumSize(35, 35)
        label_count.setMaximumSize(35, 35)

        button_remove = QPushButton("✕", clicked=partial(self.delete, id))
        # button_remove.setObjectName("del_" + str(id))
        button_remove.setStyleSheet("QPushButton:hover{\n"
                                    "background:red;\n"
                                    "color:white\n"
                                    "}")
        button_remove.setMinimumSize(35, 35)
        button_remove.setMaximumSize(35, 35)
        button_remove.height = 50

        layout.addWidget(label_name)
        layout.addWidget(button_minus)
        layout.addWidget(label_count)
        layout.addWidget(button_plus)
        layout.addWidget(button_remove)
        self.formLayout.addRow(layout)

    def delete(self, id):
        # id = int(self.sender().objectName()[4:])
        for i in range(self.formLayout.rowCount()):
            if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(4).widget():
                self.formLayout.removeRow(i)
                del self.orders[id]
                self.counting()
                return

    def incCount(self, id):
        label = self.findChild(QLabel, "count_"+str(id))
        label.setText(str(int(label.text())+1))
        self.orders[id]["count"] += 1
        self.counting()

    def decCount(self, id):
        # id = int(self.sender().objectName()[4:])
        label = self.findChild(QLabel, "count_" + str(id))
        if label.text() != "1":
            label.setText(str(int(label.text()) - 1))
            self.orders[id]["count"] -= 1
            self.counting()

    def formatPrice(self, price):
        text = str(price)[::-1]
        result = ""
        while text:
            result += text[:3] + " "
            text = text[3:]
        return result[len(result)-2::-1]

    def add_order(self):
        confirm = Confirm("Buyurtmalarni jo'natishni xohlaysizmi?")
        confirm.exec()
        if confirm.confirmation:
            addorder(self.id, self.orders)
            self.clear_order(False)
            self.load_history()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
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

