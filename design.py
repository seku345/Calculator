# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(322, 274)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.app_name.setObjectName("app_name")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(10, 45, 301, 31))
        self.score.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: black;\n"
"")
        self.score.setObjectName("score")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(1, 178, 75, 23))
        self.button_1.setObjectName("button_1")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(1, 207, 75, 23))
        self.button_equal.setObjectName("button_equal")
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setGeometry(QtCore.QRect(163, 91, 75, 23))
        self.button_div.setObjectName("button_div")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(1, 149, 75, 23))
        self.button_4.setObjectName("button_4")
        self.button_prcnt = QtWidgets.QPushButton(self.centralwidget)
        self.button_prcnt.setGeometry(QtCore.QRect(1, 91, 75, 23))
        self.button_prcnt.setObjectName("button_prcnt")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(244, 149, 75, 23))
        self.button_plus.setObjectName("button_plus")
        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.button_sqrt.setGeometry(QtCore.QRect(82, 91, 75, 23))
        self.button_sqrt.setObjectName("button_sqrt")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(163, 120, 75, 23))
        self.button_9.setObjectName("button_9")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(163, 149, 75, 23))
        self.button_6.setAutoDefault(False)
        self.button_6.setObjectName("button_6")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(82, 207, 75, 23))
        self.button_0.setObjectName("button_0")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setEnabled(True)
        self.button_clear.setGeometry(QtCore.QRect(244, 178, 75, 52))
        self.button_clear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_clear.setObjectName("button_clear")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(82, 178, 75, 23))
        self.button_2.setObjectName("button_2")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(1, 120, 75, 23))
        self.button_7.setObjectName("button_7")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(163, 178, 75, 23))
        self.button_3.setObjectName("button_3")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.button_dot.setGeometry(QtCore.QRect(163, 207, 75, 23))
        self.button_dot.setObjectName("button_dot")
        self.button_prod = QtWidgets.QPushButton(self.centralwidget)
        self.button_prod.setGeometry(QtCore.QRect(244, 91, 75, 23))
        self.button_prod.setObjectName("button_prod")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(244, 120, 75, 23))
        self.button_minus.setObjectName("button_minus")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(82, 120, 75, 23))
        self.button_8.setObjectName("button_8")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(82, 149, 75, 23))
        self.button_5.setObjectName("button_5")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.app_name.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Calculator</span></p></body></html>"))
        self.score.setText(_translate("Calculator", "<html>\n"
"<head>\n"
"    <style>\n"
"    p {\n"
"    border: 1px solid black;\n"
"    padding: 10px;\n"
"    }\n"
"    </style>\n"
"</head>\n"
"<body>\n"
"    <p align=\"right\">\n"
"    <span style=\" font-size:20pt;\">0</span>\n"
"    </p>\n"
"</body>\n"
"</html>"))
        self.button_1.setText(_translate("Calculator", "1"))
        self.button_equal.setText(_translate("Calculator", "="))
        self.button_div.setText(_translate("Calculator", "/"))
        self.button_4.setText(_translate("Calculator", "4"))
        self.button_prcnt.setText(_translate("Calculator", "%"))
        self.button_plus.setText(_translate("Calculator", "+"))
        self.button_sqrt.setText(_translate("Calculator", "√"))
        self.button_9.setText(_translate("Calculator", "9"))
        self.button_6.setText(_translate("Calculator", "6"))
        self.button_0.setText(_translate("Calculator", "0"))
        self.button_clear.setText(_translate("Calculator", "C"))
        self.button_2.setText(_translate("Calculator", "2"))
        self.button_7.setText(_translate("Calculator", "7"))
        self.button_3.setText(_translate("Calculator", "3"))
        self.button_dot.setText(_translate("Calculator", "."))
        self.button_prod.setText(_translate("Calculator", "*"))
        self.button_minus.setText(_translate("Calculator", "-"))
        self.button_8.setText(_translate("Calculator", "8"))
        self.button_5.setText(_translate("Calculator", "5"))
