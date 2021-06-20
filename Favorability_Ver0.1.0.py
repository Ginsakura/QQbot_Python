##Version 0.1.0##开始之前##程序基础完善##

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
#行为分类组#
##全局变量##

def Main(user,status):##主函数集##
    #global Database
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    if User_Data(cur,user) == True :
        Data = User_Data_Read(cur,user)
        user,favorability,purview,operation = Data[0],Data[1],Data[2]
    else :
        User_Data_New(cur,user)
        favorability,purview,operation = 0,6,0
    Logic(Database,cur,user,status,purview,favorability,operation)

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
        Operation integer)''')
    New_Database.close()

def User_Data(cur,user):##用户数据存在判定模块##已完成##未测试##
    result = cur.execute(f'select ifnull((select User from {Table} where User='{User}'), 0)')
    if result == 0 :
        result = False
    else :
        result = True
    return result

def User_Data_New(cur,user):##用户数据新建模块##已完成##未测试##
    cur.execute(f'insert into {Table} values(?,?,?)', (user,0,6,0))
    Database.commit()

def User_Data_Read(cur,user):##用户数据读取模块##已完成##未测试##
    read = cur.execute(f'select {user} from {Table}')
    return read

def Database_write(Database,cur,user,favorability,purview,argument,operation):##数据写入模块##已完成##未测试##
    cur.execute(f'update {Table} set Favorability={favorability} WHERE User={user}')
    cur.execute(f'update {Table} set Purview={purview} WHERE User={user}')
    cur.execute(f'update {Table} set Operation={operation} WHERE User={user}')
    Database.commit()
    cur.close()
    Database.close()
    Output(user,purview,argument,operation)

def Output(user,purview,argument,operation):##输出模块##
    if operation == 1 :
        repeat = '\n（重复触发）'
    else :
        repeat = ''
    print(f'[CQ:at,qq={user}]\n{result}\n好感度{argument}{repeat}')

def Logic(Database,cur,user,status,Purview,favorability,operation):##逻辑判断模块##
    
    Database_write(Database,cur,user,favorability,purview,argument)

if __name__ == '__main__':
    user = sys.argv[-1]
    status = sys.argv[-2]
    Pre = Premise()
    if Pre == False :
        New_Table(Pre)
    main(user,status)