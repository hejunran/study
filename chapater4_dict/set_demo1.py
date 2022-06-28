#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/21 002118:27
# 文件名称:set_demo1
# 开发工具:PyCharm
"""
定义集合 set  特点：没有重复，无序排列的
集合名={元素，元素，元素，....}，
"""

set1={'张三'}
print(type(set1))

# 去除列表中的重复元素  , list允许重复
list1=[1,2,1,3,4,5,6,9,8,7]
set2=set(list1)
# set.add('三体')
print(set2)

# 空集合的声明不能用{}，只能用set
set3={}
print(type(set3))
set4=set()
print(type(set4))

# 添加元素
set4.add('三体')
print(set4)
set3=set()
set3.add('红楼梦')
set3.add('盗墓笔记')
print(set3.add('红楼梦'))   # add当添加重复元素时，返回的时None，添加不成功
print(set3)
set3.update(set4)           # update是把一个集合添加到另一个集合里面
set5={'三体'}
set3.update(set5)           # 如果集合中已经有这个元素了，则返回None，添加不成功
print(set3)

import random
rand_sets=set()
path='asdfghjklzxcvbnmqwertyuiop1234567890ZXCVBNMASDFGHJKLPOIUYTREWQ'
while True:
    code=''
    for i in range(4):
        random.randint(0,len(path)-1)
        r=random.choice(path)
        code+=r
    rand_sets.add(code)
    if len(rand_sets)==4:
        break
print(rand_sets)


# 移除元素
"discard 删除一个成语，删除的元素如果不在集合中，返回空"
set3.discard('三体u')
print(set3)
set3.remove('三体')           # 移除的必须时集合中的元素，不是其中的元素报错

# 集合的交，并，差

"""
总结：
list：允许重复，有序，由下标[]
tuple:允许重复，里面的元素不能增加删除，只能查看（）
dict：键值对存在，键：唯一，值：允许重复{}
set：不允许重复，无序   {}

强制转换问题
list --------> tuple,set(长度可能不一致)
tuple ------->list,set(长度可能不一致)
set --------->list ,tuple

dict-------->list,tuple,set,可以转换，但是都是把字典的键放到list，tuple，set中

list------->dict
特殊要求：
list1=[('a','b'),('c','d')]

"""
list1=[('a','b'),('c',12)]
print(dict(list1))

