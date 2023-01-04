##Version 0.0.1##一切的开始##
import os
import sys
import sqlite3
import datetime

##Global##
global team,data,date,user,DB,cur
Path = f'./Data/'
File = 'Costom_Welcome_Data.db'
Table = 'Costom_Welcome'
##Global##

def Premise():
    global DB,cur
    if not os.path.exists(Path) :
        os.makedirs(Path)
        if not os.path.isfile(Path+File) :
            New_Database = sqlite3.connect(Path+File)
            cur = New_Database.cursor()
            cur.execute(f'''
                Create table 
                {Table} (
                Team integer Primary Key,
                Date text,
                Text Text,
                Oprater integer)''')
            cur.execute(f'insert into {Table} values(?,?,?,?)', (1000000,"0000-00-00 00:00","欢迎……",1000000))
            New_Database.commit()
            New_Database.close()
    DB = sqlite3.connect(Path+File)
    cur = DB.cursor()

def Main(cmd):
    global team,data,date,user,DB,cur
    Now = datetime.datetime.now()
    date = f"{Now.year}-{Now.month}-{Now.day} {Now.hour}:{Now.minute}"
    if cmd == 'set':
        Write()
    elif cmd == 'read':
        Read()

def Read():
    global team,data,date,user,DB,cur
    exist = cur.execute(f"select Text from {Table} where Team=\'{team}\'")
    exist = exist.fetchone()
    if exist == None :
        print('欢迎~')
    else :
        print(exist[0])

def Write():
    global team,data,date,user,DB,cur
    cur.execute(f'insert into {Table} values(?,?,?,?)', (team,date,data,user))
    DB.commit()
    print(data)

if __name__ == '__main__':
    global team,data,date,user
    command,team,data,user = 'read',101010,"taemfghakjgkjagfkjdsg,zjhgfhjefraukeygkjt",10000
    #command = sys.argv[1]#command=set/read
    #team = sys.argv[2]
    #data = sys.argv[3]
    #user = sys.argv[4]
    Premise()
    Main(command)



'''
exist = cur.execute(f"select Team from {Table} where Team='{Team}'")
exist = exist.fetchone()
    if exist == None :
'''