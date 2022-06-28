#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/3 000320:28
# 文件名称:类_new和init方法
# 开发工具:PyCharm
"""
__new__（）:
    1.__new__（）创建和返回一个新的对象。通俗说：是用来创建实例对象的
        Python中存在于类中的构造方法__init__（）负责将类实例化，而在__init__（）执行之前，
        __new__（）负责制造这样的一个实例对象，以便__init__（）去让该实例对象更加的丰富（为其添加属性等）
    2.__new__方法接受的参数和__init__一样，因为__init__是在类实例创建之后调用，而 __new__方法正是创建这个类实例的方法。
    3.必须要有返回值，返回值是实例化出来的实例，在自己实现__new__()时需要注意：
        可以return父类（super（当前类名，cls）.__new__())的实例
        也可以直接调用object的__new__出来的实例。
        形式：
        return super(当前类名，cls).__new__(cls)
        或者：
        return object.__new__(cls)
__init__()：
    1.__init__()的作用是初始化某个类的一个实例
__call__()
    __call__()的作用是使实例能够像函数一样被调用，同时不影响实例本身的生命周期（__call__()不影响一个实例的构造和析构）。但是__call__()可以用来改变实例的内部成员的值。
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __new__(cls, name, age):
    def __new__(cls, *args, **kwargs):                # 这种写法，不论init里面传什么参数，new都可以保持与其一直
        print('__new__被call')
        print(args)
        # return super(Person, cls).__new__()         # 这种写法报错，参数不够，实例化后的对象要如何给
        return super(Person,cls).__new__(cls)         # 等价于return object.__new__(cls)，new的参数返回写的时候不用传递
        # return object.__new__(cls)
    def __call__(self, *args, **kwargs):
        print(args)            # 元组
        print(kwargs)          # 字典
        self.name='zhaokaimin'
        self.age=28
        print('姓名：{}，年龄：{}'.format(self.name,self.age))

p = Person('hejunran',30)
print(p.name)
print(p.age)
p()             # 像函数一样被调用，call
