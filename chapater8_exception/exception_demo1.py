#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/2 000215:49
# 文件名称:exception_demo1
# 开发工具:PyCharm
"""
异常：程序运行时产生的错误
格式：
try：
    可能出现异常的代码
except:
    如果有异常执行的代码
[finnaly:
    无论是否存在异常都会执行的代码]

情况一：try里面有可能产生多个异常，except后面可以跟异常的类型
    try：
        执行代码
    except 异常类型1：
        异常执行的代码
    except 异常类型2
        异常执行的代码
    但是最后基类Expection要放在最后
情况二：
    try：
        执行代码（可能会产生异常的代码）
    except 异常类型1：
        发生异常，执行的代码
    except 异常类型2
        发生异常，执行的代码
    expect Expection as err：    ------>此处相当于异常的对象实例
        print（err）    -------->打印出错误原因
情况三：
try :
    执行代码（可能会产生异常的代码）
expect 异常类型：
    发生异常，执行的代码
else：
    不发生异常，依赖于try块内部的代码成功执行后，而执行的代码。
finally：
    这个是无论是否有异常都会执行这块代码

情况四：
raise抛出异常，外部接住异常（raise是一个主动的过程）

"""
def func():
    try:
        n1 = int(input('输入第一个数字：'))
        n2 = int(input('输入第二个数字：'))
        operational = input('请输入你输入的运算符号：')
        result=0
        if operational=='+':
            result =n1 + n2
        elif operational=='-':
            result = n1 - n2
        elif operational=='/':
            result = n1 / n2
        elif operational=='*':
            result = n1 * n2
        else:
            print('符号错误!')
    except ZeroDivisionError:
        print('除数不能为0')
    # except ValueError:
    #     print('输入必须是数字')
    except Exception as err:              # Exception 是所有异常的基类，此处加个 as err ，然后在打印一下，就可以知道具体的错误是啥啦，在那个位置
        print('ccccc',err)
    else:
        print(result)

# func()

def register():
    uesername = input('用户名：')
    if len(uesername)<6:
        raise Exception('用户名长度必须大于6')              # raise是主动抛出异常，不是系统抛出的异常。外部需要接住这个异常
    else:
        print('输入用户名是：',uesername)
    password = input('密码：')
    if len(password)<6:
        raise Exception('密码长度不低于六位')
    elif password.isdigit() or password.isalpha():
        raise Exception('密码必须包含字符和数字')
    else:
        print('密码输入正确。')

try :
    register()
except Exception as err:
    print(err)
else:
    print('注册成功')

