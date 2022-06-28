import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
# 导入桌面类
from PyQt5.QtWidgets import QDesktopWidget
# 导入水平布局
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
# 导入按钮控件
from PyQt5.QtWidgets import QPushButton,QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("This is a test")
        devicewidget = DeviceWidget()
        self.setCentralWidget(devicewidget)

class DeviceWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(DeviceWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        save_image_btn = QPushButton("Save Image")
        restore_image_btn = QPushButton("Install Image")

        device_size_layout = QHBoxLayout()
        device_size_desc_lbl = QLabel("Space:")
        device_size_lbl = QLabel("69420MB")
        device_size_layout.addWidget(device_size_desc_lbl)
        device_size_layout.addWidget(device_size_lbl)

        layout.addWidget(save_image_btn)
        layout.addWidget(save_image_btn)
        layout.addLayout(device_size_layout)

        self.setLayout(layout)

#Initialization
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()