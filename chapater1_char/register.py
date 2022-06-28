#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/16 001619:41
# 文件名称:register
# 开发工具:PyCharm
"""
要求：用户名：全部小写，首字母不能是数字，长度必须要6位以上
     手机号：长度为11位，纯数字
     密码：必须是6位数字
"""
# 第一True 可以改为Flag =True 用Flag标志位来控制循环的结束
while(True):
    user_name=input('please input user name or telephone number:')
    # 首字母的不能是数字还可以写为  user_name[0].isalpha（）
    if (len(user_name)>=6 and user_name.islower() and not user_name[0].isdigit()) or (len(user_name)==11 and user_name.isdigit()):
        while(True):
            password = input("请输入你的密码：")
            if len(password)==6 and password.isdigit():
                if user_name=='admin123' or user_name=='12345678912':
                    if password== '123456':
                        print("登录成功")
                        break
                    else:
                        print("用户和密码不匹配")
                        break
                else:
                    print("用户名或手机号不对")
                    break
            else:
                print('密码输入错误')
                continue
        break
    else:
        print("用户名或手机号错误")
        continue
