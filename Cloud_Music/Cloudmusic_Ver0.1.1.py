##Version 0.1.1##开始之前##存储点歌数据##

import re
import os
import sys
import datetime

##全局变量##
Path = './Cloudmusic_Data/'
File = 'Cloudmusic_Data.db'
Table = 'Cloudmusic_Data'
datetime = datetime.datetime.now()
global user,songid,songname
##全局变量##

def Premise():##数据库文件、路径状态判断模块##已完成##未测试##
    if not os.path.isfile(Path+File) :
        if not os.path.exists(Path) :
            return False
    else :
        return True

def New_Table(Pre):##点歌数据库新建模块##已完成##未测试##
    global Path,File,Table
    if Pre == False :
        os.makedirs(Path)
    New_Database = sqlite3.connect(Path+File)
    cur = New_Database.cursor()
    cur.execute(f'''
        Create table 
        {Table}(
        User integer Primary Key,
        Datetime text,
        SongID integer,
        Songname text)''')
    cur.execute(f'insert into {Table} values(?,?,?,?)', (2602961063,datetime.datetime.now(),0,'FirstRun'))
    New_Database.commit()
    New_Database.close()

def main(text,reg1,reg2):##正则匹配模块##已完成##测试通过##
    global songname,songid
    text2 = re.sub(r'\s','',text)
    m = re.match(reg1,text2)
    if m.group(2) == None :
        m = re.match(reg2,text)
        songname = m.group(2)
        songid = 0
    else:
        songid = m.group(3)
        songname = 'None'
    User_Data_Write()

def User_Data_Write():##点歌数据写入模块##已完成##未测试##
    global user,songid,songname,datetime,Path,File,Table
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    cur.execute(f'insert into {Table} values(?,?,?,?)', (user,datetime,songid,songname))
    Database.commit()
    Database.close()
    Output()

def Output():
    global user,songid,songname
    #
    print(f'')


if __name__ == '__main__':
    Pre = Premise()
    if Pre == False :
        New_Table(Pre)
    text = sys.argv[1]
    #text = '网易云点歌 I 45466'
    reg = r'网易云(点歌)?(ID|id)?(\d*)?'
    reg2 = r'网易云(点歌)?\s?(.*)'
    main(text,reg,reg2)