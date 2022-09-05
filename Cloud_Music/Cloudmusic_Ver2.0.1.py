##Version 2.0.1##以类方式重写##增加ID点歌##Fix BUG##修改发送所使用的CQ码##

import re
import os
import sys
import json
import sqlite3
import urllib3  
import datetime
from time import sleep
from base64 import b64encode
from Crypto.Cipher import AES
from requests_html import HTMLSession as html


class Cloudmusic():
    def __init__(self, user, text):
        self.Path = f'./Data/Cloudmusic_Data/'
        self.File = 'Cloudmusic_Data.db'
        self.Table = 'Cloudmusic_Data'
        self.time = datetime.datetime.now()
        self.user = user
        self.songID = 0
        self.songName = ''
        self.album = ''
        self.singer = ''
        self.imageURL = ''
        self.text = text[0]
        self.searchText = ''
        self.reg_id = r'网易云(点歌)?(ID|id|Id|iD)?(.*)?'
        self.reg_name = r'网易云点歌\s?(.*)'
        self.searchURL = 'http://music.163.com/api/search/pc'
        self.UA = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        self.status = ''

    def Main(self):
        self.Premise()
        #self.text = re.sub(r'\s','',self.text)
        s1 = re.match(self.reg_id, self.text)
        if s1.group(2) == None:
            self.searchText = s1.group(3)
            self.SearchText()
        else:
            self.songID = s1.group(3)
            self.SearchID()

    def Premise(self):##数据库文件、路径状态判断模块##已完成##未测试##
        if not os.path.exists(self.Path) :
            os.makedirs(self.Path)
        if not os.path.isfile(f'{self.Path}{self.File}'):
            ndb = sqlite3.connect(f'{self.Path}{self.File}')
            cur = ndb.cursor()
            now_time = datetime.datetime.now()
            cur.execute(f'''
                Create table 
                {self.Table} (
                Datetime text Primary Key,
                UserID integer,
                SongID text,
                SongName text,
                Album text,
                Singer text,
                ImageURL text,
                Status text)''')
            cur.execute(f'insert into {self.Table} values(?,?,?,?,?,?,?,?)', (self.time,00000,'0','None','None','None','None','Init Data'))
            ndb.commit()
            ndb.close()

    def SearchText(self):
        param = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": self.searchText, "type": "1", "offset": "0",
            "total": "true", "limit": "1", "csrf_token": ""}
            ##limit为搜索数目
        params=self.get_enc(json.dumps(param))
        data={
            'params': params,
            'encSecKey':'bb20ee9409e57057e4d1b55e4d77c94bff4d8cbf181c467bbd3fa156e3419665c6c1e643621d5d82c128251fb85f0cb34d4f08c88407b4148924ffa818f59a64b3814784e7e3837bad4f6f9690cb2cf721d9ea1af12c16a32a9df00be710b70ee8ed32036cc6a465b28ef43f4382cbcb4595b3121be75ecba9171876b611b8fc'
        }
        url='https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        try:
            web = html().post(url=url, data=data, headers=self.UA)
            data=json.loads(web.text)
            self.songID = data['result']['songs'][0]['id']
            self.songName = data['result']['songs'][0]['name']
            self.singer = [i['name'] for i in data['result']['songs'][0]['ar']][0]
            self.album = data['result']['songs'][0]['al']['name']
            self.imageURL = data['result']['songs'][0]['al']['picUrl']
            self.status = 200
            self.Output()
        except Exception as e:
            self.status = repr(e)
            self.User_Data_Write()

    def SearchID(self):
        http = urllib3.PoolManager()
        page = http.request('get',f'http://music.163.com/song?id={self.songID}')
        self.status = page.status
        if self.status == 200 :
            data = page.data
            self.Web_resolve(data)
        else :
            self.status = f'HTTP Error : {status}'
            self.User_Data_Write()
            print(self.status)

    def Web_resolve(self,data):
        data = data.decode()
        Err_404 = re.search(r'<div data-module="404"',data)
        if not Err_404 == None :# False:
            #print(Err_404)
            print('你要查找的歌曲没有找到……Q w Q')
            self.status = '404'
            self.songName = 'None'
            self.singer = 'None'
            self.album = 'None'
            self.User_Data_Write()
        else:
            #print(Err_404)
            self.songName = re.search(r'<em class="f-ff2">(.*)</em>',data)
            songSubname = re.search(r'<div class="subtit f-fs1 f-ff2">(.*)</div>',data)
            self.singer = re.search(r'歌手：<span title="(.*)">.*class="s-fc7"',data)
            self.album = re.search(r'" class="s-fc7">(.*)</a>.*</p>',data)
            self.imageURL = re.search(r'class="j-img" data-src="(.*)jpg">',data)
            if songSubname == None :
                songSubname = 'None'
                #songSubname = songSubname.group(1)
                self.songName = self.songName.group(1)
            else :
                songSubname = songSubname.group(1)
                self.songName = f'{self.songName.group(1)}({songSubname})'
            self.singer = self.singer.group(1)
            self.album = self.album.group(1)
            self.imageURL = f'{self.imageURL.group(1)}jpg'
            #print(songname)
            #print(songSubname)
            #print(singer)
            #print(album)
            #print(image_url)
            #result = eval(repr(result).replace('\\\\', '\\'))
            self.Output()

    def to_16(self, data):
        len1=16-len(data)%16
        data+=chr(len1)*len1
        return data
    
    def encryption(self, data,key):
        iv = '0102030405060708'
        aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
        data1 = self.to_16(data)
        bs = aes.encrypt(data1.encode('utf-8'))
        return str(b64encode(bs),'utf-8')
    
    def get_enc(self,data):
        param4 = '0CoJUm6Qyw8W8jud'
        #enc='NA5SxhePf6dxIxX7'
        #enc='GLvjERPvSFUw6EVQ'
        enc = 'g4PXsCuqYE6icH3R'
        first = self.encryption(data,param4)
        return self.encryption(first,enc)

    def Output(self):
        self.User_Data_Write()  
        #print(f'[CQ:music,type=custom,url=https://y.music.163.com/m/song/{self.songID},audio=http://music.163.com/song/media/outer/url?id={self.songID},title={self.songName},content={self.singer},image={self.imageURL}]')
        print(f'[CQ:music,type=163,id={self.songID}]')

    def User_Data_Write(self):##点歌数据写入模块##已完成##未测试##
        #print(self.time,self.user,self.songID,self.songName,self.album,self.singer,self.imageURL,f'Http:{self.status}')
        Database = sqlite3.connect(self.Path+self.File)
        cur = Database.cursor()
        time = datetime.datetime.now()
        cur.execute(f'insert into {self.Table} values(?,?,?,?,?,?,?,?)', (self.time,self.user,self.songID,self.songName,self.album,self.singer,self.imageURL,f'Http:{self.status}'))
        Database.commit()
        Database.close()

if __name__ == '__main__':
    usr = 000
    if len(sys.argv) > 1:
        op = sys.argv[1:]
        f = Cloudmusic(usr,op)
        a = f.Main()