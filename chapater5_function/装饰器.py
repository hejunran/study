# _*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/1 000115:25
# 文件名称:装饰器
# 开发工具:PyCharm

def foo():
    print('foo')

def func():
    print('func')

foo = func       # 此时函数的名字相当于一个地址指针
foo()            # func



"""
装饰器：
遵循开放封闭的原则，在不改变原函数的情况下，扩展函数功能
定义：
def aaa(func):
    def xxx(参数，。。。)
        ...
        func()
        ...
        return xxx
装饰：
@装饰器名  ------->原函数 = 装饰（原函数）
def 原函数():
    pass
  
带参数的装饰器：
如果原函数有参数，则装饰器内部也要有参数  
功能;
    1.引入日志
    2.函数执行时间统计
    3.执行函数前预备处理处理
    4.执行函数后的清理功能
    5.权限校验能场景
    6.缓存
    
"""
# 定义装饰器
def decorater(func):
    def wrapper():
        func()
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
    return wrapper

@decorater   # 等价于 house=decorater(house)
def house():
    print('毛坯房。。。。。')

house()


# 带参数的装饰器
def deccorate_new(func):
    def wrapper(adress):
        func(adress)
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
    return  wrapper

@deccorate_new
def house_new(address):
    print('房子的地址：{}是一个毛坯房'.format(address))

house_new('北京四合院')    #  -----》此时相当于wrapper，那么wrapper也要又参数



def deccorate_new2(func):
    def wrapper(*args):
        func(*args)      # ---->func就是house_new2, args是一个元组=('北京工业大学',1000)是一个元组，而house_new2是两个参数，故需要拆包，加*号
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')

    return wrapper

@deccorate_new2
def house_hotel(address):
    print('房子的地址：{}'.format(address))

@deccorate_new2
def house_new2(address,area):
    print('房子的地址：{}是一个毛坯房,面积是{}'.format(address,area))


house_new2('北京工业大学',1000)      # ----->相当于wrapper

house_hotel('天天')


# 多种参数组合，加关键字参数, 这样可以装饰任意函数
def deccorate_new3(func):
    def wrapper(*args,**kwargs):       # 不过调用时，切记前面的参数不能放关键字参数
        func(*args,**kwargs)      # ---->func就是house_new2, args是一个元组=('北京工业大学',1000)是一个元组，而house_new2是两个参数，故需要拆包，加*号
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')

    return wrapper

@deccorate_new3
def house_hotel3(address):
    print('房子的地址：{}'.format(address))

@deccorate_new3
def house_new3(address,area):
    print('房子的地址：{}是一个毛坯房,面积是{}'.format(address,area))

@deccorate_new3
def house_school(name,address,area):
    print('学校的名字是：{}，地址在：{}，面积是{}'.format(name,address,area))

house_new3('北京工业大学',1000)      # ----->相当于wrapper
house_school('北京工业大学','朝阳区',area=1000)



# 装饰器中的return
"""
原函数有返回值，那么装饰器中的内部函数也应有返回值，具体返回值是多少，可以根据实际情况而定
"""
def deccorate_new4(func):
    def wrapper(*args,**kwargs):       # 不过调用时，切记前面的参数不能放关键字参数
        r=func(*args,**kwargs)      # ---->func就是house_new2, args是一个元组=('北京工业大学',1000)是一个元组，而house_new2是两个参数，故需要拆包，加*号
        print('预计装修费用：{}元'.format(r))
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
        return 60000

    return wrapper

@deccorate_new4
def house_new4():
    print('毛坯房。。。')
    return 50000

r=house_new4()
print(r)