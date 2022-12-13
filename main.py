from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from design import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()