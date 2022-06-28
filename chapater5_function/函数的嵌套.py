#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/1 000114:59
# 文件名称:函数的嵌套
# 开发工具:PyCharm
"""
嵌套：
# 内层函数----->外层函数------>全局------->系统builtins

闭包：
1.嵌套函数，外部函数中定义了内部函数
2.内部函数引用了外部函数的变量
3.外部函数有返回值，返回值是内部函数名
格式：
def  外部函数名（）：
    def 内部函数名（）：
       。。。
    return 内部函数名

作用：
1.保存返回返


回闭包时的状态值
2.
"""

def outer():
    a=100

    def inner():     # 这个函数相当于变量
        b=200
        b +=a        # 内部函数可以使用外部函数的变量，但是不可以直接修改外部函数变量，
        #a +=b        如果在内部函数修改外部函数的变量，需要加nonlocal关键字
        # nonlocal a
        # a +=b
        print('a:',a)
        print('我是内部函数',b)
    result=locals()       # locals() 查看函数中的局部变量，以字典的形式返回局部变量
    print(result)
    print(a)
    print(inner)
    # 调用inner()
    inner()

outer()

# 闭包
def outer(n):
    a=100
    def inner():
        b =a + n
        print('内部函数：',b)
    return inner        # 3.返回值是内部函数

r =outer(5)   # 此时函数的返回值是内部函数的地址
print(r)
r()

def outer(n):
    a=100
    def inner():
        b =a + n
        print('内部函数：',b)
        return b
    return inner        # 3.返回值是内部函数
r =outer(5)   # 此时函数的返回值是内部函数的地址
print(r)
r()