#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/30 003019:27
# 文件名称:全局和局部变量
# 开发工具:PyCharm
"""
全局变量和局部变量
global关键字的添加：
只有不可变的类型才添加关键字 global
可变的类型不用添加 global

不可变类型：当我们改变变量的值时，地址发生了改变
        类型：str，int，float，元组-tuple

可变类型：当我们改变变量的内容时，地址不发生改变
        类型：list，dict，set

全局变量再函数之外
局部变量在函数内部
"""
# python中有一个小整数对象池（1到256），
a=100
print(id(a))
a=90
print(id(a))
b=100
print(id(b))
c='xyz'
print(id(c))
c='x'
print(id(c))


list1=[1,2,3,4,5]
print(id(list1))
list1.append(6)
print(id(list1))

dict1={'hejunran':1}
print(id(dict1))
dict1.update({'wangzhe':2,'author':'hejunran'})
print(dict1)
print(id(dict1))