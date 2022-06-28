#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000517:31
# 文件名称:进程5
# 开发工具:PyCharm
"""
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态的生成多个进程
但是如果生成的进程数为成千上百个，手动的去创建的工做量是巨大的，此时可以使用multiprocessing中的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新请求提交到Pool中时，如果没有满，
那么就会创建一个新的进程用来执行该请求，但是如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
直到池中进程结束，才会创建新进程来执行

阻塞式：

非阻塞式：
    1.把任务全部添加到队列中，并没有其他进程执行完毕之后，但是回调函数是等待某一个任务（进程完成之后），再执行


"""

# 非阻塞式进程
from multiprocessing import Pool,Process
import time
from random import random
from time import sleep
import os


def task(*args,**kwargs):
    print('开始做任务了啦',args[0])
    start= time.time()
    sleep(random()*2)
    end =time.time()
    # print('完成任务{}用时时间：{}，任务（当前进程id）id：{}'.format(args[0],end-start,os.getpid()))
    return '完成任务{}用时时间：{}，任务（当前进程id）id：{}'.format(args[0],end-start,os.getpid())

container=[]
def callback_func(n):
    container.append(n)

if __name__ == '__main__':
    pool=Pool(5)                    # processes: Optional[int] = 5 创建一个大小为5的进程池，其实是一个队列

    task_list=['听音乐','吃饭','打游戏','写作业','科研','做ppt','考试','睡觉']
    for temp_task in task_list:
        pool.apply_async(task,args=(temp_task,),callback=callback_func)     # callback是回调方法,可以定义一个函数接收task返回的值

    pool.close()        # 这是进程池添加任务结束
    pool.join()         # 堵住主进程，否则主进程结束，子进程就死了,当所有任务完成只有，结束

    for c in container:
        print(c)
    print(container)
    print('over')