import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
# 导入桌面类
from PyQt5.QtWidgets import QDesktopWidget
# 导入水平布局
from PyQt5.QtWidgets import QHBoxLayout
# 导入按钮控件
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWindow, self).__init__(parent)

        # 设置主窗口的标题(因为其继承于QMainWindow，所以QMainWindow的属性，方法它都可以使用)
        self.setWindowTitle('这是一个主窗口应用')
        self.resize(800,400)

        # 创建一个状态栏的对象
        self.status = self.statusBar()
        # 调用状态栏对象的方法
        self.status.showMessage("只存在五秒的信息",5000)

        # 主窗口居中显示
        self.center_mainwin()

        # 添加一个按钮，退出主程序
        self.quit_application()

    def center_mainwin(self):
        """ 这个函数的功能是实现窗口的居中显示"""
        # 首先创建一个桌面窗口的实例，然后调用screenGeometry()方法获得屏幕坐标 geometry的英语意思是：几何形状
        screen = QDesktopWidget().screenGeometry()
        """ 可以先获取当前窗口的坐标系，然后再计算，也可以直接获取 """
        # win_size = self.geometry()
        # self.move((screen.width() - win_size.width()) / 2, (screen.height() - win_size.height()) / 2)
        self.move((screen.width()-self.width())/2,(screen.height()-self.height())/2)


    def quit_application(self):
        """ 这个函数的作用是退出应用程序 """
        # 添加一个按钮，调用QPushButton类，实例化一个按钮对象，并初始化命名
        self.button = QPushButton("退出应用程序")
        # self.button.setText('这是一个按钮命名的方法')
        # 构建连接,将按钮信号连接到槽方法
        self.button.clicked.connect(self.onClicked_Button)

        # 创建一个水平布局，然后把按钮控件放进布局中，这些都是临时变量
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        # 创建一个窗体
        mainFram = QWidget()
        mainFram.setLayout(layout)
        # 把窗体控件放进主窗体中
        self.setCentralWidget(mainFram)
        # self.setLayout(layout)  # 把布局直接放进当前的主窗体中不显示


    def onClicked_Button(self):
        """按钮单击事件触发的方法，这就是一个自定义的槽函数"""
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication().instance()
        app.quit()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./images/Dragon.ico'))

    # 创建主窗口类对象
    firwin = FirstMainWindow()
    firwin.show()

    sys.exit(app.exec_())

