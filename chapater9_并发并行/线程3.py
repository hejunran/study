#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/7 000715:08
# 文件名称:线程3
# 开发工具:PyCharm
"""
共享数据：
    如果多个线程共同对某个数据进行修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个数据进行同步
同步：一个一个的完成，一个做完另一个才能进来

使用Thread对象的Lock和RLock可以实现简单的线程同步，两个对象都有acquire方法和release方法，
对于每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间
多线程的优势在于可以同时运行多个任务（至少宏观上感受是这样的），但是当线程需要贡献数据时，
可能存在数据不同步问题，为了避免这种情况，才引入锁的概念

死锁：
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
尽管死锁很少发生，但是一旦发生就会造成应用的停止响应，程序不做任何事情

"""

import threading
import random
import time

lock=threading.Lock()
list1=[0]*10

def task1():
    # 获取线程锁，如果已经上锁了，则阻塞等待
    lock.acquire()            # 阻塞别的线程申请资源
    for i in range(len(list1)):
        list1[i]=i
        time.sleep(0.3)
    lock.release()           # 释放锁
        # pass

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('----->',list1[i])
        time.sleep(0.3)
    lock.release()
    # pass

if __name__ == '__main__':
     t1=threading.Thread(target=task1,name='aa')
     t2=threading.Thread(target=task2,name='bb')

     t1.start()
     t2.start()