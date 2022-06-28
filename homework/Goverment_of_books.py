#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/21 002119:45
# 文件名称:Goverment_of_books
# 开发工具:PyCharm
"""
图书管理系统
至少五本书
liabrary=[{'bookname':'xxx','author':'xxx','price':'xxx','number':'xxx'}]
功能：
1.借书
2.还书
3.查询 （根据书名和作者查）
4.查询所有
5.退出
"""

liabrary=[{'bookname':'水浒传','author':'施耐庵','price':'30','number':3},
          {'bookname':'西游记','author':'吴承恩','price':'25','number':5},
          {'bookname':'三国演义','author':'罗贯中','price':'35','number':10}]
import time
flag=True
the_first_choice=True
while flag:
    if the_first_choice:
        choice=input('欢迎来到图书馆管理系统，请选择你需要的服务：1.借书，2.还书，3.查询，4.查询所有，5.退出\n')
    if choice==str(1):
        print('借书服务管理')
        sign=True
        the_first_input=True
        while sign:
            if the_first_input:
                brow_book_name=input('请输入你想要借的书本名字：')
            for i in liabrary:
                if brow_book_name in i['bookname']:
                    if i['number']>0:
                        i['number']=i['number']-1
                        print('借书成功')
                        sign=False
                        break
                    else:
                        print('图书馆中该书全部被借出')
            else:
                brow_book_name=input('图书馆中不存在该书籍，请重新输入想借的书籍名称（按q退出）：')
                if brow_book_name =='q':
                    sign=False
                    break
                else:
                    the_first_input=False

    elif choice==str(2):
        print('还书服务管理')
        sign=True
        the_first_input=True
        while sign:
            if the_first_input:
                return_bookname=input('请输入还书名字：')
                for i in liabrary:
                    if i['bookname']==return_bookname:
                        i['number']+=1
                        print('还书成功')
                        sign=False
                        break
                else:
                    return_bookname=input('该书不是图书馆书籍，请重新输入要还书籍名称：')
                    the_first_input =False

    elif choice ==str(3):
        print('图书查询管理')
        sign=True
        the_first_input=True
        while sign:
            if the_first_input:
                choice=input('请选择你的查询方式：1.按书名，2.按作者\n')
            if choice ==str(1):
                book_name=input('请输入查询书名：')
                for i in liabrary:
                    if i['bookname']==book_name:
                        print('{}{}{}{}'.format('书名'.center(15),'作者'.center(15),'价格'.center(15),'数量'.center(15)))
                        print(i['bookname'].center(15), end='')
                        print(i['author'].center(15), end='')
                        print(i['price'].center(15), end='')
                        print(str(i['number']).center(15), end='')
                        print()
                else:
                    print('图书馆不存在书名为{}书籍'.format(book_name))
                    break
            elif choice==str(2):
                author=input('请输入作者名：')
                the_first_display=True
                for i in liabrary:
                    if i['author']==author:
                        if the_first_display:
                            the_first_display = False
                            print('{}{}{}{}'.format('书名'.center(15), '作者'.center(15), '价格'.center(15), '数量'.center(15)))
                        print(i['bookname'].center(15), end='')
                        print(i['author'].center(15), end='')
                        print(i['price'].center(15), end='')
                        print(str(i['number']).center(15), end='')
                        print()
                else:
                    if the_first_display==False:
                        break
                    else:
                        print('不存在该作者{}的书籍'.format(author))
                        break
            else:
                choice =input('输入错误，请重新选择查询方式：1.按书名，2.按作者\n')

    elif choice==str(4):
        print('图书馆所有书籍：')
        print('{}{}{}{}'.format('书名'.center(15),'作者'.center(15),'价格'.center(15),'数量'.center(15)))
        for i in range(len(liabrary)):
            print(liabrary[i]['bookname'].center(15),end='')
            print(liabrary[i]['author'].center(15),end='')
            print(liabrary[i]['price'].center(15),end='')
            print(str(liabrary[i]['number']).center(15),end='')
            print()
    elif choice==str(5):
        print('正在退出图书管理系统，请稍等……')
        time.sleep(5)
        print('退出成功。')
        flag=False
    else:
        choice=input('输入错误，请重新选择：1.借书，2.还书，3.查询，4.查询所有，5.退出\n')
        the_first_choice=False