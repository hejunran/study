#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/6 00069:47
# 文件名称:线程1
# 开发工具:PyCharm
"""
线程:
    t1=threading.Thread(target=download,name='aa',args=(1.5,))
    t1.start()
    状态：新建，就绪，运行，阻塞，结束
"""
import threading
from time import sleep
# 进程 Process
# 线程 Threading

def download(*args,**kwargs):
    imgs=['girl.jpg','boy.jpg','man.bmp']
    for images in imgs:
        print('正在下载：{}'.format(images))
        sleep(args[0])
        # args[0].put(images)
        print('图片:{}下载成功'.format(images))

def listenMsuic(*args,**kwargs):
    musics=['稻香','大碗宽面','烤面筋','小苹果']
    for temp_music in musics:
        sleep(args[0])
        print('正在听音乐：{}'.format(temp_music))

if __name__ == '__main__':
    # 线程对象
    t1=threading.Thread(target=download,name='aa',args=(1.5,))
    t1.start()

    t2 =threading.Thread(target=listenMsuic,name='bb',args=(2,))
    t2.start()
    # t.join()
    n=1
    while True:
        print(n)
        sleep(2)
        n +=1