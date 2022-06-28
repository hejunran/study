#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/3 00039:52
# 文件名称:集合推导式
# 开发工具:PyCharm
"""
集合推导式
类似于列表推导式，只不过集合中不存在重复值
"""
# 集合推导式
list1=[1,2,3,1,4,5,6,2,3]
set1={x+1 for x in list1}
set2={x+1 for x in list1 if x>5}

# 字典推导式
dict1={'a':'A','b':'B','d':'D'}
new_dict={value:key for key,value in dict1.items()}
print(new_dict)


#生成器,不同于类别推导式，就是最外层用小括号就行
g = (x*3 for x in range(10))     #  <class 'generator'>
print(type(g))
# 通过调用__next__()方式得到元素
print(g)
g.__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# 通过系统自带的next（生成器对象），每调一次next则会产生一个数
next(g)
print(next(g))

s = (x*3 for x in range(10))
while True:
    try:
        e=next(s)
        print(e)
    except Exception as err:
        print('没有更多元素啦')
        break

"""
函数生成生成器
步骤：
1.定义一个函数，函数中使用yield关键子
2.调用函数，接收调用结果
3.得到的结果就是生成器
4.借助于next(),__next__()得到你想要的元素

"""
def func():
    n =0
    while True:
        n +=1
        yield n           # 相当于一个 return n  和一个暂停

g =func()     # 调用时只是产生一个生成器对象，没有进入函数体内部
print(g)
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))