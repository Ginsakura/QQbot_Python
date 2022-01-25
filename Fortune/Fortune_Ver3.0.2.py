##Version 3.0.2##轻微修改日期模块##bug修复##
import os
import sys
import random
import sqlite3
import datetime

##全局变量##
Path = f'{os.getcwd()}\\Fortune_Data\\'
File = 'Fortune_Data.db'
Table = 'Fortune_Data'
DB = sqlite3.connect(Path+File)
cur = DB.cursor()
global user,time,date,main,extra
##全局变量##

def Premise():##数据库路径状态判断模块##已完成##
    if not os.path.exists(Path) :
        os.makedirs(Path)

def New_Table():##运势数据库新建模块##已完成##
    global Path,File,Table,date,user,time,main,extra
    #Database = sqlite3.connect(Path+File)
    #cur = Database.cursor()
    cur.execute(f'''
        Create table 
        {date} (
        User integer Primary Key,
        Time text,
        Main integer,
        Extra integer)''')
    #cur.execute(f'insert into {date} values(?,?,?,?)', (user,time,main,extra))
    #DB.commit()
    #DB.close()

def Main_Function(statu):
    global main,extra
    if statu == True :
        main = random.randint(1,100)
        extra = random.randint(1,100)
    first = ['大凶','凶','末吉','吉','中吉','大吉']
    remark = ['换言之……也是一种幸运……喵……？（不确定的语气）','今天请小心一点喵……','一切如常喵~','运气还不错喵~','今天也是幸运的一天喵~','好幸运喵（★ω★）']
    if main <= 5 :#1-5
        if main == 1 :
            result = Special(main,extra)
        else :
            result = first[0]+Extra(5,True,extra)+'\n'+remark[0]
    elif main <= 20 :#6-20
        result = first[1]+Extra(15,True,extra)+'\n'+remark[1]
    elif main <= 50 :#21-50
        result = first[2]+Extra(30,False,extra)+'\n'+remark[2]
    elif main <= 80 :#51-80
        result = first[3]+Extra(30,False,extra)+'\n'+remark[3]
    elif main <= 95 :#81-95
        result = first[4]+Extra(15,False,extra)+'\n'+remark[4]
    else :#96-100
        if main == 100 :
            result = Special(main,extra)
        else :
            result = first[5]+Extra(5,False,extra)+'\n'+remark[5]
    if statu == True :
        User_Data_Write(result,main,extra)
    else:
        return result

def Extra(main_Extra,judg,Extra_Extra):##二阶判定模块##已完成##
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

def Special(main_Special,Extra_Special):##额外判定逻辑模块##已完成##
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
        return result+' Ex'+review[x]
    else :
        return result+' +'+review[y]

def Table_Exist():##检查当天的表是否存在##
    global date
    exist = cur.execute(f'select * from sqlite_master where type=\'table\' and name = {date}')
    exist = exist.fetchone()
    if exist == None :
        New_Table()
        Main_Function(statu=True)
    else:
        User_Data_Read()

def User_Data_Read():
    global user,main,extra
    data = cur.execute(f'select * from {date} where User={user}')
    Read_Data = data.fetchone()
    if Read_Data == None :
        Main_Function(statu=True)
    else :
        user,time,main,extra = Read_Data
        result = Main_Function(statu=False)
        print(f'[CQ:at,qq={user}]\n{result}\n\n你今天{time}已经抽过了的说……（轻轻戳手指……）')

def User_Data_Write(result,main,extra):
    cur.execute(f'insert into {date} values(?,?,?,?)', (user,time,main,extra))
    DB.commit()
    DB.close()
    print(f'[CQ:at,qq={user}]\n{result}')
    pass

if __name__ == '__main__':
    global user,time,date
    time = datetime.datetime.now()
    time = time.strftime('%H:%M:%S')
    date = datetime.date.today()
    if len(str(date.month)) == 1:
        month = f'0{date.month}'
    else :
        month = date.month
    if len(str(date.day)) == 1:
        day = f'0{date.day}'
    else :
        day = date.day
    date = f'\'{date.year}.{month}.{day}\''
    #date = '\'2021.08.73\''
    user = sys.argv[-1]
    #user = 1043251354546230
    Premise()
    Table_Exist()
    