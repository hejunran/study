#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/21 002114:00
# 文件名称:dict_demo1
# 开发工具:PyCharm
"""
定义：字典对应键和值，是一一对应的，字典包括在{}中
键是不可以修改的，只可以修改键后面的值
字典名[key]=value
注意key是唯一的，如果在添加时出现相同的名字的key，则会修改原来key所对应的value值，如果没有相同的key，则会添加这对key和value

"""
# 字典初始化
"初始化方法一:"
star_result= {"易烊千玺": 400,"王源": 400,"王俊凯": 400}
print(star_result)

"初始化二：通过dict初始化，dict里面等号后面是key对应的值，等号前面是key"
"dict初始化时，前面的键值是不用加引号的，但是在访问时，是要加引号的"
dic2 = dict(book1='python学习',book2='深度学习')
print(dic2)
print(dic2['book1'])

"初始化方法三:通过fromkeys()方法创建一个字典中元素都有相同的值，如果没有给值，则为None"
"fromkeys(),前面放的是键名字，后面是值"
dic3 = dict.fromkeys(range(2), 1)
dic4 = dict.fromkeys(('x','y'),0)
print(dic3)
print(dic4)

"初始化方法四:利用zip方法进行创建" \
"zip方法是把两个可迭代的对象进行一一绑定"
dic5 =dict(zip('科研',[1,2]))
print(dic5)    # {'科': 1, '研': 2}

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))       #[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zip(x, y))
print(x == list(x2) and y == list(y2))
# True

# 键值的修改
star_result['易烊千玺']=500
print(star_result)
# 当没有这个键时，此时字典为自动添加这个键值对
star_result['于和伟']=600
print(star_result)

# 字典的删除
book={'书名':'《三体》','价格':50,'作者':'刘慈欣','出版社':'清华出版社'}
"方法一：pop删除，根据key实现删除，删除的是键值对，该方法的返回值为key对象的value"
r=book.pop('出版社')
print(r)
print(book)
"方法二;popitem删除,不用传任何参数，依次删除字典最后一对键值，如果字典为空，报错"
"该方法的返回值是key和value"
key,value=book.popitem()
print(key,value)
print(book)

"方法三：系统自带del方法进行删除"
"形式一：del 字典名[key]，这种类似于pop(key)"
"形式二：del 字典名，这种直接清除了这个字典"
del book['价格']
print(book)

# 字典的遍历
# get，get方法是根据key获取value值 ,如果没有该key时候，返回值为None或者传进行的形参默认值
# dict[key]获取value值，但是这种如果没有这个key，会keyerror报错
book={'书名':'《三体》','价格':50,'作者':'刘慈欣','出版社':'清华出版社'}
value=book.get('书名')     #
print(value)
value=book.get('书名1','默认值')     #
print(value)
# value=book['书名1']

'使用for进行遍历'
"使用for 进行遍历时，单独的for i in 字典名，此时的i返回的时key的值"
'获取键值对 ：items（）'
'获取键：keys（）'
'获取值：values（）'
for i in book:
    print(i)
for i in book.keys():
    print(i)
for i in book.values():
    print(i)
values=book.values()
print(book.items())      # items()把每一对键值放进一个元组里面
for i in book.items():
    print(i)
for key,value in book.items():
    print(key,value)
for key,value in zip(book.keys(),book.values()):
    print(key,value)

# setdefault,只可以用来添加键值对使用，不能用修改使用
book.setdefault('出版社','人民出版社')
print(book)

"字典的合并"
# update()支持两个字典的合并，但是 + 号是不能进行字典的合并，+号可以实现字符串和列表的合并
dict2={'a':1,'b':2}
book.update(dict2)
print(book)


