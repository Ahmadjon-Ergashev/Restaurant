from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QPoint, Qt
import sys

from design.Ui_Confirmation import Ui_Confirmation

class Confirm(QDialog, Ui_Confirmation):
    def __init__(self, confirm_msg):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.click_ok)
        self.btn_cancel.clicked.connect(self.click_cancel)
        self.confirm_msg = confirm_msg
        self.txt_confirm.setPlainText(self.confirm_msg)
        self.confirmation = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def click_ok(self):
        self.confirmation = True
        self.close()

    def click_cancel(self):
        self.confirmation = False
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Warning("Deneme")
    win.show()
    sys.exit(app.exec())