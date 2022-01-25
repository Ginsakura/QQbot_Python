##Version 0.2.0##倒数第二步##xml卡片输出##

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
    Website_resolve()

def Website_resolve():##URL解析模块##未完成##未测试##
    pass

def Output(singer,image_url):##xml卡片输出模块##
    global songname,songid

    ## songname == title ##
    
    '''
    [CQ:music,type=custom,
    url=https:\\y.music.163.com\m\song\4911872,
    audio=http:\\music.163.com\song\media\outer\url?id=4911872,
    title=上を向いて歩こう,content=坂本九,
    image=http:\\p4.music.126.net\1Akxb7z2M1YPfR-HhobCpw==\742170348760930.jpg]
    '''
    url = re.sub(r'/','','https://y.music.163.com/m/song/')
    audio_url = re.sub('','','http://music.163.com/song/media/outer/url?id=')
    print(f'[CQ:music,type=custom,url=https:\/\/y.music.163.com\/m\/song\/{songid},audio=http:\/\/music.163.com\/song\/media\/outer\/url?id={songid},title={songname},content={singer},image={image_url}')


if __name__ == '__main__':
    Pre = Premise()
    if Pre == False :
        New_Table(Pre)
    text = sys.argv[1]
    #text = '网易云点歌 I 45466'
    reg = r'网易云(点歌)?(ID|id)?(\d*)?'
    reg2 = r'网易云(点歌)?\s?(.*)'
    main(text,reg,reg2)