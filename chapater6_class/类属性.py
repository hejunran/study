#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/3 000314:07
# 文件名称:类属性
# 开发工具:PyCharm
"""
类变量指的是在类中，但在各个类方法外定义的变量
类变量的特点是，所有类的实例化对象都同时共享类变量，也就是说，类变量在所有实例化对象中是作为公用资源存在的。
类变量的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用

"""

class CLanguage :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)

# 注意，因为类变量为所有实例化对象共有，通过类名修改类变量的值，会影响所有的实例化对象。
print("修改前，各类对象中类变量的值：")
clang1 = CLanguage()
print(clang1.name)
print(clang1.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)

print("修改后，各类对象中类变量的值：")
CLanguage.name = "Python教程"
CLanguage.add = "http://c.biancheng.net/python"
print(clang1.name)
print(clang1.add)
print(clang2.name)
print(clang2.add)

# 注意，通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，而是在给该对象定义新的实例变量
