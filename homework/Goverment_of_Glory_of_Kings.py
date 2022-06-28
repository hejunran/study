#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/19 001917:01
# 文件名称:Goverment_of_Glory_of_Kings
# 开发工具:PyCharm
"""
王者荣耀角色管理系统
角色：姓名，性别，职业
添加角色
删除角色
修改角色
查询角色  单个角色
显示所有角色
退出系统
"""
import time

all_roles=[]  # 放置所有角色的容器
print('---------------------欢迎进入王者荣耀系统---------------------')
while True:
    options=input('请输入你想要的操作：1.添加角色，2.删除角色，3.修改角色，4.查询角色，5.显示所有角色，6.推出系统\n')
    if options==str(1):
        print('添加模块')
        flag=True
        ones_choice=True
        while flag:
            if ones_choice==True:
                name=input('请输入添加的角色名字：')
                sex = input('请输入该角色的性别：')
                job =input('请输入该角色的职业：')
                if sex in ['男','女']:
                    role=[name,sex,job]
                else:
                    sign=True
                    while sign:
                        sex=input('性别输入错误，请重新输入:')
                        if sex in ['男', '女']:
                            role = [name, sex, job]
                            sign=False
                all_roles.append(role)
                print('成功添加了角色{}进入王者荣耀系统'.format(name))
                choice=input('是否继续添加角色：Y(y) or N(n)')
            if choice=='Y'or choice=='y':
                continue
            elif choice=='N' or choice=='n':
                flag=False
                break
            else:
                ones_choice=False
                choice=input('输入错误，请重新选择是否添加角色：Y(y) or N(n)')
    elif options == str(2):
        print('删除模块')
        flag =True
        ones_choice=True
        while flag:
            if ones_choice ==True:
                role_name=input('请输入你想删除的角色名字：')
            sign = False
            for i in all_roles:
                if role_name in i:
                    delet_assure=input('是否删除角色{}:Y(y) or N(n)'.format(role_name))
                    if delet_assure == 'Y' or delet_assure == 'y':
                        all_roles.remove(i)
                        print('成功删除角色{name}'.format(name=role_name))
                        sign = True
                    elif delet_assure== 'N' or delet_assure== 'n':
                        ones_choice=False
                        sign = True
                        role_name=input('请重新输入你想删除的角色名：（退出请按q）')
                        if role_name == 'q':
                            flag = False
                        break
                    choice=input('是否继续删除角色：Y(y) or N(n)')
                    if choice == 'Y' or choice == 'y':
                        flag = True
                        break
                    elif choice == 'N' or choice == 'n':
                        flag=False
                        break
            if sign==False:
                ones_choice = False
                role_name=input('没有该角色，请重新输入要删除的角色名称：（退出请按q）')
                if role_name=='q':
                    flag = False
    elif options==str(3):
        print('更改模块')
        flag = True
        ones_choice = True
        while flag:
            if ones_choice==True:
                role_name=input('请输入想要更改的角色名称(输入q退出)：')
            if role_name=='q':
                flag=False
            else:
                for role in all_roles:
                    if role_name in role:
                        change_choice = input('请输入想要更改的选项：1.姓名，2.性别，3.职业\n')
                        if change_choice == str(1):
                            change_assure = input('请输入是否进行更改角色{}的名字：Y(y) or N(n)'.format(role_name))
                            if change_assure == 'Y' or change_assure == 'y':
                                new_name = input('请输入新名字：')
                                role[0] = new_name
                                print('角色{}名字信息更改成功'.format(role_name))
                                flag = True
                                break
                            elif change_assure == 'N' or change_assure == 'n':
                                break
                        elif change_choice == str(2):
                            change_assure = input('请输入是否进行更改角色{}的性别：Y(y) or N(n)'.format(role_name))
                            if change_assure == 'Y' or change_assure == 'y':
                                # new_name = input('请输入新名字：')
                                if role[1] == '男':
                                    role[1] = '女'
                                else:
                                    role[1] = '男'
                                print('角色{}性别信息更改成功'.format(role_name))
                                flag = True
                                break
                            elif change_assure == 'N' or change_assure == 'n':
                                break
                        elif change_choice == str(3):
                            change_assure = input('请输入是否进行更改角色{}的职业：Y(y) or N(n)'.format(role_name))
                            if change_assure == 'Y' or change_assure == 'y':
                                new_job = input('请输入新职业：')
                                role[2] = new_job
                                print('角色{}职业信息更改成功'.format(role_name))
                                break
                            elif change_assure == 'N' or change_assure == 'n':
                                break
                else:
                    role_name=input('不存在该角色,请重新输入角色名字(输入q退出):')
                    ones_choice = False
                    if role_name == 'q':
                        flag = False
    elif options == str(4):
        print('角色查询模块')
        flag=True
        while flag:
            role_name = input('请输入查询角色名字：')
            for role in all_roles:
                if role_name in role:
                    print('存在角色{}'.format(role_name))
                    flag=False
                    break
            else:
                print('不存在该角色{name}'.format(name=role_name))
                flag=False
    elif options==str(5):
        print('显示所有角色')
        print('{}{}{}'.format('名称'.center(10),'性别'.center(10),'职业'.center(10)))
        for role in all_roles:
            print(role[0].center(10),end='')         #这是格式化输出的一种形式
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print()
    elif options==str(6):
        print('正在退出王者荣耀管理系统')
        time.sleep(3)
        print('退出成功，欢迎再次光临')
        break
    else:
        print('输入错误，请重新选择.')
