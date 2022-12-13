import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from design import Ui_Calculator


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        
        self.ui.button_0.released.connect(self.clicked)
        self.ui.button_1.released.connect(self.clicked)
        self.ui.button_2.released.connect(self.clicked)
        self.ui.button_3.released.connect(self.clicked)
        self.ui.button_4.released.connect(self.clicked)
        self.ui.button_5.released.connect(self.clicked)
        self.ui.button_6.released.connect(self.clicked)
        self.ui.button_7.released.connect(self.clicked)
        self.ui.button_8.released.connect(self.clicked)
        self.ui.button_9.released.connect(self.clicked)
        self.ui.button_plus.released.connect(self.clicked)
        self.ui.button_minus.released.connect(self.clicked)
        self.ui.button_dot.released.connect(self.clicked)
        self.ui.button_prod.released.connect(self.clicked)
        self.ui.button_div.released.connect(self.clicked)
        self.ui.button_sqrt.released.connect(self.clicked)
        self.ui.button_prcnt.released.connect(self.clicked)
        self.ui.button_clear.released.connect(self.clicked)
        self.ui.button_equal.released.connect(self.clicked)
        
        self.current_score = '0'
        self.active_button = None
        self.score_html_before = '<html><head><style>p {border: 1px solid black;padding: 10px;}</style></head><body><p align=\"right\"><span style=\" font-size:20pt;\">'
        self.score_html_after = "</span></p></body></html>"
        
    def clicked(self):
        button_name = self.sender()
        self.active_button = button_name.objectName()
        match self.active_button[7:]:
            case '0':
                print('I am a zero!')
                self.current_score += '1'
            case '1':
                ...
            case '2':
                ...
            case '3':
                ...
            case '4':
                ...
            case '5':
                ...
            case '6':
                ...
            case '7':
                ...
            case '8':
                ...
            case '9':
                ...
            case 'plus':
                ...
            case 'minus':
                ...
            case 'prod':
                ...
            case 'div':
                ...
            case 'sqrt':
                ...
            case 'dot':
                ...
            case 'prcnt':
                ...
            case 'clear':
                ...
            case 'equal':
                ...
        self.ui.score.setText(f'{self.current_score}')
        
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