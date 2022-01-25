##Version 2.0.0##代码重构##

import random
import sys
import datetime
import configparser

def Extra(main,judg,Ex):##二阶判定模块已完成##测试通过##
    second = ['Ex','+','','-']
    if Ex <= main :
        re = 3
    elif Ex >= 100-main :
        re = 1
    else :
        re = 2
    if judg == True :
        re = 0-re
    return second[re]
    print(second[re])

def Special(main,Extra):##额外判定逻辑已完成##测试通过##
    review = ['\n这……请吃好喝好……注意天上，注意地面……（默哀脸）','\n喵↑？你真的没有作弊吗？（怀疑的目光）','\n换言之……也是一种幸运呢……','\n好幸运喵（★ω★）']
    x = 1
    y = 3
    if main == 1 :
        result = '大凶'
        x = 0
        y = 2
    else :
        result = '大吉' 
    if Extra == main :
        return result+'Ex'+review[x]
    else :
        return result+'+'+review[y]

def main(user,time):#一阶(主)判定模块已完成##初步测试通过##等待完整测试##
    seed = f'{user} {time}'
    random.seed(seed)
    num = random.randint(1,100)
    Ex = random.randint(1,100)
    first = ['大凶','凶','末吉','吉','中吉','大吉']
    remark = ['换言之……也是一种幸运……喵……？（不确定的语气）','今天请小心一点喵……','一切如常喵~','运气还不错喵~','今天也是幸运的一天喵~','好幸运喵（★ω★）']
    if num <= 5 :#1-5
        if num == 1 :
            result = Special(num,Ex)
        else :
            result = first[0]+Extra(5,True,Ex)+'\n'+remark[0]
    elif num <= 20 :#6-20
        result = first[1]+Extra(15,True,Ex)+'\n'+remark[1]
    elif num <= 50 :#21-50
        result = first[2]+Extra(30,False,Ex)+'\n'+remark[2]
    elif num <= 80 :#51-80
        result = first[3]+Extra(30,False,Ex)+'\n'+remark[3]
    elif num <= 95 :#81-95
        result = first[4]+Extra(15,False,Ex)+'\n'+remark[4]
    else :#96-100
        if num == 100 :
            result = Special(num,Ex)
        else :
            result = first[5]+Extra(5,False,Ex)+'\n'+remark[5]
    print(f'{result}\nseed={seed}\nmain={num}\nExtra={Ex}')
    #print(result+"\nseed="+seed)
    #print('num='+str(num)+'\nEx='+str(Ex))


#测试区域
'''
time = str(datetime.datetime.now())
user = "00000000 "
main(user,time)
'''
#测试区域

if __name__ == '__main__':
    user = sys.argv[-1]
    time = str(datetime.datetime.now())
    main(user,time)