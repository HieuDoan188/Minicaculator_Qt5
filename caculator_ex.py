import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from functools import partial


class caculator(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle('Mini Caculator')
        # self.setGeometry(100,100,400,400)
        self.setFixedSize(300,300) # cố định kích thước khung
        # self.move(200,200)
        
        # đưa vị trí của appp vào giữa
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # tạo display và button
        self._createDiplay()
        self._createButtons()

    def _createDiplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText],pos[0],pos[1])
        
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

# class control xử lý hiển thị và xóa 
class control:
    def __init__(self,view):
        self._view = view
        # chạy hàm connect
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=','C'}:
                btn.clicked.connect(partial(self._buildExpression,btnText))
        
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# hàm bắt lỗi
def Errorhandle(expression):
    try:
        result = str(eval(expression,{},{}))
    except Exception:
        result = ERROR_MSG
    return result

# hàm xử lý toán học


def main():
    app = QApplication(sys.argv)
    view = caculator()
    view.show()

    control(view=view)

    sys.exit(app.exec_()) # runs the application’s event loop with pycalc.exec_()

if __name__=='__main__':
    main()






