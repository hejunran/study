"""
一：数据库的好处
1.可以持久化数据到本地
2.结构化查询

二：数据库常见概念
1.db：数据库，存储数据的容器
2.dbms：数据库管理系统，数据库软件，或者数据库产品，用于创建管理db
3.sql：结构化查询语言，用于和数据库通信的语言，不是某个数据库软件独有的，几乎是所有主流数据库通用的语言

三：数据库存储的特点’
1.数据存放在表中，表再放在库中
2.一个库可以有多张表，每张表都具有唯一的表名来标识自己
3，表中有一个或者多个列，列又被称为子段，相当于Java中的‘属性’
4.表中的一行数据，相当于Java中‘对象’

四：常见的数据库管理系统
mysql，oracle，sqlserver，db2

五：mysql相关介绍
1.mysql的背景
    前身属于瑞典的一家公司，Mysql，AB，然后08年被sun公司收购了，09年sun被oracle收购
2.mysql的优点
    开源，免费，成本低； 性能高，移植性好； 体积小，便于安装
3.mysql的安装
    属于c/s架构的软件，一般来讲安装服务端
4.mysql服务的启动和停止
    方式一：命令行方式
    net start 服务名
    net stop 服务名
    方式二：计算机，右击，管理，服务
5.mysql服务的登录和退出
    登录：mysql [-h 主机名 -p 端口号] -u 用户名 -p密码
    退出：exit或者ctrl + c

6.mysql查询
    基础查询
        语法：
            select 查询列表 from 表名；
        类似于： system.out.println(打印的东西);
        特点：
            1.查询列表可以是：表中的字段，常量值，表达式，函数
            2.查询的结果是一个虚拟的表格
        isnull函数， 判断某个字段或者表达式是否为null，如果为空返回1，否者返回0
        ifnull函数，判断某个字段或者表达式是否为null，如果是空返回指定值，否者返回原本的值  ifnull(commission_pct,0),如果commission_pct为空，返回指定值0
    条件查询
        语法
            select 查询列表 from 表名 where 筛选条件；

"""


import pymysql
# 连接数据库
conn=pymysql.connect(host='127.0.0.1',    # 连接的地址
                     user='root',         # 数据库用户名
                     passwd='123456',     # 密码
                     port=3306,           # 端口 端口类型为整数
                     db='myemployees',    # 数据库名称
                     charset='utf8'      # 字符串编码
                     )
cur =conn.cursor()          # 生成游标对象
sql = "select * from employees"    # sql查询语句
cur.execute(sql)                 # 执行查询语句
data = cur.fetchall()           # 通过fetchall方法获得数据

for i in data[:2]:
    print(i)                      # 此时拿出来的数据是一个元祖类型

# 查询员工id
sql1 = 'select employee_id from employees'
cur.execute(sql1)
data1 = cur.fetchall()
for i in data1[:3]:
    print(i)

# 查询多个字段
sql2 = 'SELECT last_name, salary,email FROM employees'
cur.execute(sql2)
data2 =cur.fetchall()
for i in data2[:6]:
    print(i)

# 起别名查询
sql3 ='SELECT last_name AS 姓,first_name AS 名 FROM employees'
cur.execute(sql3)
data3 =cur.fetchall()
for i in data3[:3]:
    print(i)

sql4 ='SELECT CONCAT(last_name,first_name) AS 姓名 FROM employees'
cur.execute(sql4)
data4 =cur.fetchall()
for i in data4[:3]:
    print(i)

cur.close()                 # 关闭游标
conn.close()                # 关闭连接
