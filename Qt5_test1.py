# ứng dụng đầu tiên với Qt5
"""
tạo ứng dụng “Hello, World!” với Python và PyQt với các bước sau:

1. Import một số widgets từ PyQt5.QtWidgets.
2. tạo 1 ví dụ QApplication.
3. tạo giao diện.
4. Show GUI.
5. chạy ứng dụng với 1 số sự kiện lặp event loop (or main loop).
"""
"""
 Đầu tiên import thư viện sys để handle tình trạng của ứng dụng, sau đó là các module 
 QApplication, QWidget, và QLabel từ package PyQt5.QtWidgets
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# bước 2 : tạo 1 ví dụ cho QApplication
app = QApplication(sys.argv)

# hiển thị một số thông tin trên GUI(tên tiêu đề, hiện 1 thông tin trên GUI) sử dụng QWidget()
window = QWidget()
window.setWindowTitle("PyQt5_test1")
window.setGeometry(10,10,400,100) # xác định kích thước và vị trí hiển thị trên màn hình
window.move(500,250) # xác định vị trí của khung hiển thị 
helloMsg = QLabel("<h1><i>hello world!</i></h1>", parent=window) # show chữ hello world trên nên của GUI window vừa tạo
# Qlabel chấp nhận HTML text nên ta có thể ứng sử dụng các tab Html để hiển thị
helloMsg.move(60,15)  # xác định vị trí của chữ

# hiển thị GUI 
window.show()

# chạy vòng lặp để hiển thị GUI
sys.exit(app.exec_())

# ---------- xem xét code style ------------

