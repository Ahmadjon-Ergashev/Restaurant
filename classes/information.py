from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QPoint, Qt
import sys

from design.Ui_Information import Ui_information

class Information(QDialog, Ui_information):
    def __init__(self, info_msg):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.close)
        self.info_msg = info_msg
        self.txt_error.setPlainText(self.info_msg)

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
    win = Information("Deneme")
    win.show()
    sys.exit(app.exec())