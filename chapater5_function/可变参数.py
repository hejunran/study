# _*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/30 003015:27
# 文件名称:可变参数
# 开发工具:PyCharm
"""
可变参数：
*args
**kwargs

*args
拆装包问题
函数的装包：
    def 函数(*args)
    pass
    调用时： 函数（1，2，3，4）传给多个参数时，会有一个装包的过程
拆包：
list,tuple,set
    def 函数（*args）：    -------->这是一个装包的过程
        pass
    调用时： 函数（*list）------->这是一个拆包的过程
函数调用时： 函数（*列表名） 函数（*元组名） 函数（*集合名），这个函数调用时在元组，集合，列表前加个*是一个拆包的过程，这是因为多参数传递
传递给函数是多个参数，不是一个列表，元组，集合等这些为一个参数，故需要一个拆包的过程
如果不拆包，就会直接进行装包的过程，那么传进去的元素就是 ： （list，）元组里面包含一个列表（注意元组要求一个元素时，会添加一个逗号）

可变参数两个**的问题
**kwargs
kwargs 是一个关键字参数，在函数调用时，必须传递关键字参数，才可以将其转换成key：value
如果函数调用时传入的一个字典，要先进行相应的拆字典，然后再装字典。
def 函数名（**kwargs）：
    pass
调用时：函数名（**字典名）-------->调用时，**的作用时拆包的过程，然后以bookname='西游记',author='吴承恩',number=5这样关键字的形式传入函数，
然后进行装包的过程。

"""


# 求和
# def get_sum(a, b):
#     # 这种只能求两个数的和
#     return a + b
def get_sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)


get_sum(1, 2)  # 此时args为(1, 2)按元组存放，不能再更改数据了
get_sum(1, 2, 3)  # 此时args为(1, 2, 3)
get_sum(1, 2, 3, 4, 5)  # 此时args为(1, 2, 3, 4, 5)

a, *b, c = 1, 2, 3, 4, 5, 6
# python中加*相当于把变量变成一个容器，存放多个值，在普通的赋值中容器是列表，在函数的传参中容器是元组
print(a)  # 1
print(b)  # [2, 3, 4, 5]  这个过程相当于把2，3，4，5打包装入b这个列表中
print(c)  # 6

a, b, c = (1, 2, 3)  # 这是一个拆包的过程
print(a)
print(b)
print(c)

*a, b, c = (1, 2, 3, 4, 5, 6, 7)  # 这是一个先拆包再装包的过程
print(a)  # [1, 2, 3, 4, 5]
print(b)  # 6
print(c)  # 7

list=[1,2,3,4,5,6]
# get_sum(list)
get_sum(*list)
"""
可变参数两个**的问题
**kwargs
kwargs 是一个关键字参数，在函数调用时，必须传递关键字参数，才可以将其转换成key：value
"""
def show_book(**kwargs):
    print(kwargs)   # {}

show_book()
# show_book('西游记','红楼梦')
show_book(bookname='西游记',author='吴承恩',number=5)
show_book(bookname='西游记')

dict={'bookname':'西游记','author':'吴承恩','number':5}
# show_book(dict)      # 这中不行，要先拆包，再装包
show_book(**dict)

"""
对于有
*args
**kwargs
都存在时
"""
def show_books(*args,**kwargs):
    print(args)       # args 元组
    print(kwargs)     #  kwargs 是字典

show_books()
show_books('王思聪')
# 结果：
# ('王思聪',)
# {}
show_books('wangsicong','zhangyining')
# 结果：
# ('wangsicong', 'zhangyining')
# {}
show_books(bookname='西游记',author='吴承恩',number=5)
# 结果 ：
# ()
# {'bookname': '西游记', 'author': '吴承恩', 'number': 5}
show_books('wangsicong','zhangyining',bookname='西游记',author='吴承恩',number=5)
# 结果：
# ('wangsicong', 'zhangyining')
# {'bookname': '西游记', 'author': '吴承恩', 'number': 5}
list1=[1,2,3,4,2,6]
dict={'bookname':'西游记','author':'吴承恩','number':5}
show_books(*list1,**dict)
# 结果
# (1, 2, 3, 4, 2, 6)
# {'bookname': '西游记', 'author': '吴承恩', 'number': 5}

# ''.join()