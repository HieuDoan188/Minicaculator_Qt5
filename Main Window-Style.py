# Filename: main_window.py

"""Main Window-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
 
class Window(QMainWindow): # tạo class WIndow thừa kế thừ QmainWindow
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer.""" 
        super().__init__(parent)
        self.setWindowTitle('QMainWindow') # set window title
        self.setCentralWidget(QLabel("I'm the Central Widget")) # set Qlabel vs vị trí ở giữa
        self._createMenu()  # gọi các phương thức riêng từ các hàm để tạo những phần tử trong GUI
        self._createToolBar() 
        self._createStatusBar() 

    def _createMenu(self): # tạo 1 menu bar với 1 phẩn tử exit bên trong
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction('Exit', self.close)

    def _createToolBar(self): # tạo 1 tool bar 
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self): # tạo 1 status bar tại bottom của window
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())