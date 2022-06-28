# _*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/1 000120:21
# 文件名称:匿名函数
# 开发工具:PyCharm
"""

用Lambda关键词能创建小型的匿名函数
匿名函数定义格式：
lambda 参数列表：返回值运算表达式
"""


def test(a):
    return a + 1

r = lambda a: a + 1    # 此时的r相当于函数名,a相当于参数,r也是接收返回值
print(r)
print(r(3))
print(test(3))

r=lambda x,y:x+y
print(r)
print(r(3,4))

"""
匿名函数的使用场合
    1.作为参数使用
"""

def  func1(a,f):
    print('------》',a)
    r =f(a)
    print('--------->',r)

func1(8,lambda x:x**2)


list1=[('tom',12),('tony',23),('any',25)]
m=max(list1,key=lambda x:x[1])    # 此处key是一个函数，取得是元组的第二个值，然后函数根据key来比较大小
print(m)

m=min(list1,key=lambda x:x[1])
print(m)

m=sorted(list1)
print(m)
m=sorted(list1,key=lambda x:x[1])
print(m)

m=sorted(list1,key=lambda x:x[1],reverse=True)
print(m)

# filter匿名函数返回值必须是bool类型。
m=filter(lambda x:x[1]>22,list1)
print(m)
print(list(m))