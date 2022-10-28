from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QPoint, Qt
import sys


from design.Ui_Update_password import Ui_UpdatePassword
from classes.warning import Warning
from classes.information import Information
from classes.sql import updatePassword, updateAdminPassword, checkPassword, checkAdminPassword

class Update_password(QDialog, Ui_UpdatePassword):
    def __init__(self, id, admin):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.id = id
        if admin:
            self.btn_updatepassword.clicked.connect(self.updateAdminPassword)
        else:
            self.btn_updatepassword.clicked.connect(self.updatePassword)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def updatePassword(self):
        if (checkPassword(self.id, self.old_password.text())) is False:
            Warning("Eski parol xato kiritildi").exec()
        elif len(self.password_1.text()) < 6:
            Warning("Yangi parol 6 yoki undan ortiq belgidan iborat bo'lishi lozim").exec()
        elif self.password_1.text() != self.password_2.text():
            Warning("Yangi parol tasdiqlanmadi").exec()
        else:
            updatePassword(self.id, self.password_1.text())
            self.old_password.clear()
            self.password_1.clear()
            self.password_2.clear()
            Information("Parol Yangilandi").exec()
        self.close()

    def updateAdminPassword(self):
        if (checkAdminPassword(self.id, self.old_password.text())) is False:
            Warning("Eski parol xato kiritildi").exec()
        elif len(self.password_1.text()) < 6:
            Warning("Yangi parol 6 yoki undan ortiq belgidan iborat bo'lishi lozim").exec()
        elif self.password_1.text() != self.password_2.text():
            Warning("Yangi parol tasdiqlanmadi").exec()
        else:
            updateAdminPassword(self.id, self.password_1.text())
            self.old_password.clear()
            self.password_1.clear()
            self.password_2.clear()
            Information("Parol Yangilandi").exec()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Update_password("Deneme")
    win.show()
    sys.exit(app.exec())