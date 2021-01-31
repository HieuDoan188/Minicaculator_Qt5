# Filename: dialog.py

"""Dialog-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog): # tạo class Dialog kế thừa thuộc tính của QDialog class
    """Dialog."""
    def __init__(self, parent=None): # hàm khởi tạo 
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()  # tạo một layout dạng form 
        formLayout.addRow('Name:', QLineEdit())   # thêm các Widget vào layout
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)  # uses dlgLayout to arrange all the widgets on the form.
        btns = QDialogButtonBox() # provides a convenient object to place the dialog buttons.
        btns.setStandardButtons(  # tạo 2 button standard là ok và cancel
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok) 
        dlgLayout.addWidget(btns) 
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())