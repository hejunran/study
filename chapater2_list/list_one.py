#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/16 001621:12
# 文件名称:list_one
# 开发工具:PyCharm

list_example=['牛奶','辣条','面包','烤肉','鸡腿','臭豆腐']
# 列表的逆序输出 ,字符串的逆序输出一样，切片操作，strat：end：step 要保证start 到end方向和step方向一致才可以取到值
# 访问列表里面的值和字符串的值可以用下标直接访问 str[i] , list[i]
# index(self, value, start=None, stop=None)，从strat开始到end结束，查找列表中element值为value的元素的下表
# count(value) 统计列表中值为value的元素的个数
print(list_example.index('面包',1,-1))
print(list_example[::-1])    # ['臭豆腐', '鸡腿', '烤肉', '面包', '辣条', '牛奶']
print(list_example[::-2])    # ['臭豆腐', '烤肉', '辣条']
print(list_example.clear())

# 字符串的遍历 for i in str 这里i是字符串里面的值 也可以 for i in range(len(str))，这里面i是字符串的下标
# 列表的遍历也可以for i in list,这里i是列表里面的值，也可以 for i in range(len(list))，这里面i是列表的下标
for i in list_example:
    print(i)
for i in range(len(list_example)):
    print(list_example[i])

# 列表的增加, append(),insert(),+,extend()
# append在列表的末尾添加元素
# insert(位置，元素)，根据位置下标，插入元素
# 使用加号拼接 把加号后面列表中的元素添加到加号前面的列表元素后面
# 使用extend(),扩展列表 调用这个函数的为要扩展的对象，传如的参数为加在后面的列表
list_example2=[]
list_example2.append('面包')
list_example2.append('牛奶')
list_example2.append('辣条')
print(list_example2)
print(list_example2.index('牛奶'))
list_example3=['王思聪']
list_example3.append('张一宁')
print(list_example3)

# 使用加号拼接 ，
""" 总结：加号的使用
数字时：+ 号就是运算符
字符串时： + 号是拼接符
列表时： + 号可以合并两个列表
"""
list_example4 =list_example3+list_example2
print(list_example4)

# 使用extend(),扩展列表 调用这个函数的为要扩展的对象，传如的参数为加在后面的列表
list_example3.extend(list_example2)
print(list_example3)

# 列表元素的删除:pop ,remove,clear
# pop()里面的参数放的是索引下表，弹出相应的值。pop()也可以不放任何参数，这样是从列表的末尾弹出一个值
# remove()里面的参数放的是value，放的不是索引，是值，删除列表中所有值为value的元素。如果列表中有多个element的元素值等于value，remove只会删除一个（从左往右的第一个）
# 判断元素是否在列表中 可以用 if i in list ，判断元素不在列表中 if i not in list
# clear() 无需传参，清空列表里面所有元素，列表仍然存在
# del() 无需传参，删除列表，删除了该列表指向列表首地址指针。
print('*'*20)
print(list_example2)
list_example2.pop(-1)
print(list_example2)
list_example2.append('面包')
list_example2.append('面包')
list_example2.append('面包')
print(list_example2.count('面包'))
print(list_example2)
list_example2.remove('面包')
print(list_example2)

# 删除列表中所有值为'面包'的元素
flag=True
while flag:
    if '面包' in list_example2:
        list_example2.remove('面包')
    else:
        flag=False
print('*'*20)
print(list_example2)

# del
print('*_'*20)
list_example5 =list_example3    # 此时list_example5 和list_example3指向的地址一样，此处的赋值相当于赋予的是地址。
print(list_example3)
del list_example3[2]
print(list_example3)
print(list_example5)    # 注意此处由于list_example5 和list_example3指向的地址一样，删除list_example3指向的第三个空间元素，相当于删除了list_example5中的元素
del list_example3       # 此时是删除了list_example3这个变量名，这个变量名可以指向列表的首地址，删除了它，就无法指向列表了
print(list_example5)    # 此处相当于回收了list_example3这个指向列表的地址



# reverse(),sort()
#  reverse() 对列表中的元素进行反转，没有排序
# sort() 对列表中的元素进行排序，升序
list_example5.sort()
print(list_example5)
list_example5.reverse()
print(list_example5)


"""
列表的切片处理
如 L =[1,2,3,4,5,6,7,8,9]
l1=L[::2] 表示从列表中每间隔两个位置取出，然后构成一个新的列表l1，即l1=[2,4,6,8]
l1=L[1::2] 表示从L[1]开始每隔两个位置取一个数
"""

"""
功能：zip 函数是可以接收多个可迭代对象，
然后把每个可迭代对象中的第i个元素组合在一起，形成一个新的迭代器，类型为元组。
c=zip(L1,L2)
然后取出迭代器中的元素的方法
方法一：print(next(c))
方法二：list(c) 把元组转换成列表，然后依次取出
"""









