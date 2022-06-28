#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/7 000716:07
# 文件名称:生产者与消费者
# 开发工具:PyCharm
"""
两个线程之间的通信
python的queue模块提供了同步的，线程安全队列，包括：
    FIFO队列Queue，
    LIFO队列lifoQueue
    优先级队列PriorityQueue
这些队列都实现了锁原语（原子操作，即要么不做，要吗做完），能够在多线程中直接使用，可以使用队列来实现线程间的同步。
"""

import threading
import time
import random
import queue

q=queue.Queue()
def produce(name):
    count=0
    while count<10:
        print('生产者%s生产中'%name)
        time.sleep(0.2)
        num =random.randint(1,100)
        print('生产者{}生产了产品：{}'.format(name,num))
        q.put(num)
        count+=1

def consumer(name):
    count=0
    while count<10:
        time.sleep(1)
        if not q.empty():
            num=q.get()
            print('消费者{}消耗了产品；{}'.format(name,num))
        else:
            print('没有产品了')
        count += 1

if __name__ == '__main__':
    p1=threading.Thread(target=produce,args=('A',))
    # p2 = threading.Thread(target=produce, args=('B',))
    # p3 = threading.Thread(target=produce, args=('C',))
    # p4 = threading.Thread(target=produce, args=('D',))

    c1=threading.Thread(target=consumer,args=('hejunran',))
    c2=threading.Thread(target=consumer,args=('zhaokaimin',))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    c1.start()
    c2.start()


