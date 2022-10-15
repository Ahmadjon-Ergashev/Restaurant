# from classes.login import Login
from main_user import Main_user
# class Main(QDialog):
#     def __init__(self):
#         super().__init__()
#         login = Login()
#         login.exec()
#         # self.setupUi(self)
#         # self.btn_close.clicked.connect(self.close)
#         # self.btn_minimize.clicked.connect(self.showMinimized)
#         # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#         # self.setWindowFlag(Qt.FramelessWindowHint)
#         # self.setAttribute(Qt.WA_TranslucentBackground)
#         # self.btn_newAccount.clicked.connect(self.newAccount)
#
#         # self.setWindowOpacity(0.6)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.moveFlag = True
#             self.movePosition = event.globalPos() - self.pos()
#             event.accept()
#
#     def mouseMoveEvent(self, event):
#         if Qt.LeftButton and self.moveFlag:
#             self.move(event.globalPos() - self.movePosition)
#             event.accept()

if __name__=="__main__":
    # app=QApplication(sys.argv)
    # win=Main()
    # win.show()
    # sys.exit(app.exec_())
    main = Main_user()
