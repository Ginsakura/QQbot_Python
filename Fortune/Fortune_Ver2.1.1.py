##Version 2.1.1##隐私保护及黑箱模式##

import random
import sys
import datetime
import configparser
import os

def Premise(user,time):##判断文件状态、用户数据读取模块##已完成##测试通过##
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    Today = f'{Year}-{Month}-{Day}.Log'
    if os.path.isfile(Today) == False :
        File = open(Today,'w')
        File.close()
    ini = configparser.ConfigParser()
    ini.read(Today, encoding="utf-8")
    if ini.has_section(user) == True :
        main_Premise = int(ini.get(user,'main'))
        Extra_Premise = int(ini.get(user,'Extra'))
        main(user,time,main_Premise,Extra_Premise,repeat=True,ini_file=Today)
    else :
        main(user,time,None,None,repeat=False,ini_file=Today)

def ini_write(user,time,main_ini,Extra_ini,ini_file):##数据文件写入模块##已完成##测试通过##
    ini = configparser.ConfigParser()
    ini.read(ini_file, encoding="utf-8")
    ini.add_section(user)
    ini.set(user,'user',user)
    ini.set(user,'main',f'{main_ini}')
    ini.set(user,'Extra',f'{Extra_ini}')
    ini.write(open(ini_file, 'w'))

def Extra(main_Extra,judg,Extra_Extra):##二阶判定模块##已完成##测试通过##
    second = ['Ex','+','','-']
    if Extra_Extra <= main_Extra :
        re = 3
    elif Extra_Extra >= 100-main_Extra :
        re = 1
    else :
        re = 2
    if judg == True :
        re = 0-re
    return second[re]

def Special(main_Special,Extra_Special):##额外判定逻辑模块##已完成##测试通过##
    review = ['\n这……请吃好喝好……注意天上，注意地面……（默哀脸）','\n喵↑？你真的没有作弊吗？（怀疑的目光）','\n换言之……也是一种幸运呢……','\n好幸运喵（★ω★）']
    x = 1
    y = 3
    if main_Special == 1 :
        result = '大凶'
        x = 0
        y = 2
    else :
        result = '大吉' 
    if Extra_Special == main_Special :
        return result+'Ex'+review[x]
    else :
        return result+'+'+review[y]

def User_Hidden(user):##用户账户保护模块##
    Number = len(user)
    Hidden = user[:2] + '*'*(Number-5) + user[-3:]
    return Hidden

def main(user,time,main_main,Extra_main,repeat,ini_file):##一阶(主)判定模块##已完成##初步测试通过##等待完整测试##
    seed = f'{user} {time}'
    random.seed(seed)
    Hidden_User = User_Hidden(user)
    if main_main == None :
        main_main = random.randint(1,100)
    if Extra_main == None :
        Extra_main = random.randint(1,100)
    first = ['大凶','凶','末吉','吉','中吉','大吉']
    remark = ['换言之……也是一种幸运……喵……？（不确定的语气）','今天请小心一点喵……','一切如常喵~','运气还不错喵~','今天也是幸运的一天喵~','好幸运喵（★ω★）']
    if main_main <= 5 :#1-5
        if main_main == 1 :
            result = Special(main_main,Extra_main)
        else :
            result = first[0]+Extra(5,True,Extra_main)+'\n'+remark[0]
    elif main_main <= 20 :#6-20
        result = first[1]+Extra(15,True,Extra_main)+'\n'+remark[1]
    elif main_main <= 50 :#21-50
        result = first[2]+Extra(30,False,Extra_main)+'\n'+remark[2]
    elif main_main <= 80 :#51-80
        result = first[3]+Extra(30,False,Extra_main)+'\n'+remark[3]
    elif main_main <= 95 :#81-95
        result = first[4]+Extra(15,False,Extra_main)+'\n'+remark[4]
    else :#96-100
        if main_main == 100 :
            result = Special(main_main,Extra_main)
        else :
            result = first[5]+Extra(5,False,Extra_main)+'\n'+remark[5]
    if repeat == True :
        print(f'[CQ:at,qq={user}]\nuser={Hidden_User}\n{result}\n你今天已经抽过了的说……（轻轻戳手指……）')
    else :
        print(f'[CQ:at,qq={user}]\nuser={Hidden_User}\n{result}\n')
        ini_write(user,time,main_main,Extra_main,ini_file)


#测试区域
'''
time = str(datetime.datetime.now())
user = "00000000"
Premise(user,time)
#测试区域
'''
if __name__ == '__main__':
    user = sys.argv[-1]
    time = str(datetime.datetime.now())
    Premise(user,time)
#'''