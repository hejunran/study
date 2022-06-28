#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/13 001316:01
# 文件名称:market_shop
# 开发工具:PyCharm
commodity_names={}

def Shop(per_commdity_price,per_commdity_number):

    total = per_commdity_price*per_commdity_number

    return total

def Pay(pay_style,total_money):
    if pay_style==1:
        total_money=total_money
    elif pay_style==2:
        total_money=0.95*total_money
    elif pay_style==3:
        total_money =total_money-total_money*0.1
    elif pay_style==4:
        if total_money>=100:
            n = total_money // 100
            total_money=total_money-20*n
        else:
            total_money=total_money
    else:
        return False
    return total_money

if __name__ == '__main__':
    print('welcome to the shop of beijinggongyedaxue:')
    total_money=0
    total_number=0
    while(True):
    # name =input('please input the name of commodity:')
        answer =input('是否进行商品的购买（q表示退出）:')
        if answer=='q':
            break
        else:
            price =float(input("please input the price of commodity:"))
            number =int(input("please input the number of commodity:"))
            total_money+=Shop(price,number)
            total_number+=number

    while(True):
        print('请选择你的支付方式：1.现金支付，没有折扣；2.微信支付，0.95折；'
              '3.支付宝支付，鼓励金为付款金额的10%，可以直折算到付款金额中；4.刷卡，满100减20.')   # 自带缩进功能
        pay_style =int(input())
        payment=Pay(pay_style,total_money)
        if payment==False:
            print('没有该支付方式，请重新选择。')
            continue
        else:
            print('实际购买的商品数量是：%d，商品的总额是；%.2f，你的实际支付金额为：%.2f'%(total_number,total_money,payment))
            break


