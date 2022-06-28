# _*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/7/1 000110:51
# 文件名称:Goverment_of_parking_charge_system
# 开发工具:PyCharm
"""
停车计费系统：
进入停车场计入进入时间，出停车站计算出来时间
十五分钟一块
一小时四块
停车场能停车的总数量时固定的。
"""
import time


class Parking():
    def __init__(self, parking_space_num, parking_car, car_number=0):
        self.parking_space_num = parking_space_num
        self.parking_car = parking_car

    def enroll(self, car_name, car_id):
        enroll_time = time.time()
        if self.parking_space_num > 0:
            self.parking_car.append(
                {'car_id': car_id, 'car_name': car_name, 'enroll_time': enroll_time, 'quit_time': None, 'cost': 0})
            self.parking_space_num -= 1
        else:
            print('当前停车场没有空余位置')

    def qiut(self, car_id):
        # quit_time=time.time()
        for i in self.parking_car:
            if car_id == i['car_id']:
                i['quit_time'] = time.time()
                print(i)
                self.parking_space_num +=1
                break
        else:
            print('当前停车场没有该车')

    def cost(self, car_id):
        """
        计算停车场里面车的消费
        :param car_id:
        :return: 返回离开停车场的车要交的钱
        """
        for i in self.parking_car:
            if car_id == i['car_id']:
                total_time = int(i['quit_time'] - i['enroll_time'])/60
                if total_time%15==0:
                    i['cost']= total_time/15
                else:
                    i['cost'] = total_time / 15 +1
                print(total_time)
                print(i)


if __name__ == '__main__':
    parking_car = []
    p = Parking(parking_space_num=20, parking_car=parking_car)
    print(p.parking_space_num)
    p.enroll(car_id="豫A88888",car_name='玛莎拉蒂')
    print(p.parking_space_num)
    time.sleep(120)
    p.qiut(car_id="豫A88888")
    p.cost(car_id="豫A88888")
