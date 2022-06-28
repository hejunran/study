import pymysql
"""
条件查询
语法： 
    select 查询列表
    from 表名
    where 筛选条件

分类：
    一： 按条件表达式进行筛选
    简单条件运算符： >, <, =, !=, <>, >=, <=
    二：按逻辑运算符进行筛选
    逻辑运算符：
        &&  || ！
        and or not
        && 如果两个条件都为true，则结果为true
        or 若果两个条件一个为true，则结果为true
    三：模糊查询
        like
        between and
        in
        is null
        
    
"""

conn = pymysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='123456',
                    port=3306,
                    db='myemployees',
                    charset='utf8'
                    )
cur = conn.cursor()     # 生成连接游标

" 按条件表达式查询 "
# 案例一：查询工资大于12000的员工信息
sql='select * from employees where salary > 12000'
cur.execute(sql)             # 执行查询语句
data =cur.fetchall()
print(data)
print(len(data))

# 案例二：查询部门编号不等于90号的员工名和部门编号
# sql='select first_name,department_id from employees where department_id !=90'   # != 和<>是等价的。
sql='select first_name,department_id from employees where department_id <>90'
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))

" 按逻辑表达式进行查询"
#案例一：查询工资在10000到20000之间的员工名，工资，奖金
sql='select first_name,salary,commission_pct from employees where salary >10000 and salary <20000'
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))

# 案例二：查询部门编号不在90到110之间的，或者工资高于15000的员工信息
# sql='select * from employees where salary >15000 or department_id>110 or department_id<90'
sql='select * from employees where salary >15000 or not(department_id<=110 and department_id>=90)'
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))

"模糊查询 like, between and, is null, is not null"
# 案例一：查询员工名中包含字符a的员工信息
# like通常与通配符一起使用，% ,_ 这两都是通配符
sql = " select * from employees where last_name like '%a%' "     # % 通配符，代表任意个数的字符
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))
# 案例二:查询员工名中第三个字符为e，第五个字符为a的员工名和工资
sql = " select first_name,salary from employees where last_name like '__e_a%' "     # _ 通配符，代表一位的字符
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))
# 案例三：查询员工名中第二个字符_为员工名
# sql = " select last_name from employees where last_name like '_\_%' "     # 用反斜杠作为转移字符
sql = "SELECT last_name FROM employees WHERE last_name LIKE '_$_%' ESCAPE '$' "     # 用特殊字符作为转移字符，然后用关键词escape
cur.execute(sql)
data =cur.fetchall()
print(data)
print(len(data))

"""
between and 
1.提高语句的简洁度
2.包括边界值
3.临界值不要调换顺序，and前面是小值，后面是大的值
"""
#案例：查询员工编号在100到120之间的所有的员工信息
sql ='select * from employees where employee_id between 100 and 120'
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

""" 
in 等价于 = 
含义：判断某个字段的值是否属于in列表中的某一项
特点：
    1.使用in提高语句的简洁度
    2.in列表的值类型必须一致或者兼容
    ‘123’,123
    3.不支持_,%这些通配符，因为in 等价于 =，不是like
"""
# 查询员工的工种编号是：IT_PROG,AD_VP,AD_PRES中的一个员工名和工种编号
sql="select last_name,job_id from employees where job_id in ('IT_PROG','AD_VP','AD_PRES')"
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

"""
is 只是和null 和not null配合使用，别的不行
"""
# 案例： 查询没有奖金的员工名和奖金率
sql='select last_name,commission_pct from employees where commission_pct is null'
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

sql='select last_name,commission_pct from employees where commission_pct is not null'
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

"""
安全等于
<=>
可以判断某个键值是否为空
可以判断某个数是否为某个值
"""
sql='select last_name,commission_pct from employees where commission_pct <=> null'
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

sql='select last_name,salary from employees where salary <=> 12000'
cur.execute(sql)
data = cur.fetchall()
print(data)
print(len(data))

