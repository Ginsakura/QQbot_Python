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
Purviews = ['Developer','Hard','System','Debugger','Administrator','User','Guest','Player','None']
Operation = ['']
#七级权限#
##全局变量##

def Main(user,status):##主函数集##
    #global Database
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    if User_Data(cur,user) == True :
        Data = User_Data_Read(cur,user)
        user,favorability,purview = Data[0],Data[1],Data[2]
    else :
        User_Data_New(cur,user)
        favorability,purview = 0,6
    Logic(Database,cur,user,status,purview,favorability)

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
        Purview integer)''')
    New_Database.close()

def User_Data(cur,user):##用户数据存在判定模块##已完成##未测试##
    result = cur.execute(f'select ifnull((select User from {Table} where User='{User}'), 0)')
    if result == 0 :
        result = False
    else :
        result = True
    return result

def User_Data_New(cur,user):##用户数据新建模块##已完成##未测试##
    cur.execute(f'insert into {Table} values(?,?,?)', (user,0,6))
    Database.commit()

def User_Data_Read(cur,user):##用户数据读取模块##已完成##未测试##
    read = cur.execute(f'select {user} from {Table}')
    return read

def Database_write(Database,cur,user,favorability,purview,argument):##数据写入模块##已完成##未测试##
    cur.execute(f'update {Table} set Favorability={favorability} WHERE User={user}')
    cur.execute(f'update {Table} set Purview={purview} WHERE User={user}')
    Database.commit()
    cur.close()
    Database.close()
    Output(user,purview,argument)

def Output(user,):##输出模块##
    print(f'')

def Logic(Database,cur,user,status,Purview,favorability):##逻辑判断模块##
    
    Database_write(Database,cur,user,favorability,purview,argument)

if __name__ == '__main__':
    user = sys.argv[-1]
    status = sys.argv[-2]
    Pre = Premise()
    if Pre == False :
        New_Table(Pre)
    main(user,status)