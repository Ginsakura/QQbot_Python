##Version 1.0.0##正式开始##逻辑模块完善##输出模块完善##

import random
import sys
import datetime
import os
import sqlite3

##全局变量##
Path = f'{os.getcwd()}\\Favorability_Data\\'
File = 'Favorability_Database.db'
Table = 'Favorability_Database'
#Purviews = ['Developer','Hard','System','Debugger','Administrator','User','Guest','Player','None']
Purviews = ['Extra','Developer','Lover','Main_Friend','Parents','Friend','Stranger']
#七级权限组#
Operations = ['None','Hit','Beat','Touch chest','Touch head','Touch ears','Touch the tail','Stroke the tail']
#行为分类组   ['无',  '拍',  '敲',  '摸胸',       '摸头',       '摸耳朵',    '摸尾巴',         '捋尾巴'         ]#
global user,favorability,purview,argument,operation,repeat
##全局变量##

def Main(user,status):##主函数集##
    #global Database
    global user,favorability,purview,argument,operation,repeat
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    if User_Data(cur,user) == True :
        Data = User_Data_Read(cur,user)
        user,favorability,purview,operation,repeat = Data[0],Data[1],Data[2],Data[3]
    else :
        User_Data_New(cur,user)
        favorability,purview,operation,repeat = 0,6,0,0
    Logic(Database,cur,user,status,purview,favorability,operation,repeat)

def Premise():##文件状态判断模块##已完成##未测试##
    if not os.path.isfile(Path+File) :
        if not os.path.exists(Path) :
            return False
        else :
            return None
    else :
        return True

def New_Table(Pre):##数据库新建模块##已完成##未测试##
    if Pre == False :
        os.makedirs(Path)
    New_Database = sqlite3.connect(Path+File)
    cur = New_Database.cursor()
    New_Database = cur.execute(f'''
        Create table 
        {Table}(
        User integer Primary Key,
        Favorability integer,
        Purview integer,
        Operation integer,
        repeat integer)''')
    New_Database.close()

def User_Data(cur,user):##用户数据存在判定模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeat
    result = cur.execute(f'select ifnull((select User from {Table} where User='{User}'), 0)')
    if result == 0 :
        result = False
    else :
        result = True
    return result

def User_Data_New(cur,user):##用户数据新建模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeatv
    cur.execute(f'insert into {Table} values(?,?,?,?)', (user,0,6,0,0))
    Database.commit()

def User_Data_Read(cur,user):##用户数据读取模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeatv
    read = cur.execute(f'select {user} from {Table}')
    return read

def Database_write(Database,cur,argument):##数据写入模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeatv
    cur.execute(f'update {Table} set Favorability={favorability} WHERE User={user}')
    cur.execute(f'update {Table} set Purview={purview} WHERE User={user}')
    cur.execute(f'update {Table} set Operation={operation} WHERE User={user}')
    cur.execute(f'update {Table} set repeat={repeat} WHERE User={user}')
    Database.commit()
    cur.close()
    Database.close()
    Output(user,purview,argument)

def Output(argumen):##输出模块##
    global user,favorability,purview,argument,operation,repeatv
    if repeat > 0 :
        repeats = '\n（重复触发）'
    else :
        repeats = ''
    print(f'[CQ:at,qq={user}]\n{result}\n好感度{argument}{repeats}')

def Logic(Database,cur,status,):##逻辑判断模块##
    global user,favorability,purview,argument,operation,repeatv
    if status == '' :
        pass
    if repeat > 0 :
        if operation == opera :
            repeat += 1
    else :
        pass
    Database_write(Database,cur,argument)

def Command(command):##特殊指令模块##
    pass

if __name__ == '__main__':
    user = sys.argv[1]
    status = sys.argv[-1]
    purview = sys.argv[-3]
    if purview == "Command" :
        Command(status)
    Pre = Premise()
    if Pre == False :
        New_Table(Pre)
    main(user,status)
