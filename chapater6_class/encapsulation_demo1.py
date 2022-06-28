#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/29 002915:39
# 文件名称:encapsulation_demo1
# 开发工具:PyCharm

# 面向对象编程的三大特性之一：封装
"""
封装是将数据的具体操作和实现代码放在某个对象的内部，使得这些这些实现的细节不被外界发现，外界只能通过接口使用该对象
封装的是对象的属性和行为（函数）
1.封装是面向对象编程的核心思想，将对象是属性和方法（函数）进行封装起来，而将对象的属性和方法封装起来的载体就是类，类通常对客户隐藏其实现细节，这就是封装。
"""

class Book:                                   #  类的名字首字母必须要大写
    def __init__(self,name,price,author):     # 这是类的初始化方法，在实例化类的时候必须传入init方法中相应的参数
        "  __init__方法（类的属性，给类加属性）—创建方法时会被自动调用  "
        """
        （1）、__init__方法的第一参数永远是self
        表示创建的类实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        （2）、有了__init__方法 在创建实例的时候，就不能传入空的参数了，
        必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去：

        """
        self.name=name                       # 这些是类的属性
        self.author=author
        self.price=price

    def print_book_info(self):
        print('{}的作者是{}，价格是{}'.format(self.name,self.author,self.price))

class Hero:
    job='法师'                        # 注意此处的job，在此类别的方法中调用，也要用self.job
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def print_hero_info(self):
        print('英雄{}，性别{}'.format(self.name,self.gender))
        print('英雄{},性别{},职位{}'.format(self.name,self.gender,self.job))

" 类的属性私有化，只有类的内部可以访问，外部不可以访问 "
class Students:
    def __init__(self,name,score):
        # 属性私有化，就是在属性名字前面加两个下划线，后面不能再加两条下划线，那样就不是私有化属性啦
        self.__name=name
        self.__score__=score

    def get_name(self):
        # 如果类的外部一定要获取私有化属性，则可以通过构建公共方法来获取和修改其值
        return self.__name

    def set_name(self,name):
        self.__name=name


"组合使用，一个类的属性，为另一个类的实例化对象"
class School:
    def __init__(self,student_name,student_score,book_name,book_author,book_price):
        self.stduent=Students(student_name,student_score)
        self.book=Book(book_name,author=book_author,price=book_price)
    def print_school_info(self):
        self.book.print_book_info()
        print('学生姓名{}，分数{}'.format(self.stduent.get_name(),self.stduent.__score__))

if __name__ == '__main__':
    b=Book('红楼梦',author='曹雪芹',price=35)
    print(b)                        # 此处返回的是该类实例化后放在内存中的地址

    h=Hero('王昭君','女')
    h.print_hero_info()
    print(h.job)

    s=Students('hejunran',50)
    # print(s.__name)
    print(s.__score__)
    print(s.get_name())
    s.set_name('wangzhe')
    print(s.get_name())

    school=School(book_name='三国演绎',book_author='罗贯中',book_price=35,student_name='hejunran',student_score=98)
    school.print_school_info()

    " python中有一些内置的函数  "
    " 1. issubclass(A,B) 用于检测一个类是否属于另一个类的子类，A是不是B的子类"
    print(issubclass(School,object))
    " 2.isinstance(A,B) 检测一个实例对象是否属于一个类,对象A是否属于B"
    print(isinstance(school,School))
    print(isinstance(b,School))
    print(isinstance(school,object))    # True
    "3.hasattr测定一个对象是否有某个属性（name要以字符串的形式，否则函数会以为x是一个变量） "
    print(hasattr(school,'stduent'))
    "4.setattr(A,name,value),设置对象A中属性name的值，切记name必须是公共属性，不然改不了"
    setattr(s,'__name','hello')
    print(s.get_name())