#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/3 000317:24
# 文件名称:单例模式
# 开发工具:PyCharm
"""
单例模式
开发模式：单例模式，工厂模式
"""

class Student:
    pass
s1=Student()
s2=Student()
print(s1)
print(s2)
# <__main__.Student object at 0x0000023BC734B6A0>
# <__main__.Student object at 0x0000023BC734B710>
# 可以发现每实例化一次都开辟一个空间，非常消耗内存

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

class Students:
    def __new__(cls, *args, **kwargs):
        print(cls)
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(hasattr(cls,'_instance'))
        if not hasattr(cls,'_instance'):                  # 利用这种写法时，不能用私有法的属性，因为每一次进来cls.__instance都是不存在的，那么就不能实现单例模式
            print(object.__new__(cls))
            cls._instance = object.__new__(cls)
        print(dir(cls))
        return cls._instance

su1=Students()
su2=Students()
print(su1)
print(su2)