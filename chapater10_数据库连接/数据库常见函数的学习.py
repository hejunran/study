"""
进阶四：常见函数的学习

功能：类似于java的方法，将一组逻辑语句封装在方法中，对外暴露，
好处：
    1.隐蔽实现的细节，
    2.提高代码的重用性

调用：
    select 函数名(实参列表) 【from 表】

特点：
    1.叫什么（函数名）
    2.干什么（函数功能）

分类：
    1.单行函数
    如 concat，length，ifnull等
    2.分组函数
    功能：做统计使用，又统计函数，组函数

单行函数：
    分类：字符函数，数学函数，日期函数，其他函数，流程控制函数
    字符函数：length,concat,substr,instr,trim,upper,lower,lpad,rpad,replace
    数学函数：round，ceil，floor，truncate，mod
    日期函数：now，curtime，curdate，year，month，monthname，day，hour，minute，second，str_to_date,date_format
    其他函数：version，database，user
    控制函数：if，case

"""
import pymysql

"第一类：字符函数"
# length 计算字符长度
conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='123456',
    port=3306,
    db='myemployees',
    charset='utf8'
)
cur = conn.cursor()
sql = "select length('jion')"
cur.execute(sql)
data=cur.fetchall()
print(data)

sql = "select length('张三丰hahaha')"
cur.execute(sql)
data=cur.fetchall()
print(data)

# concat 拼接字符
sql="select concat(last_name,'_',first_name) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# upper,lower
sql="select upper('john')"
cur.execute(sql)
data=cur.fetchall()
print(data)
# 案例把员工表中姓变大写，名变小写，中间用下划线拼接
sql = " select concat(upper(last_name),'_',lower(first_name)) from employees"         # 可以看出函数可以嵌套调用
cur.execute(sql)
data=cur.fetchall()
print(data)

# substr，substring 截取字符串
sql = " select substr('李莫愁爱上了陆展元',6) out_put"    # out_put 为别名，mysql中字符串的索引从1开始，6是从指定位置截取字符
cur.execute(sql)
data=cur.fetchall()
print(data)             # (('了陆展元',),)

sql = " select substr('李莫愁爱上了陆展元',1,3) out_put"    # out_put 为别名，mysql中字符串的索引从1开始
cur.execute(sql)
data=cur.fetchall()
print(data)  # (('李莫愁',),)
# 案例：姓名中首字符大写，其他字符小写，然后用下划线拼接，显示出来
sql="select concat(concat(upper(substr(last_name,1,1)),lower(substr(last_name,2))),'_',concat(upper(substr(first_name,1,1)),lower(substr(first_name,2)))) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# instr 返回子串第一次出现的索引，如果找不到返回0
sql=" select instr('杨不悔爱上了殷六侠','殷六侠') as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)

# trim 去除字符串中的前面和后面的字符
sql=" select trim('  张翠山   ') as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # (('张翠山',),)

sql=" select trim('a' from 'aaaaaaa张aaa翠aaa山aaaaaaa') as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # (('张aaa翠aaa山',),)

sql=" select trim('aa' from 'aaaaaaa张aaa翠aaa山aaaaaaa') as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # (('a张aaa翠aaa山a',),)

# lpad 用指定字符左填充到指定长度，当长度小于字符（串）长度会发生截取，rpad是右填充
sql = " select lpad('殷素素',10,'*') out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)    # (('*******殷素素',),)

sql = " select rpad('殷素素',12,'a*') out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)    # (('殷素素a*a*a*a*a',),)

# replace 把字符串中某个字符都用另一个字符替换了（全部替换）替换
sql = "select replace('张无忌爱上了周芷若，后来爱上的赵敏','周芷若','赵敏') as out_put"   # 赵敏替换周芷如
cur.execute(sql)
data=cur.fetchall()
print(data)

"第二类：数学函数"
# round 四舍五入
sql = "select round(4.25) as out_put"   # 赵敏替换周芷如
cur.execute(sql)
data=cur.fetchall()
print(data)   # ((Decimal('4'),),)
sql = "select round(-4.65) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)    # ((Decimal('-5'),),)

sql = "select round(-4.654,2) as out_put"   # 第二个参数表示保留小数点后两位
cur.execute(sql)
data=cur.fetchall()
print(data)    # ((Decimal('-4.65'),),)

# ceil 向上取整 ，返回大于等于该参数的最小整数    floor 向下取整，返回小于等于该参数的最大整数
sql = "select ceil(-4.654) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)   # ((-4,),)
sql = "select floor(-4.654) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # ((-5,),)

# truncate 截断, 截断小数点后几位。
sql = "select truncate(-4.654,2) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)         # ((Decimal('-4.65'),),)
sql = "select truncate(-4.654,1) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # ((Decimal('-4.6'),),)

# MOD取余 其实进行了 a- a/b *b
sql = "select mod(10,3) as out_put"
cur.execute(sql)
data=cur.fetchall()
print(data)  # ((1,),)
sql = "select mod(-10,-3) as out_put"   # -10-(-10)/(-3) *(-3) =-1
cur.execute(sql)
data=cur.fetchall()
print(data)   # ((-1,),)
sql = "select mod(10,-3) as out_put"   #10-10/(-3) *(-3) =-1
cur.execute(sql)
data=cur.fetchall()
print(data)     # ((1,),)


