import sqlite3
import os

def get_files():
    for filepath,dirnames,filenames in os.walk('./csv/'):
        for filename in filenames:
        	Read(filename)

def Read(filename):
	db=sqlite3.connect('./Fortune_Data.db')
	cur=db.cursor()
	print(filename)
	f = open(f'./csv/{filename}')
	num=0
	for i in f:
		if num==0:
			num+=1
			continue
		j = i.split(',')
		#print(j)
		try:
			user=int(j[0][1:-1])
			group=-1
			date=filename[0:-4]
			time=j[1][1:-1]
			main=int(j[2][1:-1])
			extra=int(j[3][1:-2])
		except:
			num+=1
			continue
		#print(user,date,time,main,extra)
		try:
			cur.execute('insert into Fortune values(?,?,?,?,?,?)', (user,group,date,time,main,extra))
		except Exception as e:
			print(e)
		num+=1
	db.commit()
	db.close()

if __name__ == '__main__':
	get_files()