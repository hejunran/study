#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/13 001319:04
# 文件名称:char_options
# 开发工具:PyCharm

# 字符串常见操作：
"计算字符串长度：len"
"查找：find，index，rfind，ridex"
"判断：startswith，endwith，isalpha，isdight,isalnum,isspace，isupper，islower"
"计算字符出现的次数;count"
"替换内容：replace"
"切割字符串：split.rsplit,splitline,partition,rpartition"
"修改大小：capitalize,title,upper,lower"
"空格处理：ljust,rjust,center,lstrip,rstrip,strip"
"字符串拼接：join"

"find 从左向右找，只要遇到一个符合要求的则返回其位置，如果没有找到则返回-1"
"rfind 从右向左找，只要遇到一个符合要求的则返回其位置，如果没有找到则返回-1"
"index 从左向右找,也是表示查找，只不过当其查找不到时，会报错"
"rindex 从右向左找,也是表示查找，只不过当其查找不到时，会报错"
"count:统计某个字符出现的次数"
"startswith: 判断字符串是否以某个字符或字符串开头，值为True，False"
"endwith: 判断字符串是否以某个字符或字符串结尾，值为True，False "
"isalpha: 判断一个字符串是都字母组成，True or False"
"isdight： 判断一个字符串是否都是数字组成 ，True or False"
"isalnum： 判断一个字符串是否只有数字和字母组成，True or False"
"isspace： 判断一个字符串全是由空格组成 True or False,当时空串时返回的时false"
"isupper:"
"istitle"
"islower:"
"replace:  从左边开始替换字符串中的字符或者字符串，通过参数count控制替换的次数，默认全部替换"
"split:从左边切割字符串   rsplit：从右边切割字符串  通过maxsplit控制切割次数     返回值都是一个列表"
"splitlines: 按行切割"
"partition ,rpartition(分隔符)，分别是从左边切割和右边切割，把一个字符串分为左边部分，切割符，右边部分这个三个部分，组成一个三元组返回"
"capitalize: 一句话中第一个单词的首字母大写"
"title:字符串中，每个单词的首字母大写"
"ljust:添加空格 控制字符串的对齐方式，左对齐"
"rjust:添加空格 控制字符串的对齐方式，右对齐"
"center:参数  width, fillchar,width调整后字符串的总长度，中间对齐"
"lstrip:删除一个字符串左侧的空格"
"rstrip:删除一个字符串右侧的空格"
"strip:删除一个字符串左侧和右侧的空格，中间的空格不会删除"
"join: 字符串拼接， 把列表中的字符串拼接成一个字符串"

s ='  adm in   '
result=s.strip()
results = s.center(30)
print(len(result))
print(result)

path='https://blog.csdn.net/w926498/article/details/8_0579520'
print(path[::-1])
print(path.istitle())

print('*-'*20)
i =path.find('_')
print(i)
print(path[i+1:])

i =path.rfind('.')
print(i)
print(path[i+1:])

print('**'*20)
i=path.count('.')
print(i)
i=path.count('#')
print(i)


# 模拟文件上传，键盘输入文件名称，判断文件名是否大于6位，扩展名是否为jpg，png，gif格式，如果不是则提示上传失败，
#如果扩展名满足条件，名字长度小于6，则随机生成一个6为数字组成的文件名，打印成功上传 xxxxxx.png

import random
# print('请输入上传的文件名：')
flie_name=input('请输入上传的文件名：')
s=flie_name.endswith('png')
if flie_name.endswith('png') or flie_name.endswith('jpg') or flie_name.endswith('gif'):
    index=flie_name.rfind('.')
    name=flie_name[:index]
    if len(name)>=6:
        print('成功上传文件%s'%flie_name)
    else:
        n= random.randint(100000,999999)
        name=str(n)+flie_name[index:]
        print('成功上传文件%s\n' % name)
else:
    print('上传失败')


# 网站上产生验证码的方法
filename=''
s='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
for i in range(4):
    index=random.randint(0,len(s)-1)
    flie_name+=s[index]
print(flie_name)

s='王思聪， 喜欢张一宁，做舔狗很开心'
result = s.replace('王思聪','狗子')
print(result)
