#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/7 000715:44
# 文件名称:线程4
# 开发工具:PyCharm

import threading
import time
import random
from threading import Thread,Lock

lockA=Lock()
lockB=Lock()

# 自定义线程
class MyThread1(Thread):
    def __init__(self,name):
        # super(MyThread1, self).__init__()
        super(MyThread1, self).__init__(name=name)
        # self.name=name

    def run(self) -> None:
        if lockA.acquire():           #请求锁
            print(self.name+'获取了A锁')
            time.sleep(0.1)
            if lockB.acquire():
                print(self.name+'又获取了B锁，原来还有A锁')
                lockB.release()
        lockA.release()

class MyThread2(Thread):
    def __init__(self,name):
        super(MyThread2, self).__init__(name=name)
        # self.name=name
    def run(self) -> None:
        if lockB.acquire():  # 请求锁
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            # if lockA.acquire():
            if lockA.acquire(timeout=0.3):
                print(self.name + '又获取了A锁，原来还有B锁')
                lockA.release()
        lockB.release()

if __name__ == '__main__':
    # t1=threading.Thread(target=MyThread1,name='aa')
    # t2=threading.Thread(target=MyThread2,name='bb')
    t1=MyThread1(name='aa')
    t2=MyThread2(name='bb')

    t1.start()   # 和自定义进程类似，运行start之后，进入就绪状态，等分配到cpu，自动找到自定义的run方法，进行运行状态。
    t2.start()

