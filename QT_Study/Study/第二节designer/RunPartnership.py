import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Partnership import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 实例化一个主窗口
    mainwindow = QMainWindow()

    # 实例化一个类的一个对象
    ui = Ui_MainWindow()
    # 调用ui对象的方法，为传入的窗体对象创建该方法中的所有组件
    ui.setupUi(mainwindow)

    mainwindow.show()

    sys.exit(app.exec_())