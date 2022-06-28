#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000519:54
# 文件名称:进程6
# 开发工具:PyCharm
"""
阻塞式：
    1.不用pool.close()和pool.join(),他本身就是阻塞的，一个进程执行不完，下一个进程不能执行
    2.添加一个执行一个任务.

    pool.close()        # 这是进程池添加任务结束
    pool.join()         # 让主进程让步
    pool.apply()        #阻塞式
    pool.apply_async()  # 非阻塞式
"""
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
    print('完成任务{}用时时间：{}，任务（当前进程id）id：{}'.format(args[0],end-start,os.getpid()))
    # return '完成任务{}用时时间：{}，任务（当前进程id）id：{}'.format(args[0],end-start,os.getpid())

container=[]
def callback_func(n):
    container.append(n)

if __name__ == '__main__':
    pool =Pool(5)

    task_list = ['听音乐', '吃饭', '打游戏', '写作业', '科研', '做ppt', '考试', '睡觉']
    for temp_task in task_list:
        pool.apply(task,args=(temp_task,))

# 开始做任务了啦 听音乐
# 完成任务听音乐用时时间：1.4152672290802002，任务（当前进程id）id：15480
# 开始做任务了啦 吃饭
# 完成任务吃饭用时时间：1.8238639831542969，任务（当前进程id）id：11524
# 开始做任务了啦 打游戏
# 完成任务打游戏用时时间：1.3388054370880127，任务（当前进程id）id：3468
# 开始做任务了啦 写作业
# 完成任务写作业用时时间：1.1403498649597168，任务（当前进程id）id：8972
# 开始做任务了啦 科研
# 完成任务科研用时时间：0.4247558116912842，任务（当前进程id）id：11468
# 开始做任务了啦 做ppt
# 完成任务做ppt用时时间：0.07895469665527344，任务（当前进程id）id：15480
# 开始做任务了啦 考试
# 完成任务考试用时时间：0.42775535583496094，任务（当前进程id）id：11524
# 开始做任务了啦 睡觉
# 完成任务睡觉用时时间：0.34951114654541016，任务（当前进程id）id：3468