# -*- coding: utf-8 -*-
##Version 2.0.0 Pre##等待释义##预构制图##以类方式重写##更换生成随机数边界的方法##

import os
import sys
import time as pause
import random
import sqlite3
import datetime
import PIL
#import Paraphrase

'''
Big_Akana[解释命运的大致运势。],
Small_Akana_Leangle[【权杖】（The Leangle）代表元素火，象征激情、能量和创造。]
Small_Akana_Garren[【星币】（The Garren）代表元素土，象征金钱、物质和享受。]
Small_Akana_Chalice[【圣杯】（The Chalice）代表元素水，象征情感、关系、爱和灵感。]
Small_Akana_Blade[【宝剑】（The Blade）代表元素风，象征思想、智慧、交流和冲突。]
'''
#小阿卡那牌是用来补足大阿卡那牌不足之处。
#若是我们想要更进一步知道命运的真相或是对方的事情。
#其中由侍从、骑士、皇后、国王组成的人物牌，也称为宫廷牌（Court cards）。

class Tarot():
    def __init__(self,user,group):
        self.path = './Data/'
        self.file = 'Tarot_Data.db'
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

        self.card1 = None
        self.card2 = None
        self.card3 = None

        self.version = 'Version_2.0.0 Pre'

    def main(self):
        self.Premise()
        if self.UserDataRead() == 0:
            self.Logic()
            self.UserDataWrite()
            self.Output()

    def Premise(self):
        if not os.path.exists(self.path) :
            os.makedirs(self.path)
        if not os.path.isfile(f'{self.path}{self.file}') :
            self.DB = sqlite3.connect(f'{self.path}{self.file}')
            self.cur = self.DB.cursor()
            self.cur.execute(f'''
                Create table Tarot (
                    User integer not null,
                    GroupID integer,
                    Date text not null,
                    Time text not null,
                    First_Card text,
                    Second_Card text,
                    Third_Card text,
                    Primary Key(User, Date)
                );''')
            self.cur.execute(f'insert into Tarot values(?,?,?,?,?,?,?)', (2602961063,-1,self.date,self.time,'0','0','0'))
            self.DB.commit()
        else:
            self.DB = sqlite3.connect(f'{self.path}{self.file}')
            self.cur = self.DB.cursor()

    def Random(self):
        x = random.randint(0,int((self.lenAkana-1)*random.uniform(0.1,1)*random.randint(1,10)))%self.lenAkana
        y = random.randint(0,int((self.lenAkanaNum[x]-1)*random.uniform(0.1,1)*random.randint(1,10)))%self.lenAkanaNum[x]
        z = random.randint(1,100)%2
        print(f'[{x},{y},{z}]')
        return [x,y,z]

    def Logic(self):
        self.first = self.Random()
        self.second = self.Random()
        while self.second == self.first :
            self.second = self.Random()
        self.third = self.Random()
        while (self.third == self.second) or (self.third == self.first):
            self.third = self.Random()
        self.card1 = f'{self.akana[self.first[0]][self.first[1]]} {self.bit[self.first[2]]}'
        self.card2 = f'{self.akana[self.second[0]][self.second[1]]} {self.bit[self.second[2]]}'
        self.card3 = f'{self.akana[self.third[0]][self.third[1]]} {self.bit[self.third[2]]}'

    def Output(self):
        print(f'[CQ:at,qq={self.user}]\n{self.card1}\n{self.card2}\n{self.card3}\n{self.version}')

    def UserDataRead(self):
        data = self.cur.execute(f'select * from Tarot where User=\'{self.user}\' and Date=\'{self.date}\'')
        readData = data.fetchone()
        if not readData == None :
            print(f'[CQ:at,qq={self.user}]\n已于{readData[2]}-{readData[3]}进行抽取\n结果为:\n{readData[4]}\n{readData[5]}\n{readData[6]}\n{self.version}')
            return 1
        else:
            return 0

    def UserDataWrite(self):
        self.cur.execute(f'insert into Tarot values(?,?,?,?,?,?,?)', (self.user,self.group,self.date,self.time,self.card1,self.card2,self.card3))
        self.DB.commit()
        self.DB.close()

if __name__ == '__main__':
    #CLI: ./Tarot.py QQNumber GroupNumber
    #s = Tarot(sys.argv[-2],sys.argv[-1])
    s = Tarot(123456,1234)
    s.main()