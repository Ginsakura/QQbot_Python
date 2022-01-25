##Version 1.0.1##最最后一步##歌曲搜索##bug修复##

import re
import os
import sys
import sqlite3
import urllib3
import datetime

##全局变量##
Path = f'{os.getcwd()}\\Cloudmusic_Data\\'
File = 'Cloudmusic_Data.db'
Table = 'Cloudmusic_Data'
global user,songid,songname,album,singer,image_url
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
    new_time = datetime.datetime.now()
    cur.execute(f'''
        Create table 
        {Table} (
        Datetime text Primary Key,
        User integer,
        SongID text,
        Songname text,
        Album text,
        Singer text,
        Status text)''')
    cur.execute(f'insert into {Table} values(?,?,?,?,?,?,?)', (new_time,2602961063,'0','None','None','None','First Run'))
    New_Database.commit()
    New_Database.close()

def main(text,reg_id,reg_name):##正则匹配模块##已完成##测试通过##
    global songid,songname,album,singer
    text2 = re.sub(r'\s','',text)
    m = re.match(reg_id,text2)
    if m.group(2) == None :
        #print(m.group(2))
        m = re.match(reg_name,text)
        if m == None:
            print('错误输入_错参')
            status = 'Error'
            songname = 'Error'
            song_subname = 'Error'
            songid = 'Error'
            singer = 'Error'
            album = 'Error'
            User_Data_Write(status)
        elif m.group(1) == '':
            print('错误输入_空参')
            status = 'None'
            songname = 'None'
            song_subname = 'None'
            songid = 'None'
            singer = 'None'
            album = 'None'
            User_Data_Write(status)
        else :
            songname = m.group(1)
            songid = 0
            Web_Search()
    else:
        songid = m.group(3)
        songname = 'None'
        URL_resolve()

def User_Data_Write(status):##点歌数据写入模块##已完成##未测试##
    global user,songid,songname,album,singer,Path,File,Table
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    time = datetime.datetime.now()
    cur.execute(f'insert into {Table} values(?,?,?,?,?,?,?)', (time,user,songid,songname,album,singer,f'Http:{status}'))
    Database.commit()
    Database.close()

def URL_resolve():##URL解析模块##未完成##未测试##
    global songname,songid,album,singer
    http = urllib3.PoolManager()
    page = http.request('get',f'http://music.163.com/song?id={songid}')
    status = page.status
    if status == 200 :
        data = page.data
        Web_resolve(data,status)
    else :
        status = f'HTTP Error : {status}'
        User_Data_Write(status)
        print(status)

def Web_resolve(data,status):
    global songname,songid,album,singer,image_url
    data = data.decode()
    Err_404 = re.search(r'<div data-module="404"',data)
    if not Err_404 == None :# False:
        #print(Err_404)
        print('你要查找的歌曲没有找到……Q w Q')
        status = '404'
        songname = 'None'
        song_subname = 'None'
        singer = 'None'
        album = 'None'
        User_Data_Write(status)
    else:
        #print(Err_404)
        songname = re.search(r'<em class="f-ff2">(.*)</em>',data)
        song_subname = re.search(r'<div class="subtit f-fs1 f-ff2">(.*)</div>',data)
        singer = re.search(r'歌手：<span title="(.*)">.*class="s-fc7"',data)
        album = re.search(r'" class="s-fc7">(.*)</a></p>',data)
        imgurl = re.search(r'class="j-img" data-src="(.*)jpg">',data)
        if song_subname == None :
            song_subname = 'None'
            #song_subname = song_subname.group(1)
            songname = songname.group(1)
        else :
            song_subname = song_subname.group(1)
            songname = f'{songname.group(1)}({song_subname})'
        singer = singer.group(1)
        album = album.group(1)
        image_url = f'{imgurl.group(1)}jpg'
        #print(songname)
        #print(song_subname)
        #print(singer)
        #print(album)
        #print(image_url)
        #result = eval(repr(result).replace('\\\\', '\\'))
        User_Data_Write(status)
        Output()

def Web_Search():
    print('Not open')

def Output():##xml卡片输出模块##
    global songname,songid,album,singer,image_url

    ## songname == title ##
    
    '''
    [CQ:music,type=custom,
    url=https://y.music.163.com/m/song/4911872,
    audio=http://music.163.com/song/media/outer/url?id=4911872,
    title=上を向いて歩こう,content=坂本九,
    image=http://p4.music.126.net/1Akxb7z2M1YPfR-HhobCpw==/742170348760930.jpg]
    '''
    #url = re.sub(r'/','','https://y.music.163.com/m/song/')
    #audio_url = re.sub('','','http://music.163.com/song/media/outer/url?id=')
    print(f'[CQ:music,type=custom,url=https://y.music.163.com/m/song/{songid},audio=http://music.163.com/song/media/outer/url?id={songid},title={songname},content={singer},image={image_url}]')


if __name__ == '__main__':
    global user
    Pre = Premise()
    if not Pre == True :
        New_Table(Pre)
    #text = sys.argv[-1]
    #user = sys.argv[1]
    #text = '网易云点歌 ID 22823170'
    #text = '网易云 ID 114514'
    text = '网易云点歌'
    user = 0000000
    reg_id = r'网易云(点歌)?(ID|id|Id|iD)?(\d*)?'
    reg_name = r'网易云点歌\s?(.*)'
    main(text,reg_id,reg_name)