import time
import time_api
import time_control




def ex1():#把需要每天定时执行的函数放在这里就行了
    ###############任务函数，这里可以放任意多个需要执行的函数
    time_api.f1();







#本代码只设置，一天内某个时刻——小时，分钟的出发执行
set_time_hour=12 #开始执行的小时时刻设置
set_time_min=12 #开始执行的分钟时刻设置



if __name__ == "__main__":
    set_time_hour = int(input("请输入一个整数小时0-23:"))
    set_time_min = int(input("请输入一个分钟小时0-59:"))
    time_control.main(ex1,set_time_hour,set_time_min)



