#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/26 002615:40
# 文件名称:list_推导式
# 开发工具:PyCharm

# 列表推导式
"""
格式：
一：[ i for i in 可跌代的]
二：[i for i in 可跌代的  if 条件] 此时列表中i的值取决于if后面的条件
三：[结果一 if 条件一 else 结果二 for i in 可迭代 ]
四：[结果一 if 条件一 else 结果二 for i in 可迭代 if 条件二]
"""
list1=[i for i in range(1,21)]
print(list1)

list2=[i+2 for i in range(1,21)]
print(list2)

# 将0到100之间的偶数放到列表中
list3=[i for i in range(0,101,2)]
print(list3)
list4=[i for i in range(0,101) if i%2==0]
print(list4)

# 把list中全部的单词取出来，组成一个新列表
lists=['hello','123','world','luck','88','height']
list5=[i for i in lists if i.isalpha()]
print(list5)
# 把list中全部的单词取出来，组成一个新列表，如果单词时h开头的首字母大写,不是h开头的全部转大写
list6=[world.title() if world.startswith('h') else world.upper() for world in lists if world.isalpha()]
print(list6)

# 双重for循环格式
a=[(x,y) for x in range(0,11) for y in range(0,11)]
print(a)
#  [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)
#  , (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
#  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
#  (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
#  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
#  (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
#  (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
#  (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
#  (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
#  (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
#  (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]

a = [i for i in range(1,101)]
b =[a[x:x+3] for x in range(0,len(a),3)]
print(b)

# names=[['tom','billy','jefferson','andrew'],['alice','jill','Jenffier']]
names=[['tom','billy','jefferson','andrew'],['alice','jill','Jenffier']]
b = [j for i in names for j in i if j.count('e')>=2]
print(b)