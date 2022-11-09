##Version 1.0.3##正式开始##逻辑模块完善##

import random
import sys
import datetime
import os
import sqlite3

##全局变量##
Path = f'./Data/'
File = 'Favorability_Database.db'
Table = 'Favorability_Database'
#Purviews = ['Developer','Hard','System','Debugger','Administrator','User','Guest','Player','None']
Purviews = ['Extra','Developer','Lover','Main_Friend','Parents','Friend','Stranger']
#七级权限组#
Operations_1 = ['无','拍','敲','抓','摸','捋'.'蹭']
Operations_2 = ['胸','头','耳朵','尾巴']
#行为分类组['None','Hit','Beat','Touch chest','Touch head','Touch ears','Touch the tail','Stroke the tail']
#         ['无',  '拍',  '敲',  '摸胸',       '摸头',       '摸耳朵',    '摸尾巴',         '捋尾巴'         ]#
global user,favorability,purview,operation,repeat,argument,status
##全局变量##

def Main():##主函数集##
    #global Database
    global user,favorability,purview,argument,operation,repeat,status
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    if User_Data(cur) == True :
        User_Data_Read(cur)
    else :
        User_Data_New(cur)
        favorability,purview,operation,repeat = 0,6,0,0
    Logic(Database,cur)

def Premise():##文件状态判断模块##已完成##未测试##
    if not os.path.isfile(Path+File) :
        if not os.path.exists(Path) :
            return False
    else :
        return True

def New_Table(Pre):##数据库新建模块##已完成##未测试##
    if Pre == False :
        os.makedirs(Path)
    New_Database = sqlite3.connect(Path+File)
    cur = New_Database.cursor()
    cur.execute(f'''
        Create table 
        {Table}(
        User integer Primary Key,
        Favorability integer,
        Purview integer,
        Operation integer,
        repeat integer)''')
    cur.execute(f'insert into {Table} values(?,?,?,?,?)', (2602961063,0,0,0,0))
    New_Database.commit()
    New_Database.close()

def User_Data(cur):##用户数据存在判定模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeat
    result = cur.execute(f'select ifnull((select User from {Table} where User=\'{user}\'), 0)')
    if result == 0 :
        result = False
    else :
        result = True
    return result

def User_Data_New(cur):##用户数据新建模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeat
    cur.execute(f'insert into {Table} values(?,?,?,?,?)', (user,0,6,0,0))
    Database.commit()

def User_Data_Read(cur):##用户数据读取模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeat
    data = cur.execute(f'select * from {Table} where User={user}')
    read = data.fetchone()
    user,favorability,purview,operation,repeat = read

def Database_write(Database,cur):##数据写入模块##已完成##未测试##
    global user,favorability,purview,argument,operation,repeat
    favorability = favorability+argument
    cur.execute(f'update {Table} set Favorability={favorability} WHERE User={user}')
    cur.execute(f'update {Table} set Purview={purview} WHERE User={user}')
    cur.execute(f'update {Table} set Operation={operation} WHERE User={user}')
    cur.execute(f'update {Table} set repeat={repeat} WHERE User={user}')
    Database.commit()
    cur.close()
    Database.close()
    Output()

def Output():##输出模块##
    global user,favorability,purview,argument,operation,repeat
    if repeat > 0 :
        repeats = '\n（重复触发）'
    else :
        repeats = ''
    if argument >= 0:
        argu = f'+{argument}'
    print(f'[CQ:at,qq={user}]\n好感度{argu}{repeats}')

def Logic(Database,cur):##逻辑判断模块##
    global user,favorability,purview,argument,operation,repeat,status
    for i in range(len(Operations_1)):
        if Operations_1[i] in status :
            operations = str(i)
    if operations == '0':
        for i in range(len(Operations_2)):
            if Operations_2[i] in status :
                operations += str(i)
    if repeat > 0 :
        if operations == operation :
            repeat += 1
    operation = operations
    Argument()
    Database_write(Database,cur)

def Argument():
    global user,favorability,purview,argument,operation,repeat,status
    if operation == '33':
        argument = 3

def Command(command):##特殊指令模块##
    print("Disable")

if __name__ == '__main__':
    global user,status
    user = sys.argv[1]
    status = sys.argv[-1]
    cmd = sys.argv[-2]
    Pre = Premise()
    if cmd == "Command" :
        Command(status)
    elif Pre == False :
        New_Table(Pre)
    else :
        Main()
