"""
分组查询:
分组数据：GROUP BY 子句语法
可以使用GROUP BY 子句将表中的数据分为若干组
select column，group_function(column)
from table
【where condition】
【GROUP BY  group_by_expression】
【ORDER BY column】
其中 condition是约束条件
group_by_expression是分组表达式
group_function是分组函数
column是某一列
ORDER BY column是按某一列排序

注意：
    查询列表必须是特殊，要求是分组函数和group by后出现的字段

特点：
一：分组查询的筛选条件分为两类：
                    数据源             位置                           关键字
    1.分组前筛选      原始表             group by 子句的前面             where
    2.分组后筛选      分组后的结果表       group by 子句的后面             having

分组函数做条件时候，一定放在having后面，不能放在where后面
能用分组前筛选的优先考虑分组前筛选。
二：group by 子句支持单个字段分组，多个字段分组(多个字段之间用逗号隔开没有顺序要求），表达式或函数用的较少
三：也可以添加排序，排序放在整个分组查询的最后

"""
import pymysql

conn =pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='123456',
    port=3306,
    db='myemployees',
    charset='utf8'
)

# 简单的分组查询
# 案例：查询每个工种的最高工资
sql="select max(salary),job_id from employees group by job_id"
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例：查询每个位置上的部门个数
sql="select count(*),location_id from departments group by location_id"
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 添加筛选条件
# 案例：查询邮箱中包含a字符的，每个部门的平均工资
sql="select avg(salary), department_id from employees where email like '%a%' group by department_id "
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例：查询有奖金的每个领导手下员工的最高工资
sql =" select max(salary),manager_id from employees where commission_pct is not null group by manager_id "
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 添加复杂的筛选条件
# 案例：查询那个部门的员工个数大于二
"""
分步:1.查询每个部门的员工个数，2.然后根据1的结果进行筛选，查询那个部门的员工个数大于2
having和group by组合使用，用于分组后的查询。
"""
sql="select count(*),department_id from employees group by department_id having count(*)>2"
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资
# 第一步：查询每个工种有奖金的员工的最高工资
sql="select job_id,max(salary) from employees where commission_pct is not null group by job_id"
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)
# 第二步：根据1的结果，筛选，最高工资大于12000的工种
sql="select job_id,max(salary) from employees where commission_pct is not null group by job_id having max(salary) >12000 "
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

# 案例：查询领导编号>102的每个领导手下的最低工资>5000的领导编号是哪个，以及其最低工资
sql = " select manager_id,min(salary) from employees where ifnull(manager_id,0)>102 group by manager_id having min(salary)>5000"
cur =conn.cursor()
cur.execute(sql)
data=cur.fetchall()
print(data)

