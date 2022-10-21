from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QGroupBox, QLabel, QScrollArea, QHBoxLayout, QFrame, QVBoxLayout, QLayout
from PyQt5.QtCore import QPoint, Qt
import sys

from design.Ui_main_user import Ui_MainWindow
from classes.login import Login

class Main_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        login = Login()
        login.exec_()
        super(Main_user, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        # label = []
        # button = []
        # formLayout = QFormLayout()
        # groupBox = QGroupBox()
        # groupBox.setStyleSheet('QLabel{background: transparent; font: 14pt "MS Shell Dlg 2"; color: black;}')
        #
        # for i in range(10):
        #     label.append(QLabel("label"))
        #     button.append(QPushButton("Button", clicked = self.delete))
        #     formLayout.addRow(label[i], button[i])
        # button[0].
        # groupBox.setLayout(formLayout)
        # scrool = QScrollArea()
        # scrool.setWidget(groupBox)
        # scrool.setWidgetResizable(True)
        # # scrool.setFixedHeight(400)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(scrool)
        # self.frame_7.setLayout(layout)
        # self.verticalLayout.addStretch()

        # group = QGroupBox()
        # self.layout = QVBoxLayout()
        # self.layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        # self.layout.setSpacing(0)
        # group.setLayout(self.layout)
        # scroll = QScrollArea()
        # scroll.setWidget(group)
        # scroll.setWidgetResizable(True)

        # self.verticalLayout.addWidget(scroll)
        self.pushButton.clicked.connect(self.add)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def add(self):
        group = QFrame()
        layout = QHBoxLayout()
        group.setLayout(layout)
        layout.addWidget(QPushButton("hello"))
        layout.addWidget(QLabel("label"))
        # layout.addWidget(group)
        self.verticalLayout_2.addWidget(group)
        # self.verticalLayout_2.addWidget(QFrame())
        # self.verticalLayout_2.addWidget(QFrame())
        # self.verticalLayout_2.addWidget(QFrame())

    def delete(self):
        sender = self.sender()
        sender.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main_user()
    win.show()
    sys.exit(app.exec_())