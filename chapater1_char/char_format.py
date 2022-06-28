#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/16 001620:47
# 文件名称:char_format
# 开发工具:PyCharm
"""
格式化：
1. %d %s %f
   print("王思聪说：%s"%sss)
2.format
# {}起到占位的作用
# {}方括号里面的序号起到标识format变量的序号，可以实现变量的复用 ，这种索引从0开始
# {}用变量名的形式，则format里面的参数必须是关键子参数
"""
name ="王思聪"
age=33
s=53
print('王思聪:%s，%d，%f'%(name,age,s))

# {}起到占位的作用
result='舔狗{}今年{}岁，爱上张一宁'.format(name,age)
print(result)

# {}方括号里面的序号起到标识format变量的序号，可以实现变量的复用 ，这种索引从0开始
result='舔狗{0}今年{1}岁，爱上张一宁,可惜张一宁不爱{0}'.format(name,age)
print(result)

# {}用变量名的形式，则format里面的参数必须是关键子参数
result='舔狗{name}今年{age}岁，爱上张一宁,可惜张一宁不爱{name}'.format(name='王思聪',age='33')
print(result)

