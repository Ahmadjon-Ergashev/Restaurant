from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QPoint, Qt
import sys
import pickle as pc

from design.Ui_Registration import Ui_Registration
from classes.warning import Warning

class Registration(QDialog, Ui_Registration):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_createAccount_2.clicked.connect(self.createAccount)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def createAccount(self):
        if len(self.phone_2.text()) < 18 or len(self.name_2.text()) < 3 or len(self.surname_2.text()) < 3 or \
                len(self.password_2.text()) < 6 or len(self.password_3.text()) < 6:
            Warning("Iltimos maydonlarni to'ldiring").exec()
        elif self.password_2.text() != self.password_3.text():
            Warning("Iltimos parollarni tekshiring").exec()

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
    app=QApplication(sys.argv)
    win=Registration()
    win.show()
    sys.exit(app.exec())