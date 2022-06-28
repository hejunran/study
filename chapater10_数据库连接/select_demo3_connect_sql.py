"""
进阶三:排序查询
语法结构：
    select 查询列表
    from 表
    【where 筛选条件】
    order by 排序列表 【asc|desc】   # desc是降序排列，asc是升序排列

特点：
    1.默认是升序排列
    2.order by 支持单个字段，多个字段，表达式，函数，别名
    3.order by 一般是放在我们查询语句的最后面，limit子句除外。
"""

import pymysql

conn = pymysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='123456',
                    port=3306,
                    db='myemployees',
                    charset='utf8'
                    )
cur = conn.cursor()

# 案例：查询员工信息，按着工资从高到低进行排序
sql = "select * from employees order by salary desc"
cur.execute(sql)
data = cur.fetchall()
print(data)


# 案例：查询部门编号>=90的员工信息，要求按入职时间的先后排序
sql="select * from employees where department_id>=90 order by hiredate"
cur.execute(sql)
data = cur.fetchall()
print(data)

# 案例：按员工的年薪的高低显示员工的信息和年薪【按表达式排序】
sql="select * ,salary*12*(1+ ifnull(commission_pct,0)) 年薪 from employees order by salary*12*(1+ ifnull(commission_pct,0))"
cur.execute(sql)
data=cur.fetchall()
print(data)

# 按别名查询
sql="select * ,salary*12*(1+ ifnull(commission_pct,0)) 年薪 from employees order by 年薪"
cur.execute(sql)
data=cur.fetchall()
print(data)

# 按员工名的长度显示员工名和工资, 按函数排序
sql= 'select last_name,salary from employees order by length(last_name)'
cur.execute(sql)
data=cur.fetchall()
print(data)

# 查询员工信息，先按工资排序，再按员工编号排序【按多个字段排序】
sql='select * from employees order by salary asc , employee_id desc'
cur.execute(sql)
data=cur.fetchall()
print(data)