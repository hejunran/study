#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000516:39
# 文件名称:进程2
# 开发工具:PyCharm
"""
向往进程中传参数
process=Process(target =函数名，name=进程名字，args=（给函数传递的参数）），注意args是一个元组。
process ：进程对象
对象的调用：
process.start()  启动了进程并且执行任务
process.run()  只是执行了任务，但是没有启动进程
terminate()   终止
"""
from multiprocessing import Process
from time import sleep
import os

def task1(*args, **kwargs):      # args和kwargs用于接受Process传进来的参数。
    print(args)
    while True:
        sleep(args[0])
        # os.getpid()是得到当前子进程的pid号， os.getppid()得到的是主进程的pid号
        print('这是任务1........',os.getpid(),'--------------',os.getppid())

def task2(*args, **kwargs):
    while True:
        sleep(args[0])
        print('这是任务2........',os.getpid(),'--------------',os.getppid(),args[1])

number =1
if __name__ == '__main__':
    "当我们运行当前程序时，系统会自动会程序分配一个进程，这是主进程，然后再调Process创建两个子进程，可以知道，任务1和任务2父进程相同"
    # 子进程
    p1= Process(target=task1,name='任务1',args=(1,))        # (1,)元组的标准格式
    p1.start()
    print(p1.name)
    p2 = Process(target=task2,name='任务2',args=(2,'bb'))
    p2.start()
    print(p2.name)

    while True:
        number +=1
        sleep(0.2)
        if number>100:
            p1.terminate()
            p2.terminate()
        else:
            print(number)