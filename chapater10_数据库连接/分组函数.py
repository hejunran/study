"""
二：分组函数
功能：用作统计使用，又称为聚合函数或统计函数或组函数
分类：
sum 求和，avg 平均值，max 最大值， min 最小值，count 计算个数

特点 ：
    1. sum,avg一般用于处理数值类型数据
    2.max，min，count可以处理任何类型
    3.是否忽略null值
        上面所有分组函数计算时候都忽略null值
    4.可以和关键字distinct搭配使用

    5.count函数的详细介绍
        SELECT COUNT(salary) FROM employees;
        SELECT COUNT(*) FROM employees;      # 这个用于统计行数
        SELECT COUNT(1) FROM employees;       # 相当于加了一列数值为1（这个1可以换成任义常数）的常量，这相当于统计行数
        效率
            MYISAM存储引擎下， count(*)的效率高
            INNODB存储引擎下，count(*)和count(1)的效率差不多，比count(字段）要高一些。
            count(*) 这种不需要判断这个列值是否为空，所以会更快

    6.和分组函数一同查询的字段一般要求是group by后的字段
"""

import pymysql
"简单使用"
conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='123456',
    port=3306,
    db='myemployees',
    charset='utf8'
)

cur = conn.cursor()
sql = "select sum(salary) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# avg
sql = "select avg(salary) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# max
sql = "select max(salary) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# min
sql = "select min(salary) from employees"
cur.execute(sql)
data=cur.fetchall()
print(data)

# 和distinct组合使用
sql=" SELECT COUNT(DISTINCT salary),COUNT(salary) FROM employees "
cur.execute(sql)
data=cur.fetchall()
print(data)