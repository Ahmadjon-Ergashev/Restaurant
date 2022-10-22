from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPixmap
import sys

from design.Ui_main_user import Ui_MainWindow
from classes.login import Login
from classes.sql import *

class Main_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        login = Login()
        login.exec_()
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        self.orders = dict()

        self.load(self.grid_Foods, products("Ovqatlar"))
        self.load(self.grid_Salads, products("Salatlar"))
        self.load(self.grid_Sweets, products("Shirinliklar"))
        self.load(self.grid_Drinks, products("Ichimliklar"))
        self.btnCancel.clicked.connect(self.cancel)

    def load(self, layout, result):
        x = 0
        y = 0
        for data in result:
            label_photo = QLabel()
            label_photo.setPixmap(self.load_img(data[4]))
            label_photo.setMinimumSize(200, 200)
            label_photo.setMaximumSize(200, 200)
            button_add = QPushButton("Qo'shish")
            button_add.setObjectName("b_"+str(data[0]))
            button_add.clicked.connect(self.add)
            button_add.setMinimumSize(200, 30)
            button_add.setMaximumSize(200, 30)
            label_name = QLabel(data[2])
            label_name.setMinimumSize(200, 30)
            label_name.setMaximumSize(200, 150)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setWordWrap(True)
            label_price = QLabel(str(data[3]))
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

    def load_img(self, path):
        pixmap = QPixmap(path)
        return pixmap

    def cancel(self):
        while self.formLayout.rowCount():
            self.formLayout.removeRow(0)

    def counting(self):
        count = 0
        sum = 0
        for product in self.orders.values():
            count += product["count"]
            sum += product["count"] * product["price"]

        self.label_count.setText(str(count))
        self.label_sum.setText(str(sum))


    def toobject(self, product):
        return {"price": product[3],
                "count": 1}

    def add(self):
        id = int(self.sender().objectName()[2:])
        object = get_productByID(id)[0]
        text = object[2]
        temp = self.toobject(object)
        for i in range(self.formLayout.rowCount()):
            if text == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(0).widget().text():
                self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) + 1))
                self.orders[id]["count"] += 1
                self.counting()
                return
        self.orders[id] = temp
        self.counting()
        layout = QHBoxLayout()
        label_name = QLabel(text)
        label_name.setAlignment(Qt.AlignCenter)

        button_plus = QPushButton("+", clicked=self.incCount)
        button_plus.setObjectName("inc_" + str(id))
        button_plus.setStyleSheet("QPushButton:hover{\n"
                                    "background: rgba(82,120,21, 0.7);\n"
                                    "}")
        button_plus.setMinimumSize(35, 35)
        button_plus.setMaximumSize(35, 35)

        button_minus = QPushButton("-", clicked=self.decCount)
        button_minus.setObjectName("dec_"+str(id))
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

        button_remove = QPushButton("✕", clicked=self.delete)
        button_remove.setObjectName("del_" + str(id))
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

    def delete(self):
        id = int(self.sender().objectName()[4:])
        for i in range(self.formLayout.rowCount()):
            if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(4).widget():
                self.formLayout.removeRow(i)
                del self.orders[id]
                self.counting()
                return

    def incCount(self):
        id = int(self.sender().objectName()[4:])
        # print(id)
        # for i in range(self.formLayout.rowCount()):
        #     if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(3).widget():
        #         print(self.orders[id])
        #         self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) + 1))
        #
        #
        #
        label = self.findChild(QLabel, "count_"+str(id))
        label.setText(str(int(label.text())+1))
        self.orders[id]["count"] += 1
        self.counting()

    def decCount(self):
        id = int(self.sender().objectName()[4:])
        label = self.findChild(QLabel, "count_" + str(id))
        if label.text() != "1":
            label.setText(str(int(label.text()) - 1))
            self.orders[id]["count"] -= 1
            self.counting()
        # for i in range(self.formLayout.rowCount()):
        #     if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(1).widget():
        #         if self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text() != "1":
        #             self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) - 1))
        #             self.orders[id]["count"] -= 1
        #             self.counting()

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
    win = Main_user()
    win.show()
    sys.exit(app.exec_())
