#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/13 001317:32
# 文件名称:char_address
# 开发工具:PyCharm
"验证字符串的地址是否一致"
"在python中有一个字符串的保留区，里面放着字符串"
s1 ='hello'   #  此处相当于把hello的地址传给了s1
s2 = s1       # 此处相当于把s1内容——hello的地址转给了s2
s3 ='hello'   # 此处是在字符串保留区中找到hello的地址，传给s3   故此时s1，s2，s3的地址是一致的
s4='hello1'
print(id(s1))   # id 输出的是变量的地址
print(id(s2))
print(id(s3))
print(id(s4))

# is比较的是内存地址
print(s1 is s2)

# 切片机制，字符串和列表
# str[start:end:step]  start 表示起点，end表示终点，step的正负值表示方向，step表示移动步长
s='ABCDEFG'
print(s[1:4])    # 截取是需要注意，前面包括，后面不包含
print(s[:5])
print(s[-3:-1])
print(s[-3:7])
print(s[-3:])

print(id(s[-3:-1]))
print(id(s[-3:7]))
print(id(s[-3:]))
# id在python中访问的是地址
x =s[:]
print(id(x))
print(id(s))

