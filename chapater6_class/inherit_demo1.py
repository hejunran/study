#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/29 002914:21
# 文件名称:inherit_demo1
# 开发工具:PyCharm
"""
继承：继承描述的是事务之间的所属关系 子类在继承的时候，在定义类时，小括号（）中为父类的名字，父类的属性，方法否会被继承给子类。
在python中继承中的一些特点： 
  1：在继承中基类的构造（init()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。 
  2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数 
  3：Python总是首先查找对应类型的方法，如果它不能在派生类（子类即当前类）中找到对应的方法，它才开始到基类(父类)中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。 
  4：由上面的关系，可以进行方法的重写，在子类中重写父类方法

"""
class SchoolMember():
    "学校成员的基类"
    number=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.enroll()

    def enroll(self):
        "注册"
        print("刚刚注册了一名新成员，名字为{}".format(self.name))
        SchoolMember.number +=1

    def remove(self):
        '离职'
        print('刚刚一名职员离职了，名字为{}'.format(self.name))
        SchoolMember.number -= 1

    def __str__(self):
        " 类对象的一个描述方法"
        """返回一个对象的描述信息"""
        return "名字是%s，年龄是%d"%(self.name,self.age)

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):           # 这是初始化，传入参数   # 先继承，再重构
        """
        继承类的构造方法：
        1.经典类的写法： 父类名称.__init__(self,参数1，参数2，...)
        2. 新式类的写法：super(子类，self).__init__(参数1，参数2，....)
        """
        super(Teacher, self).__init__(name,age,sex)
        # SchoolMember.__init__(name=name,age=age,sex=sex) 这个和super()都是子类调用父类方法的
        self.salary=salary
        self.course=course

    def teach(self):
        print("{}老师，年龄：{}，性别：{}，任教科目：{}，薪酬：{}".format(self.name,self.age,self.sex,self.course,self.salary))

class Students(SchoolMember):
    def __init__(self,name,sex,age,course,tuition):
        SchoolMember.__init__(self,age=age,name=name,sex=sex)
        self.course=course
        self.tuition=tuition

    def pay_tuition(self):
        print('学生姓名：%s,性别：%s，年龄：%d，交学费：%s'%(self.name,self.sex,self.age,self.tuition))

if __name__ == '__main__':

    teacher1=Teacher(name='赵凯敏',age=23,sex='女',course='数学',salary=5000)
    teacher1.teach()
    print(teacher1.__str__())   # 继承了父类的__str__()方法
    stu=Students(name='贺俊然',age=25,sex='男',course='物理',tuition=50000)
    print(teacher1.number)
    teacher1.remove()
    print(teacher1.number)
    print(stu.number)