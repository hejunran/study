#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000517:16
# 文件名称:进程4
# 开发工具:PyCharm
"""
自定义进程
"""

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess, self).__init__()
        self.name=name

    # 重写run方法
    def run(self):
        n =1
        while True:
            print('{}---------->自定义进程，n：{}'.format(n,self.name))
            # print('这是一个进程名字：',self.name)
            n +=1

if __name__ == '__main__':
    p1 =MyProcess('任务1')
    p1.start()                  # 调用start()方法，首先开辟新的进程，然后他会找里面的run方法进行执行。
    p2 = MyProcess('任务2')
    p2.start()
