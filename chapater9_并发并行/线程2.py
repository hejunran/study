#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/6 000610:18
# 文件名称:线程2
# 开发工具:PyCharm

"""
线程可以共享全局变量，
GIL 全局解释器锁
python底层只要用线程默认加锁    GIL
当计算率达到一定程度，线程锁会被自动释放掉

作用范围
进程：计算密集型
线程：耗时操作，爬虫，IO

"""
import threading
from time import sleep

ticket =1000

def run1():
    global ticket
    for i in range(100):
        ticket -=1

def run2():
    global ticket
    for i in range(100):
        ticket -=1

if __name__ == '__main__':

    t1 =threading.Thread(target=run1,name='aa')
    t1.start()

    t2=threading.Thread(target=run2,name='bb')
    t2.start()

    t3 = threading.Thread(target=run1, name='bb')
    t3.start()

    print(ticket)