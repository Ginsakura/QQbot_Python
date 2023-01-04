##Version 0.0.1##
import sqlite3
import datetime

class FS():
	def __init__(self,user,group):
		super(FS, self).__init__()
		self.version = '0.0.1 Pre'
		self.path = './Data/'
		self.file = 'Favorability_Data.db'
		self.DB = None
		self.cur = None
		
		self.user = user
		self.group = group

		#self.changeNum = Num
		#self.changeType = Type

		self.now = datetime.datetime.now()
		self.time = self.now.strftime('%H:%M:%S')
		self.date = self.now.strftime('%Y.%m.%d')





if __name__ == '__main__':
	#CLI: ./FS.py QQNumber GroupNumber
	#s = FS(sys.argv[-2],sys.argv[-1])
	s = FS(123456,1234,0.5,'add')
	s.main()