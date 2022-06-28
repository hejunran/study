"""
进阶6 ：
连接查询，又称为多表查询
含义：当我们查询的字段来自多个表中

笛卡尔乘积现象：表1 有m行， 表2 有n列 结果为m*n列
    发生原因：没有有效的连接条件
    如何避免： 添加有效的连接条件
分类 ：
    1.按年代标准分类：
        sql92标准：仅仅支持内连接
        sql99标准【推荐使用】：支持内连接+外连接（左外和右外）+交叉连接
    2.按功能分类
        内连接：
            等值连接
            非等值连接
            自连接
        外连接：
            左外连接
            右外连接
            全外连接
        交叉连接

"""

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    port=3306,
    db='girls',
    charset='utf8'
)
cur =conn.cursor()

sql='select * from beauty'
cur.execute(sql)
data=cur.fetchall()
print(data)

""" 等值连接 """
# 案例1：查询女神名和对应的男神名
sql ="SELECT NAME,boyName FROM boys,beauty WHERE boys.id = beauty.boyfriend_id "
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例2： 查询员工名和对应的部门名
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    port=3306,
    db='myemployees',
    charset='utf8'
)
cur =conn.cursor()
sql=" select last_name,department_name from employees,departments where employees.department_id = departments.department_id"
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例3：