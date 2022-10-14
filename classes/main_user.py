from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QPoint, Qt
import sys

from design.Ui_main_user import Ui_MainWindow

class Main_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)


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