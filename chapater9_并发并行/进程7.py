#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000520:07
# 文件名称:进程7
# 开发工具:PyCharm
"""
进程间的通信

"""

from multiprocessing import Queue
from multiprocessing import Process
from time import sleep

def download(*args,**kwargs):
    imgs=['girl.jpg','boy.jpg','man.bmp']
    for images in imgs:
        print('正在下载：{}'.format(images))
        sleep(0.3)
        args[0].put(images)
    # pass

def getfile(*args,**kwargs):
    while True:
        try :
            file = args[0].get(timeout=3)
            print('保存成功：{}'.format(file))
        except :
            print('全部保存成功。')
            break

    pass


if __name__ == '__main__':

    q = Queue(5)
    pool1=Process(target=download,args=(q,))
    pool2=Process(target=getfile,args=(q,))
    pool1.start()
    pool2.start()
    pool1.join()
    pool2.join()
