# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 800))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QStatusBar{\n"
"border: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1301, 40))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"}\n"
"QFrame{\n"
"\n"
"border-radius:none;\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.9);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:silver;\n"
"background:transparent;")
        self.label_2.setObjectName("label_2")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setGeometry(QtCore.QRect(1261, 0, 41, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"color:silver;\n"
"\n"
"border-radius:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:red;\n"
"color:white\n"
"}")
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_2)
        self.btn_minimize.setGeometry(QtCore.QRect(1220, 0, 41, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"border-radius:none;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(0, 0, 0,0.6)\n"
"}")
        self.btn_minimize.setObjectName("btn_minimize")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(321, 40, 981, 763))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QWidget{\n"
"background-image: url(:/images/img/back_1.jpg);\n"
"}\n"
"QWidget{\n"
"  font-size: 20px;\n"
"  font-weight: 600;\n"
"  color: transparent;\n"
"  background-clip: text;\n"
"  border: none;\n"
"  -webkit-background-clip: text;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"\n"
" }\n"
"QTabBar::tab{\n"
" width: 225px;\n"
"  background: rgba(0,0,0,0.6);\n"
"  color: white;\n"
"  padding: 10px;\n"
"}\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
" \n"
"background: rgba(195,63,11,0.6);\n"
" }\n"
" QTabBar::tab:hover {\n"
"   background: rgba(82,120,21, 0.7);\n"
" }\n"
"QFrame{\n"
"    background: rgba(0,0,0,0.6);\n"
"}\n"
"QFrame:hover{\n"
"    background: rgba(0,0,0,0.7);\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_products = QtWidgets.QWidget()
        self.tab_products.setObjectName("tab_products")
        self.frame = QtWidgets.QFrame(self.tab_products)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1301, 721))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab_products, "")
        self.tab_users = QtWidgets.QWidget()
        self.tab_users.setObjectName("tab_users")
        self.frame_3 = QtWidgets.QFrame(self.tab_users)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1301, 721))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tabWidget.addTab(self.tab_users, "")
        self.tab_admin = QtWidgets.QWidget()
        self.tab_admin.setObjectName("tab_admin")
        self.frame_4 = QtWidgets.QFrame(self.tab_admin)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1301, 721))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tabWidget.addTab(self.tab_admin, "")
        self.tab_profil = QtWidgets.QWidget()
        self.tab_profil.setObjectName("tab_profil")
        self.frame_5 = QtWidgets.QFrame(self.tab_profil)
        self.frame_5.setGeometry(QtCore.QRect(-40, 0, 1341, 721))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.tabWidget.addTab(self.tab_profil, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 325, 761))
        self.tabWidget_2.setStyleSheet("QWidget{\n"
"background-image: url(:/images/img/list_back.jpg);\n"
"}\n"
"QWidget{\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  color: transparent;\n"
"  background-clip: text;\n"
"  border: none;\n"
"  -webkit-background-clip: text;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"\n"
" }\n"
"QTabBar::tab{\n"
" width: 142px;\n"
"  background: rgba(0,0,0,0.6);\n"
"  color: white;\n"
"  padding: 10px;\n"
"}\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
" \n"
"background: rgba(195,63,11,0.6);\n"
" }\n"
" QTabBar::tab:hover {\n"
"   background: rgba(82,120,21, 0.7);\n"
" }\n"
"QFrame{\n"
"    background: rgba(0,0,0,0.6);\n"
"  filter: blur(8px);\n"
"  -webkit-filter: blur(8px);\n"
"}\n"
"QFrame:hover{\n"
"    background: rgba(0,0,0,0.7);\n"
"}\n"
"")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 321, 731))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 321, 731))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tabWidget_2.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Asosiy"))
        self.btn_close.setText(_translate("MainWindow", "✕"))
        self.btn_minimize.setText(_translate("MainWindow", "_"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_products), _translate("MainWindow", "Ovqatlar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_users), _translate("MainWindow", "Salatlar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_admin), _translate("MainWindow", "Shirinliklar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profil), _translate("MainWindow", "Ichimliklar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Xarid"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Profil"))
import images_rc
