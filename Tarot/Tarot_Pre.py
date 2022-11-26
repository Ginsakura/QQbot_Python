# -*- coding: utf-8 -*-
##Version 1.0.2 Pre##等待释义##预构制图##以类方式重写##更换生成随机数边界的方法##

import os
import sys
import time as pause
import random
import sqlite3
import datetime
import pillow
#import Paraphrase

'''[
Big_Akana[#解释命运的大致运势。],
Small_Akana_Leangle[#【权杖】（The Leangle）代表元素火，象征激情、能量和创造。],
Small_Akana_Garren[#【星币】（The Garren）代表元素土，象征金钱、物质和享受。],
Small_Akana_Chalice[#【圣杯】（The Chalice）代表元素水，象征情感、关系、爱和灵感。],
Small_Akana_Blade[#【宝剑】（The Blade）代表元素风，象征思想、智慧、交流和冲突。]
]'''
#小阿卡那牌是用来补足大阿卡那牌不足之处。
#若是我们想要更进一步知道命运的真相或是对方的事情。
#其中由侍从、骑士、皇后、国王组成的人物牌，也称为宫廷牌（Court cards）。

class Tarot():
    def __init__(self,user,group):
        self.path = './Data/'
        self.file = 'Tarot_Data.db'
        self.table = 'Tarot_Data'
        self.DB = None
        self.cur = None

        self.user = user
        self.group = group

        self.now = datetime.datetime.now()
        self.time = self.now.strftime('%H:%M:%S')
        self.date = self.now.strftime('%Y.%m.%d')

        self.akana = [['0 愚人（The Fool）','Ⅰ 魔术师（The Magician）','Ⅱ 女教皇（The High Priestess）','Ⅲ 女皇（The Empress）','Ⅳ 皇帝（The Emperor）','Ⅴ 教皇（The Hierophant）','Ⅵ 恋人（The lovers）','Ⅶ 战车（The Chariot）','Ⅷ 力量（Strength）','Ⅸ 隐士（The Hermit）','Ⅹ 命运之轮（The Wheel of Fortune）','ⅩⅠ 正义（Justice）','ⅩⅡ 悬吊者（The Hanged Man）','ⅩⅢ 死神（Death）','ⅩⅣ 节制（Temperance）','ⅩⅤ 魔鬼（The Devil）','ⅩⅥ 高塔（The Tower）','ⅩⅦ 星星（The Star）','ⅩⅧ 月亮（The Moon）','ⅩⅨ 太阳（The Sun）','ⅩⅩ审判（Judgment）','ⅩⅩⅠ 世界（The World）'],['权杖王牌','权杖二','权杖三','权杖四','权杖五','权杖六','权杖七','权杖八','权杖九','权杖十','权杖侍卫','权杖骑士','权杖皇后','权杖国王',],['星币王牌','星币二','星币三','星币四','星币五','星币六','星币七','星币八','星币九','星币十','星币侍卫','星币骑士','星币皇后','星币国王',],['圣杯王牌','圣杯二','圣杯三','圣杯四','圣杯五','圣杯六','圣杯七','圣杯八','圣杯九','圣杯十','圣杯侍卫','圣杯骑士','圣杯皇后','圣杯国王'],['宝剑王牌','宝剑二','宝剑三','宝剑四','宝剑五','宝剑六','宝剑七','宝剑八','宝剑九','宝剑十','宝剑侍卫','宝剑骑士','宝剑皇后','宝剑国王']]
        self.lenAkana = 5
        self.lenAkanaNum = [22,14,14,14,14]
        self.bit = ['逆位','正位']
        
        self.first = list()
        self.second = list()
        self.third = list()

        self.version = 'Version_1.0.1'

    def main(self):
        self.Premise()

    def Premise(self):
        if not os.path.exists(self.path) :
            os.makedirs(self.path)
        if not os.path.isfile(f'{self.path}{self.file}') :
            self.DB = sqlite3.connect(f'{self.path}{self.file}')
            self.cur = self.DB.cursor()
            self.cur.execute(f'''
            Create table 
            Tarot (
            User integer not null,
            Group integer not null,
            Date text not null,
            Time text not null,
            First_Card integer
            First_Card_Bit integer,
            Second_Card integer,
            Second_Card_Bit integer,
            Third_Card integer,
            Third_Card_Bit integer,
            Primary Key(User, Date)
            );''')
            self.cur.execute(f'insert into {Table} values(?,?,?,?,?,?,?,?,?,?)', (2602961063,-1,self.date,self.time,0,0,0,0,0,0))
            self.DB.commit()
        self.DB = sqlite3.connect(f'{self.path}{self.file}')
        self.cur = self.DB.cursor()

    def Random(self):
        x = random.randint(0,int((self.lenAkana-1)*random.uniform(0.1,1)*random.randint(1,10)))%self.lenAkana
        y = random.randint(0,int((self.lenAkanaNum[x]-1)*random.uniform(0.1,1)*random.randint(1,10)))%self.lenAkanaNum[x]
        z = random.randint(1,100)%2
        print(x,y,z)
        return x,y,z


def main():
    global user
    times = 1
    first,second,third = None,None,None
    x,y,z = Random()
    first = f'{Akana[x][y]} {Bit[z]}'
    ft = Akana[x][y]
    fx,fy,fz = x,y,z
    x,y,z = Random()
    second = f'{Akana[x][y]} {Bit[z]}'
    st = Akana[x][y]
    sx,sy,sz = x,y,z
    x,y,z = Random()
    third = f'{Akana[x][y]} {Bit[z]}'
    tt = Akana[x][y]
    tx,ty,tz = x,y,z
    while st == ft :
        x,y,z = Random()
        second = f'{Akana[x][y]} {Bit[z]}'
        sx,sy,sz = x,y,z
    while tt == ft :
        x,y,z = Random()
        third = f'{Akana[x][y]} {Bit[z]}'
        tx,ty,tz = x,y,z
    while tt == st :
        x,y,z = Random()
        third = f'{Akana[x][y]} {Bit[z]}'
        tx,ty,tz = x,y,z
    Output(first,fx,fy,fz,second,sx,sy,sz,third,tx,ty,tz)
    #print(f'{first},{fx},{fy},{fz}\n{second},{sx},{sy},{sz}\n{third},{tx},{ty},{tz}')



def Output(first,fx,fy,fz,second,sx,sy,sz,third,tx,ty,tz):
    User_Data_Write(first,second,third)
    print(f'[CQ:at,qq={user}]\n{first}\n{second}\n{third}\n{Version}')
    #Paraphrase

def User_Data_Write(first,second,third):##占卜数据写入模块##
    global user,Path,File,Table
    Database = sqlite3.connect(Path+File)
    cur = Database.cursor()
    time = datetime.datetime.now()
    cur.execute(f'insert into {Table} values(?,?,?,?,?)', (time,user,first,second,third))
    Database.commit()
    Database.close()

if __name__ == '__main__':
    global user
    user = sys.argv[-1]
    date = datetime.date.today()
    seed = f'{user}{date.year}{date.month}{date.day}'
    random.seed(seed)
    Pre = Premise()
    if not Pre == True :
        New_Table(Pre)
    main()