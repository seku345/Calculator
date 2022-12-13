from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from design import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())