#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/1 000114:44
# 文件名称:引用
# 开发工具:PyCharm
import sys

list1=[1,2,3,4]
list2=list1
list3=list1
print(sys.getrefcount(list1))     # sys.getrefcount()计算的是引用当前对象的指针个数，包括该函数创建的一个临时指针
