#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/19 001911:36
# 文件名称:tuple_example1
# 开发工具:PyCharm
"""
元组和列表类似，但是元组是不可以增删改
# 如果非要更改元组，可以把元组改为（list）列表，然后再更改，更改后再变为元组（tuple）
元组使用小括号（）
定义：
名字=（）

注意事项，如果一个元组里面只有一个元素时，必须添加逗号，（"aaa",)
"""

t1=()
print(type(t1))

t2=('aab')
print(type(t2))     # <class 'str'>

t3=('aa',)
print(type(t3))     # <class 'tuple'>

t4=('a','b',4)
print(type(t4))     # <class 'tuple'>

# 小标和切片，字符串，列表，元组都要注意小标不要越界
print(t2[0])
print(t2[2])
print(t3[0])

# 元组只有两个函数可以使用 count和index
# count是计算元组中值为value的元素的个数
# index   T.index(value, [start, [stop]]) -> integer -- return first index of value.
#  Raises ValueError if the value is not present.
t5 = ('a','b','c','u','e','a',1,5)
n=t5.count('a')
print(n)
index=t5.index('a',1,6)
print(index)
# 元组可以遍历
for i in t5:
    print(i)

# 如果非要更改元组，可以把元组改为列表，然后再更改，更改后再变为元组
t_example=list(t5)
print(t_example)
t_example.append('x')
t5=tuple(t_example)
print(t5)

