import time
import time_api


def get_next_like_inter_time_hour(hour):
    #24小时格式
    #返回与下一个相同小时的小时间隔，返回的是秒数
    localtime = time.localtime(time.time())
    now_time_hour = localtime.tm_hour
    if now_time_hour <=hour:
        return (hour-now_time_hour)*60*60
    else:
        return (24-now_time_hour+hour)*60*60

def get_next_like_inter_time_min(min):
    #60分钟
    #返回与下一个相同分钟的分钟间隔，返回的是秒数
    localtime = time.localtime(time.time())
    now_time_min = localtime.tm_min
    if now_time_min <=min:
        return (min-now_time_min)*60
    else:
        return (60-now_time_min+min)*60

def main(f,set_time_hour,set_time_min):
    while True:
        localtime = time.localtime(time.time())
        if localtime.tm_hour == set_time_hour:#达到设定的时小时了
            print("到达小时："+str(localtime.tm_hour))
            if (localtime.tm_min-set_time_min <= 5 and localtime.tm_min-set_time_min >= 0) or (localtime.tm_min-set_time_min >= -5 and localtime.tm_min-set_time_min <=0 ) :#达到设定的分钟间隔了
                print("到达指定分钟："+str(localtime.tm_min))
                f()
                print("函数执行成功，该小时内不再执行")
                time.sleep(60*60) #延迟执行一小时防止在该一小时内一直执行
                print("从该时刻延迟 " + str((get_next_like_inter_time_hour(set_time_hour) - 60 * 60 + (
                            60 - localtime.tm_min) * 60) / 60 / 60) + " 小时后执行")
                time.sleep(get_next_like_inter_time_hour(set_time_hour) - 60 * 60 + (60 - localtime.tm_min) * 60)
            else:
                print("目前的分钟为 "+str(localtime.tm_min))
                print("延迟 "+str(get_next_like_inter_time_min(set_time_min)/60)+" 分钟")
                time.sleep(get_next_like_inter_time_min(set_time_min))#每一个小时开始的时候肯定会执行，
        else:

            print("从该时刻延迟 "+str((get_next_like_inter_time_hour(set_time_hour)-60*60+ (60-localtime.tm_min)*60)/60/60)+" 小时后执行")
            time.sleep(get_next_like_inter_time_hour(set_time_hour)-60*60+ (60-localtime.tm_min)*60 ) #本小时内是不可能执行到这里的（排除0小时减一个小时的意外），不是本小时内的该小时到下一个小时应该减去一个小时的时间，计算该小时到这一个小时最后一刻结束的时间，再加上剩余的小时时间，这样就可以从某时刻到达某个小时开始的时候

#为什么不用死循环，死循环不让主函数挂起的话，程序在系统给他的时间片内它是执行不完的，一直处于完全利用cpu的状态，所以cpu的利用率很高，比如cpu给一个程序分配了1秒的时间片，这一秒内，cpu被它占用的比例就是该分钟内的时间利用率，
#所以这段时间内，程序要么能执行完，或者程序能执行一段时间挂起，就算每一秒挂起一次，程序的cpu利用也会很低