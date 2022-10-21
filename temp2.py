import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt

class Window(QWidget):
    layout = QVBoxLayout()
    def __init__(self):
        super().__init__()
        self.resize(700, 500)
        self.widget = QFrame(self)
        self.widget.setStyleSheet("QFrame{background: rgba(0,0,0,0.3);}")
        self.widget.objectName="widget"
        self.widget.setGeometry(0,0, 300, 300)
        self.widget.setFrameShape(QFrame.StyledPanel)
        self.widget.setFrameShadow(QFrame.Raised)
        self.button = QPushButton("Tikla", self.widget)
        self.button.layoutDirection()
        self.button.setGeometry(10, 50, 200, 75)
        self.button.clicked.connect(self.delete)

        # self.setLayout(self.layout)
        # edits = {}
        # edits['n1'] = QPushButton("Hello")
        # edits['n1'].clicked.connect(self.add)
        # # edits['n2'] = QPushButton("n1", clicked=self.add)
        # # edits['n3'] = QPushButton("n2", clicked=self.add)
        # # edits['n4'] = QPushButton("n3", clicked=self.add)
        # # edits['n5'] = QPushButton("n4", clicked=self.add)
        # # edits['n6'] = QPushButton("n5", clicked=self.add)
        # # edits['n1'].deleteLater()
        # for item in edits.values():
        #     self.layout.addWidget(item)

    def add(self):
        widget = QWidget()
        widget.set
        self.layout.addWidget(QPushButton("Delete", clicked=self.delete))

    def delete(self):
        sender = self.sender()
        sender.parent().deleteLater()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())