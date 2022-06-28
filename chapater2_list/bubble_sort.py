#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/18 001821:49
# 文件名称:bubble_sort
# 开发工具:PyCharm
nums=[5,1,7,6,8,2,4,3]

# 基于交换的排序
for i in range(0,len(nums)):
    print(i)
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            continue
        else:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)

# 冒泡排序
# 每一轮都把最大的数值放在最后面
nums=[5,1,7,6,8,2,4,3]
for i in range(0,len(nums)-1):         # 外层控制轮数
    flag = False                       # 添加标志位，如果某一轮数组中元素没有发生位置交换，说明已经排好序，则直接跳出循环
    for j in range(0,len(nums)-1-i):   # len(nums)-1 是为了防止数据越界，-i是每一轮都把最大的数放在最后一位，故下一轮都比上一轮少比较一位
        if nums[j]>nums[j+1]:          # 如果要是降序排列，此处改为小于号，每次把最小元素放在最后面。
            flag=True
            nums[j],nums[j+1]=nums[j+1],nums[j]
    if flag == False:
        break
print(nums)

# 冒泡排序
# 每一轮都把最小的数值放在最前面
print('*-'*30)
nums=[5,1,7,6,8,2,4,3]
for i in range(0,len(nums)-1):         # 外层控制轮数
    for j in range(0,len(nums)-1):
        # print(j)
        if nums[len(nums)-1-j]<nums[len(nums)-1-j-1]:
            nums[len(nums)-1-j], nums[len(nums)-1-j- 1] = nums[len(nums)-1-j - 1], nums[len(nums)-1-j]
    print(nums)
