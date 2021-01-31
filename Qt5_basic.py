"""
--- 1 vài concept cần biết để cấu trúc 1 GUI bằng Qt được hiệu quả.
1. Widgets (Buttons,Labels,Line edits,Combo boxes,Radio buttons)
2. Layout managers
3. Dialogs
4. Main windows
5. Applications
6. Event loops
7. Signals and slots
PyQt5.QtWidgets là module cung cấp các concept này và chúng đặc biệt quan trọng.
Xem xét một số kiến thức sau:

"""
"""
 1. Widgets (Buttons,Labels,Line edits,Combo boxes,Radio buttons)
- Tạo button bằng QpustButton hiên thị một số nút nhấn đơn giản như, yes, no, apply, close, exit...
- Tạo các labels bằng Qlabel giúp hiển thị những thông tin text hoặc image, chấp nhận HTML tab
- line edit bằng QLineEdit giúp edit data trong cửa sổ lệnh.
- combo bằng QComboBox nhằm tạo một list option 
- radio button bằng QRadioButton nhằm tạo ra các hộp lựa chọn, hữu hiệu khi ta muốn tạo một sự lựa chọn
từ  nhiều sự lựa chọn khác nhau
- còn nhiều module nữa vào trang Qt đê tìm hiểu thêm.

2. Layout managers thư viện tạo một số dạng layout có sẵn
- QHBoxLayout: giúp tạo một layout với các đối tượng widget được thêm dần vào sau
- QVBoxLayout: giúp tạo một layout với các đối tượng thêm dần theo chiều dọc
- QGridLayout: giúp tạo một layout với các đối tượng thêm theo một Grid được định
sẵn kích thước. - chạy như matrix ấy
- QFormLayout: tạo một layout với 2 cột 1 cột mô tả và 1 cột có thể là tùy biến thành các Widget 
khác nhau như QLineEdit, QComboBox, QSpinBox...

3. Dialogs: với PyQt ta có thể phát triển 2 dạng ứng dụng GUI dựa trên class sử dụng để tạo
- A Main Window-Style application: sử dung QMainWindow tạo ra 1 main window vs a menu bar,
 some toolbars, a status bar, and a central widget...- có thể chứa nhiều dialog
- A Dialog-Style application: sử dung QDialog tạo 1 cửa sổ 

4. Application: QApplication - là cốt lõi của bất kì ứng dụng tạo bởi python nào
- cài đặt main setting cho chương trình
- Handling initialization and finalization
- Providing the event loop and event handling
- Handling most of the system-wide and application-wide settings
- Providing access to global information, such as the application’s directory, screen size, and so on
- Parsing common command-line arguments
- Defining the application’s look and feel
- Providing localization capabilities

5. Event loop: định hướng những sự kiện khi người sử dụng nhấn vào 1 button, hay nhập j đó...
- .exec_() on the QApplication object để tạo các sự kiện điều hướng cho ứng dụng.

6. Signals and Slots: 
- kết nối các signal tới 1 slot để thực hiện 1 tác vụ nào đố
"""

import sys
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout

app = QApplication(sys.argv)
layout = QVBoxLayout()

