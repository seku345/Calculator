from PyQt5 import QtWidgets, QtGui
from test_2 import Ui_MainWindow
import sys
print(5)
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)