import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication

if __name__ == '__main__':
    # 初始化一个application实例
    app = QApplication(sys.argv)

    # 实例化一个窗体对象
    mywidget = QWidget()

    # 实例化一个桌面窗体的对象，然后获取桌面窗体屏幕的大小
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    size = screen.size()
    screen_width = screen.width()
    screen_height = screen.height()

    # resize设置窗体的大小
    mywidget.resize(400, 400)
    # 获取当前窗体的长宽
    mywidget_width = mywidget.width()
    mywidget_heigth = mywidget.height()
    """# 设置窗体在桌面的位置,利用窗体大小和桌面大小使得窗体在桌面正中央显示"""
    #  (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
    mywidget.move((screen.width() - mywidget.width()) / 2, (screen.height() - mywidget.height()) / 2)

    # setWindowTitle设置窗体的名称
    mywidget.setWindowTitle('这是一个桌面应用程序')
    # 显示窗体
    mywidget.show()

    # 进入程序的主循环、循环扫描在这个窗口上的事件，并通过exit函数确保主循环安全结束，
    sys.exit(app.exec_())


