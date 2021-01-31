# Filename: signals_slots.py

"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting(): # tạo 1 slot - như kiểu 1 tác vụ cần thực hiện
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout() # 

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # kết nối tác vụ click button với slot greeting

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_()) # hiển thị 1 vòng lặp