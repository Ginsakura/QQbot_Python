import io
import os
import re
import sys
from PIL import Image, ImageFont, ImageDraw
import sqlite3
import datetime
from base64 import b64decode
from requests_html import HTMLSession as html

class ED60S(object):
	"""docstring for ED60S"""
	def __init__(self):
		super(ED60S, self).__init__()
		self.rootUrl = 'https://www.zhihu.com/people/mt36501'
		self.UA = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
		dateToday = datetime.date.today()
		self.date = [dateToday.year,dateToday.month,dateToday.day]
		self.web = None
		self.webDate = None
		self.webData = None
		self.dayLink = None
		self.d60Url = None
		self.Headimg = io.BytesIO(b64decode("iVBORw0KGgoAAAANSUhEUgAAAEgAAAAoCAIAAADSeytKAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALRSURBVGhD7ZihkrMwEMfzfS/CRHTO5wkyFVV1KGRU1RlkRQUCWYNCRaLqTiFu8gT4zgmGN7n/JqEFSntT5ubmuOFngE3J7j/Z3XT4V9c1+4v899c/xyJsbizC5sYibG4swubGImxuLMLmxuDffaP1O2N8rWRAT2afl6tNqqQbfYbGmMvE5INzJSdMM5n+jjXvbwlQuXHP9bkoktI/PEddl2WZZUqprIQqzrgf+CHGU7GYJqaLVGmavr7Q7WotAaXADzIqTIjzVZlYdde6sfiH53Gvd/EDHm+0eJPFmyze5PC224hGhVVVVWR68GOzD0POZRzHUnIe7ifsaaPx7gAeto7ggEvM7wdib0ehk/060L7gB+I8p4iGAY0Ji6JICPb2fq1+8qqKqop0fTqdah2xEeVfE3CbmuJwiNqrdYSJGh3CgTgYTG8OgoYtWAtnh2P4pYEXbhsbDTAKKE2PeKEalM/ojm12W+xaolRSOUOjs4IC2bm+xldwUNmAJiC2a5vc9orkqD5qZvI3FMDhqChmr59w9ujV2uHXGgmTIzaxtQE19YePs8N48wjW2+uiAfsmAvENAJ4Flvr7aOozBLqtsE/2erFvhueEW2isbYx+G8YZO2hj0t6vxoWxQL3abBmnH8c30F/ysQ0gcBj5Abey2OETjkgUB07aYBDMHWFo17tOpssNZF5yz6YBi27WcTo2tz1Uzf7WZw6qp6FWEbeV0SYlctiCMdCv+bvCLptGJQCZKNwqkeEenQiOUc39nR/QaPTQMLQhVklM94/aqPNVKOq7qhBoXn4dA3WE43MWI9/O7KoedrQBeoECkuqMvuDqsOWLD6Y4IYLOJvsDo2uaymBmws3et/ZsZk+y0TlbDQ/i+eVfgnEKyKQSkT7uWG4bf6RPD3Ol5fd/4m6MzssPulttduubJnGP5dv93FiEzY1F2NxYhM2NRdjcWITNC8Y+AQqKke12y8pfAAAAAElFTkSuQmCC"))
		self.version = "2.0.2"
		self.updateText = "Bug Fix"

	def GetWebPage(self):
		try:
			self.web = html().get(url=self.rootUrl, headers=self.UA)
			self.webDate = self.web.html.find("div.List-item>div.List-itemMeta>div.ActivityItem-meta",first=True)
		except:
			return "LinkError!"
		try:
			if self.webDate.text[5:15] == ("%d-%02d-%02d"%(self.date[0],self.date[1],self.date[2])):
				self.dayLink = self.web.html.find('h2.ContentItem-title>span>a',first=True).absolute_links
				self.d60Url = "".join(self.dayLink)
				print(self.d60Url)
			else:
				print("404 Not Found.")
		except Exception as e:
			print("Not found the web page.")
		if os.path.isfile(f'./Img/Everyday60s-{"%d.%02d.%02d"%(self.date[0],self.date[1],self.date[2])}.png'):
			self.Output()
		elif not self.d60Url is None:
			self.Day60s()
		else:
			print("Find Link Error.")

	def Day60s(self):
		#print("d60s")
		# self.d60Url = "https://zhuanlan.zhihu.com/p/604372811"
		day60 = html().get(url=self.d60Url, headers=self.UA)
		#imgf = open('./head.jpg','wb+')
		try:
			headimghtml = day60.html.find('div.RichText>figure>noscript>img',first=True).html
			headimgurl = re.findall(r'data-original="(.*)"/>',headimghtml)[0]
			headimg = html().get(url=headimgurl)
			#imgf.write(headimg.content)
			#imgf.close()
			#headimg = headimg.content
			self.Headimg = io.BytesIO(headimg.content)
		except:
			print("Not Find HeadImg")
		try:
			paragraph = day60.html.find('div.css-376mun>div.css-1g0fqss>p')
			self.webDate = paragraph[0].text
		except:
			print("Text Find Error")
		head = paragraph[2].text
		# print([i.text for i in paragraph])
		if paragraph[0].text == '':del paragraph[0]
		del paragraph[0:2]
		text = list()
		for i in paragraph:
			text.append(i.text)
		#print(len(text))
		if len(text) == 0:
			self.DownloadImg(day60.html.find('div.css-1yuhvjn>div>figure>img'))
		else:
			if text[-1] == '':
				text.pop(-1)
			self.MakeImage(text)

	def DownloadImg(self,imgUrl):
		src = imgUrl[0].attrs.get("data-original")
		try:
			#保存图片
			r_save_pic = html().get(src, headers = self.UA)
			# r.content
			with open(f'./Img/Everyday60s-{"%d.%02d.%02d"%(self.date[0],self.date[1],self.date[2])}.png','wb+') as fp:
				fp.write(r_save_pic.content)
			fp.close()
			self.OutPut()
		except Exception as msg:
			print(f"下载中出现异常:{str(msg)}")

	def MakeImage(self, text):#日期，正文传入
		#print("img")
		#创建内存对象
		#File_RAM = io.BytesIO()
		#创建文件对象
		if not os.path.exists('./Img/'):
			os.makedirs('./Img/')
		File_Disk = open(f'./Img/Everyday60s-{"%d.%02d.%02d"%(self.date[0],self.date[1],self.date[2])}.png','wb+')
		#字体路径
		fontPath = './LXGW_Bold.ttf'#粗体
		#fontPath = './LXGW.ttf'#常规
		#创建字体对象
		text_font = ImageFont.truetype(fontPath, 30)
		date_font = ImageFont.truetype(fontPath, 40)
		title_font = ImageFont.truetype(fontPath, 50)
		#高度计算
		hight, txt, line = self.Hight(text)
		#文本整合
		textn = ''
		for i in txt:
			textn += i + '\n'
		#新建图像对象
		img = Image.new('RGB', (800,hight), color="#f3f3f3")
		#创建绘图对象
		draw=ImageDraw.Draw(img)
		#头图传入
		headimg = Image.open(self.Headimg)
		headimg = headimg.resize((720, 400))
		img.paste(headimg, box=(40,40))
		#标题写入
		draw.multiline_text((200, 480), text='每天60秒读懂世界', fill='#ff3300', font=title_font, spacing=5)
		draw.multiline_text((110, 560), text=self.webDate, fill='#ff9922', font=date_font, spacing=5)
		#边框绘制
		draw.rectangle([(18,18), (782,hight-18)], outline='#444444', width=4)
		draw.line([(40,460), (760,460)], fill='#444444', width=4)
		draw.line([(50,550), (750,550)], fill='#666666', width=2)
		draw.line([(22,615), (778,615)], fill='#666666', width=4)
		for i in line:
			draw.line([(22,630+(i*34)), (778,630+(i*34))], fill='#888888', width=2)
		#文本写入
		draw.multiline_text((40, 630), text=textn, fill='#303030', font=text_font, spacing=5)
		#图片存储
		img.save(File_Disk)
		File_Disk.close()
		#内存写入
		#img.save(File_RAM, 'png')
		#图像渲染与显示
		#img.show()
		self.Output()


	def Output(self):
		print(f'[CQ:image,cache=0,file=file:///C:/Users/Administrator/Desktop/MiraiCQ/Img/Everyday60s-{"%d.%02d.%02d"%(self.date[0],self.date[1],self.date[2])}.png]')
	
	def Hight(self,text):
		#print("hight")
		frame = 80			#上下留白高度
		headi = 400			#头图高度
		headt = 150			#头部文本高度
		lineNum = 0			#初始化正文部分（1行留白）
		line = list()
		txtn = list()
		for i in text:
			lenth = 0
			txt = ''
			for j in i:
				if j >= '~':
					lenth += 2
				else:
					lenth += 1
				txt += j
				if lenth > 47:
					txt += '\n'
					lenth = 0
					lineNum += 1
			txt += '\n'
			lineNum += 2
			txtn.append(txt)
			#print(txt)
			#lineNum += len(i)//24+1		#25字/行，整除，行间距1行
			#if not len(i) % 24 == 0:		#判断是否满行
			#	lineNum += 1
			line.append(lineNum-0.5)
			#print(lineNum)
		mainTextHight = lineNum*34		#正文总高度
		del line[len(line)-1]
		totalHight = frame+headi+headt+mainTextHight
		return totalHight, txtn, line

if __name__ == '__main__':
	ED60S().GetWebPage()
