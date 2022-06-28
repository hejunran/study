import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton

# class ScreenGeometry

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()

    """
    创建按钮，注意按钮的创建可以通过传参的方法传其父对象，也可以通过setParent方法设置其父对象
    这样只要父对象显示，包含的子对象也会跟着一起显示。（所以按钮控件不需要单独show）
    """
    # 方法一： 通过setParent设置父对象
    btn = QPushButton('按钮')
    btn.setParent(widget)

    # 方法二：通过初始化实例对象时，传入父对象。
    # btn = QPushButton(widget)
    # btn.setText('按钮')

    btn.move(50,50)
    widget.resize(300,300)
    widget.move(400,200)
    widget.show()

    sys.exit(app.exec_())