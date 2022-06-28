"""
按多个字段分组查询

"""
import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    port=3306,
    db='myemployees',
    charset='utf8'
)
cur =conn.cursor()

# 案例： 查询每个部门每个工种的员工的平均工资
sql=" select avg(salary),department_id,job_id from employees group by department_id,job_id"
cur.execute(sql)
data =cur.fetchall()
print(data)

# 多组查询，添加排序
#  案例： 查询每个部门每个工种的员工的平均工资，并且按平均工资高低显示
sql=" select avg(salary),department_id,job_id from employees group by department_id,job_id order by avg(salary)"
cur.execute(sql)
data =cur.fetchall()
print(data)