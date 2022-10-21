from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFormLayout, QGroupBox, QLabel, QScrollArea, QHBoxLayout, QFrame, QVBoxLayout, QLayout
from PyQt5.QtCore import QPoint, Qt, pyqtSlot
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
        # layout_2 = QVBoxLayout(self.frame_10)
        # layout_2.addWidget(scroll)
        # self.scrollArea.setWidget(group)

        self.pushButton.clicked.connect(lambda: self.add("tekshiruv"))


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def add(self, text):
        # group = QFrame()
        #
        # group.setLayout(layout)
        # layout.addWidget(QPushButton("hello"))
        # layout.addWidget(QLabel("label"))
        # # layout.addWidget(group)
        # self.layout.addWidget(group)
        # self.verticalLayout_2.addWidget(QFrame())
        # self.verticalLayout_2.addWidget(QFrame())
        # self.verticalLayout_2.addWidget(QFrame())
        layout = QHBoxLayout()
        label_name = QLabel(text)
        label_name.setAlignment(Qt.AlignCenter)
        button_plus = QPushButton("+", clicked = self.incCount)
        button_plus.setStyleSheet("QPushButton:hover{\n"
                                    "background: rgba(82,120,21, 0.7);\n"
                                    "}")
        button_plus.setMinimumSize(35, 35)
        button_plus.setMaximumSize(35, 35)
        button_minus = QPushButton("-", clicked = self.decCount)
        button_minus.setStyleSheet("QPushButton:hover{\n"
                                    "background: rgba(195,63,11,0.6);\n"
                                    "}")
        button_minus.setMinimumSize(35, 35)
        button_minus.setMaximumSize(35, 35)
        label_count = QLabel("1")
        label_count.setAlignment(Qt.AlignCenter)
        label_count.setMinimumSize(35, 35)
        label_count.setMaximumSize(35, 35)

        button_remove = QPushButton("✕", clicked=self.delete)
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
        for i in range(self.formLayout.rowCount()):
            if self.sender()== self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(4).widget():
                self.formLayout.removeRow(i)
                return

    def incCount(self):
        for i in range(self.formLayout.rowCount()):
            if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(3).widget():
                self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) + 1))

    def decCount(self):
        for i in range(self.formLayout.rowCount()):
            if self.sender() == self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(1).widget():
                if self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text() != "1":
                    self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().setText(str(int(self.formLayout.itemAt(i, QFormLayout.FieldRole).itemAt(2).widget().text()) - 1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main_user()
    win.show()
    sys.exit(app.exec_())