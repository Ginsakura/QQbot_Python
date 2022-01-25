##Version 1.1。0##bug修复##

import random
import sys
import datetime

def main(user,time):
    random.seed(user+time)
    num = random.randint(1,100)
    Ex = random.randint(1,100)
    #num,Ex = 100,1
    if num <= 5 :
        if Ex == 1 :
            if num ==1 :
                print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大凶Ex\n这……请吃好喝好……注意天上，注意地面……（默哀脸）")
            else :
                print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大凶+\n换言之……也是一种幸运呢……")
        elif Ex >= 95 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大凶-\n换言之……也是一种幸运呢……")
        elif Ex <= 6 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大凶+\n换言之……也是一种幸运呢……")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大凶\n换言之……也是一种幸运呢……")
    elif num <= 20 :
        if Ex > 85 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：凶-\n今天请小心一点喵")
        elif Ex <= 15 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：凶+\n今天请小心一点喵")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：凶\n今天请小心一点喵")
    elif num <= 50 :
        if Ex <= 30 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：末吉-\n一切如常喵")
        elif Ex > 70 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：末吉+\n一切如常喵")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：末吉\n一切如常喵")
    elif num <= 80 :
        if Ex <= 30 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：吉-\n不错的运气喵！")
        elif Ex > 70 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：吉+\n不错的运气喵！")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：吉\n不错的运气喵！")
    elif num <= 95 :
        if Ex <= 15 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：中吉-\n今天也是幸运的一天喵~")
        elif Ex > 85 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：中吉+\n今天也是幸运的一天喵~")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：中吉\n今天也是幸运的一天喵~")


    else :
        if num == 100 :
            if Ex == 100 :
                print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大吉Ex\n喵↑？你真的没有作弊吗？（怀疑的目光）")
            else :
                print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大吉+\n好幸运喵（星星眼）")
        elif Ex >= 95 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大吉+\n好幸运喵（星星眼）")
        elif Ex <= 5 :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大吉-\n好幸运喵（星星眼）")
        else :
            print(f"time = {time}\nuser = {user}\n你抽到的数字是：{num}＆{Ex}\n你的结果是：大吉\n好幸运喵（星星眼）")

if __name__ == '__main__':
    user = sys.argv[-1]
    time = str(datetime.datetime.now())
    main(user,time)
