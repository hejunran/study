#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000516:59
# 文件名称:进程3
# 开发工具:PyCharm
"""
sleep动作是cpu分配给各个进程的模拟
多进程对于全局变量访问，在每一个全局变量里面都放一个m变量
保证每个进程访问变量互不干扰
m =1 不可变类型
list1=[] 可变类型
"""
from multiprocessing import Process
from time import sleep
import os

m =1     # 全局变量

def task1(*args, **kwargs):      # args和kwargs用于接受Process传进来的参数。
    print(args)
    global m
    while True:
        sleep(args[0])
        m +=1
        # os.getpid()是得到当前子进程的pid号， os.getppid()得到的是主进程的pid号
        print('这是任务1........',os.getpid(),'--------------',os.getppid(),m)

def task2(*args, **kwargs):
    global m
    while True:
        sleep(args[0])
        m +=1
        print('这是任务2........',os.getpid(),'--------------',os.getppid(),m)

# number =1
if __name__ == '__main__':
    "当我们运行当前程序时，系统会自动会程序分配一个进程，这是主进程，然后再调Process创建两个子进程，可以知道，任务1和任务2父进程相同"
    # 子进程
    p1= Process(target=task1,name='任务1',args=(1,))        # (1,)元组的标准格式
    p1.start()
    print(p1.name)
    p2 = Process(target=task2,name='任务2',args=(2,))
    p2.start()
    print(p2.name)

    while True:
        m +=1
        sleep(3)
        print(m)
    # while True:
    #     number +=1
    #     sleep(0.2)
    #     if number>100:
    #         p1.terminate()
    #         p2.terminate()
    #     else:
    #         print(number)