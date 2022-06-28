# _*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000516:08
# 文件名称:进程
# 开发工具:PyCharm
"""
进程：
"""
# 进程的创建
"""
在linux下可以使用fork函数创建进程，在windows系统上可以引用multiprocessing模块，创建进程。
"""

from multiprocessing import Process
from time import sleep
import os

def task1():
    while True:
        sleep(1)
        # os.getpid()是得到当前子进程的pid号， os.getppid()得到的是主进程的pid号
        print('这是任务1........',os.getpid(),'--------------',os.getppid())

def task2():
    while True:
        sleep(1)
        print('这是任务2........',os.getpid(),'--------------',os.getppid())

if __name__ == '__main__':
    # 子进程
    """
    target参数，传递的是任务
    name参数，是子进程的名字
    """
    p1= Process(target=task1,name='任务1')
    p1.start()
    print(p1.name)
    p2 = Process(target=task2,name='任务2')
    p2.start()
    print(p2.name)

