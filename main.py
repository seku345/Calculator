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
        
        self.equation = '0'
        self.last_sign = None
        self.was_num = True
        self.current_score = '0'
        self.active_button = None
        self.score_html_before = '<html><head><style>p {border: 1px solid black;padding: 10px;}</style></head><body><p align=\"right\"><span style=\" font-size:19pt;\">'
        self.score_html_after = "</span></p></body></html>"
    

    
    def clicked(self):
    
        def checking_num(score, digit: str) -> str:
            if len(score) < 18:
                if score == '0':
                    score = digit
                else:
                    score += digit
            return score
    
        button_name = self.sender()
        self.active_button = button_name.objectName()
        match self.active_button[7:]:
            case '0':
                if self.current_score[0] != '0' and len(self.current_score) < 18:
                    self.current_score += '0'
                    if not self.was_num:
                        self.equation += self.last_sign
                        self.current_score = '0'
                    self.was_num = True
            case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' as digit:
                self.current_score = checking_num(self.current_score, digit)
                if not self.was_num:
                    self.equation += self.last_sign
                    self.current_score = digit
                self.was_num = True
            case 'plus':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '+'
                self.was_num = False
                self.current_score = self.last_sign
            case 'minus':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '-'
                self.was_num = False
                self.current_score = self.last_sign
            case 'prod':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '*'
                self.was_num = False
                self.current_score = self.last_sign
            case 'div':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '/'
                self.was_num = False
                self.current_score = self.last_sign
            case 'sqrt':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '???'
                self.was_num = False
                self.current_score = str(eval(self.current_score)**0.5)
                self.equation = self.current_score
            case 'dot':
                if self.current_score.count('.') < 1 and self.was_num:
                    self.current_score += '.'
            case 'prcnt':
                if self.was_num:
                    self.equation += self.current_score
                self.last_sign = '%'
                self.was_num = False
                self.current_score = self.last_sign
            case 'clear':
                self.current_score = '0'
                self.equation = '0'
                self.last_sign = None
                self.was_num = True
            case 'equal':
                self.equation += self.current_score
                if self.equation[0] == '0':
                    self.equation = self.equation[1:]
                self.current_score = str(eval(self.equation))
                self.equation = '0'
        self.ui.score.setText(f'{self.score_html_before}{self.current_score}{self.score_html_after}')
        
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