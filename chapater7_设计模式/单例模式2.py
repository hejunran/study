#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/5 000510:43
# 文件名称:单例模式2
# 开发工具:PyCharm
"""
单例设计模式:
    属于创建型模式，它提供了一种创建对象的最佳方式。这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建
    这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象
    1.目的 —— 让 类 创建的对象，在系统中 只有 唯一 的一个实例, 每一次执行 类名() 返回的对象，内存地址是相同的
    2.单例应用场景：音乐播放器、回收站、打印机...
    3.实现单例模式的方式
        a.使用模块
        b.使用 __new__
        c.使用装饰器（decorator）
        e.使用元类（metaclass）
"""

"使用new方法实现"
# 第一种写法
class Students(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):               # hasattr() 函数用于判断对象是否包含对应的属性。，hasattr是 has attribute 的简写
            # obj=super(Students,cls)
            # print(cls)
            # print(obj)
            cls._instance =super(Students,cls).__new__(cls)               # cls.__instance=object.__new__(cls)
            # print(cls._instance)
        return cls._instance                           # getattr()  是get attribute
stu1=Students()
stu2=Students()
print(stu1)
print(stu2)

# 第二中写法：
class Singleton:
    # 私有化
    __instance =None
    # 重写父类__new__
    def __new__(cls, *args, **kwargs):
        print('-------->__new__')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print(cls.__instance)
            return cls.__instance
        else:
            return cls.__instance
s=Singleton()
s1=Singleton()
print('--------------------')
print(s)
print(s1)

"使用装饰器实现"