"第三类：日期函数"
# now函数 返回当前系统日期+时间
sql = "select now()"
cur.execute(sql)
data=cur.fetchall()
print(data)  # ((datetime.datetime(2021, 7, 29, 15, 52, 8),),)

# curdata()函数， 返回当前系统日期，不包含时间，
# curtime()函数，返回当前系统时间，不包含日期

# 获取指定的部分，如年，月，日，小时，分钟，秒
# 获取年
sql = "select year(now()) 年"     # 年 是重命名
cur.execute(sql)
data=cur.fetchall()
print(data)            # ((2021,),)

sql = "select year('1998-9-21') 年"     # 年 是重命名
cur.execute(sql)
data=cur.fetchall()
print(data)            # ((1998,),)

sql = "select year(hiredate) 年 from employees"     # 年 是重命名
cur.execute(sql)
data=cur.fetchall()
print(data)

# 获取月 month() 函数获取月份，是数字
sql = "select month(hiredate) 月 from employees"     # 月 是重命名
cur.execute(sql)
data=cur.fetchall()
print(data)

# monthname()函数是获取月份的函数，是英文的表示
sql = "select monthname(hiredate) 月 from employees"     # 月 是重命名
cur.execute(sql)
data=cur.fetchall()
print(data)

# str_to_date:将日期格式的字符串转换成指定的日期
"""
%Y   四位数的年份
%y   2位数的年份
%m   月份（01,02,03，...）
%c   月份（1,2,3，...,12）
%d   日（01,02,03，...）
%H   小时（24制）
%h   小时（12制）
%i   分钟（00,01，...，59）
%s   秒（00.01,02，...，59）
"""
sql="select str_to_date('1998-3-2','%Y-%c-%d') "
cur.execute(sql)
data=cur.fetchall()
print(data)

# 查询入职日期为1992-4-3的员工信息
sql = "select * from employees where hiredate =str_to_date('1992-4-3','%Y-%c-%d')"    # 注意数据库判断两个字符相当用 = ,而不是 ==
cur.execute(sql)
data=cur.fetchall()
print(data)
sql = "select * from employees where hiredate =str_to_date('4-3 1992','%c-%d %Y')"    # 注意数据库判断两个字符相当用 = ,而不是 ==
cur.execute(sql)
data=cur.fetchall()
print(data)

# date_format()函数，把日期转换成字符
sql = "select date_format(now(),'%Y年%m月%d日')  as out_put"    # 注意数据库判断两个字符相当用 = ,而不是 ==
cur.execute(sql)
data=cur.fetchall()
print(data)

# 查询有奖金的员工名和入职日期（**月/**日 **年）   实际应用的格式要求
sql=" select last_name,date_format(hiredate,'%c/%d %Y') from employees where salary>0"
cur.execute(sql)
data=cur.fetchall()
print(data)


"其他函数 "
# VERSION() 查询数据库的版本号
# DATABASE() 查询当前的库
# USER() 查询当前的用户

"流程控制函数"

# if函数  实现程序中的if else的功能
# if()函数中有三个参数，第一个参数为if的判断条件表达式，第二个为条件成立执行的表达式，然后把结果返回，第三个参数为条件不成立时执行的表达式，返回执行结果
sql="select if(10>5,1,0)"
cur.execute(sql)
data=cur.fetchall()
print(data)
# 查询员工是否有奖金
sql="select last_name, if(salary,'有奖金','没奖金') from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# case()函数  作用一：类似于java中的switch case的效果
"""
case()函数  

作用一：类似于java中的switch case的效果
java中：
switch(变量或表达式){
    case 常量1：语句1；break；
    ....
    default:语句n;break;
}

mysql中，case要判断字段或者表达式
when 常量1 then 要显示的值为1或者语句1；
when 常量1 then 要显示的值为1或者语句1；
...
else 要显示的值n或者语句n；
end

作用二：类似于多重if
java中
if(条件1){
    语句1
}else if(条件1){
    语句2
}
...
else{
    语句n
}

mysql中
case
when 条件1 then显示值1或者语句1
when 条件2 then显示值2或者语句2
...
else:要显示的值n或者语句n；
end

"""
# 案例： 查询员工工资，要求：
# 部门号=30，显示的工资为1.1倍
# 部门号=40，显示的工资为1.2倍
# 部门号=50，显示的工资为1.3倍
# 其他部门号，显示原工资
sql=" select salary 原始工资,department_id, case department_id when 30 then salary*1.1 when 40 then salary*1.2 when 50 then salary*1.3 else salary end as 新工资 from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例： 查询员工工资，要求：
# 如果工资>20000，显示的工资为A级别
# 如果工资>15000，显示的工资为B级别
# 如果工资>10000，显示的工资为C级别
# 否则 显示工资为D级别
sql =" select salary, case when salary>20000 then 'A' when salary>15000 then 'B' when salary>10000 then 'C' else 'D' end as '工资级别' from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)