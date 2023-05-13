from tkinter import *
from functools import partial
try:
	from Function import Function
except:
	print('not from Function import Function.')
import datetime as DT

def DebugConsole():
	root = Tk()
	root.title("Debug Console Ver_0.1.0")
	root.resizable(0, 0)
	#root.iconbitmap('./favicon.ico')#图标
	root.geometry(f'490x320+{int((root.winfo_screenwidth()-250)/2)}+{int((root.winfo_screenheight()-100)/2)}')#定义窗口大小与位置(宽x高+pos_x+pos_y)
	root.config(background="#efefef")
	window = Console(master=root)
	TIME = Console.Time(window)
	root.mainloop()

class Console(Frame):##窗口类
	def __init__(self,master=None):
		self.time_Var = StringVar()
		self.time_Var.set('__init__')
		self.alpha_Var = StringVar()
		self.alpha_Var.set('100.0%')
		self.topmost_text = StringVar()
		self.topmost_text.set('窗口置顶')
		self.UID_Var = StringVar()
		self.UID_Var.set('请输入欲发送用户对象编号')
		self.GID_Var = StringVar()
		self.GID_Var.set('请输入欲发送群组对象编号')
		self.message_Var = StringVar()
		self.message_Var.set('请输入欲发送信息')
		self.alpha = 1
		self.font='霞鹜文楷等宽'
		super().__init__(master)
		self.master = master
		self.Window()

	def Window(self):
		#窗口组件
		self.lable_alpha_text = Label(self.master, font=(self.font, 12, 'bold'), text='透明度', justify='left')
		self.lable_alpha = Label(self.master, font=(self.font, 12, 'bold'), textvariable=self.alpha_Var, justify='left')
		self.lable_alpha_text.place(x=10, y=10)
		self.lable_alpha.place(x=10, y=35)
		self.scale_alpha = Scale(self.master, from_=0.1, to=1, length=300, showvalue=False, orient="horizontal", resolution=0.001, command=partial(self.Alpha))
		self.scale_alpha.set(1)
		self.scale_alpha.place(x=70, y=25)
		self.topmost = Button(self.master, activeforeground='#f9245e', fg='#00baff', activebackground='#efefef', bg='#dfdfdf', command=self.Topmost, font=(self.font, 12, 'bold'), textvariable=self.topmost_text)
		self.topmost.place(x=390, y=15)
		self.lable_time = Label(self.master, textvariable=self.time_Var, fg='green', font=(self.font, 20))
		self.lable_time.place(x=80, y=60)
		self.Time()
		self.entry_UID = Entry(self.master, textvariable=self.UID_Var)
		#self.entry_UID["textvariable"] = self.UID_Var
		self.entry_UID.place(x=20, y=100)
		self.entry_GID = Entry(self.master, textvariable=self.GID_Var)
		#self.entry_GID["textvariable"] = self.GID_Var
		self.entry_GID.place(x=200, y=100)
		self.entry_message = Entry(self.master, textvariable=self.message_Var)
		#self.entry_message["textvariable"] = self.message_Var
		self.entry_message.place(x=20, y=140)
		self.send = Button(self.master, command=self.EntryText, font=(self.font, 12, 'bold'), text='发送')
		self.send.place(x=200, y=200)

	def Alpha(self, *arg):
		#透明度
		self.alpha = round(float(arg[0]), 3)
		self.master.attributes('-alpha',self.alpha)#透明度
		self.alpha_Var.set(f'{round(self.alpha*100, 1)}%')

	def Topmost(self):
		#窗口置顶
		#print(self.master.attributes()[11])
		if self.master.attributes()[11] == 0:
			self.master.attributes('-topmost', 1)
			self.topmost_text.set('取消置顶')
			self.topmost['fg'] = '#f9245e'
			self.topmost['activeforeground'] = '#00baff'
			#self.topmost['state'] = 'disable'
		elif self.master.attributes()[11] == 1:
			self.master.attributes('-topmost', 0)
			self.topmost_text.set('窗口置顶')
			self.topmost['fg'] = '#00baff'
			self.topmost['activeforeground'] = '#f9245e'

	def Time(self):
		#当前时间获取
		now = DT.datetime.now()
		date_F = now.date().strftime('%Y年%m月%d日')
		time_F = now.time().strftime('%H:%M:%S')
		self.time_Var.set(f'{date_F} {time_F}')
		self.master.after(1000, self.Time)

	def EntryText(self):
		uid = self.entry_UID.get()
		gid = self.entry_GID.get()
		if uid == '请输入欲发送用户对象编号':
			uid = ''
		if gid == '请输入欲发送群组对象编号':
			gid = ''
		mess = self.entry_message.get()
		s = Function.Send(uid,gid,mess)
		s.Send()


if __name__ == '__main__':
	DebugConsole()