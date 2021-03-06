##Version 1.2.4##制图模块##排版##
import io
import os
import re
import sys
from PIL import Image, ImageFont, ImageDraw
import sqlite3
import datetime
from requests_html import HTMLSession as html

def Get_Web_Page(url):
	print("GWP")
	try:
		web = html().get(url=url, headers=UA)
		date_web = web.html.find('h2>a',first=True)
	except:
		return "LinkError!"
	try:
		req = re.findall(r'([0-9]{0,2})月([0-9]{0,2})日',date_web.text)
		if req[0][0] == f"{month}" and req[0][1] == f'{day}' :
			dayLink = web.html.find('h2>a',first=True).absolute_links
			url60 = "".join(dayLink)
		else:
			return "Today not have Everyday 60 Second To Read The World's data."
	except:
		return "Not found the web page."
	Day60s(url60)

def Day60s(url60):
	print("d60s")
	day60 = html().get(url=url60, headers=UA)
	#imgf = open('./head.jpg','wb+')
	headimghtml = day60.html.find('figure>noscript>img',first=True).html
	headimgurl = re.findall(r'data-original="(.*)"/>',headimghtml)[0]
	headimg = html().get(url=headimgurl)
	#imgf.write(headimg.content)
	#imgf.close()
	#headimg = headimg.content
	Headimg = io.BytesIO(headimg.content)
	paragraph = day60.html.find('div.css-1yuhvjn>div>p')
	webdate = paragraph[1].text
	head = paragraph[2].text
	del paragraph[0:3]
	text = list()
	for i in paragraph:
		text.append(i.text)
	weiyu = text[len(text)-1]
	del text[len(text)-1]
	weiyu = re.findall(r'(【.*)', weiyu)[0]
	text.append(weiyu)
	Make_Image(Headimg, webdate, text)

def Make_Image(headimage, date, text):#头图bin，日期，正文传入
	print("img")
	#创建内存对象
	#File_RAM = io.BytesIO()
	#创建文件对象
	if not os.path.exists('./Img/'):
		os.makedirs('./Img/')
	File_Disk = open(f'./Img/Everyday60s-{year}.{month}.{day}.png','wb+')
	#字体路径
	fontPath = './LXGW_Bold.ttf'#粗体
	#fontPath = './LXGW.ttf'#常规
	#创建字体对象
	text_font = ImageFont.truetype(fontPath, 30)
	date_font = ImageFont.truetype(fontPath, 40)
	title_font = ImageFont.truetype(fontPath, 50)
	#高度计算
	hight, line = Hight(text)
	#文本整合
	textn, j = '', ''
	for i in text:
		while len(i) > 24:
			j += f'{i[0:24]}\n'
			i = i[24:]
		i = j + i +'\n'
		j = ''
		textn += i+'\n'
	#新建图像对象
	img = Image.new('RGB', (800,hight), color="#f3f3f3")
	#创建绘图对象
	draw=ImageDraw.Draw(img)
	#头图传入
	headimg = Image.open(headimage)
	headimg = headimg.resize((720, 400))
	img.paste(headimg, box=(40,40))
	#标题写入
	draw.multiline_text((200, 480), text='每天60秒读懂世界', fill='#ff3300', font=title_font, spacing=5)
	draw.multiline_text((110, 560), text=date, fill='#ff9922', font=date_font, spacing=5)
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
	img.show()

def Hight(text):
	print("hight")
	frame = 80			#上下留白高度
	headi = 400			#头图高度
	headt = 150			#头部文本高度
	lineNum = 1			#初始化正文部分（1行留白）
	line = list()
	for i in text:
		lineNum += len(i)//24+1		#25字/行，整除，行间距1行
		if not len(i) % 24 == 0:		#判断是否满行
			lineNum += 1
		line.append(lineNum-1.5)
	mainTextHight = lineNum*34		#正文总高度
	del line[len(line)-1]
	totalHight = frame+headi+headt+mainTextHight
	return totalHight, line

if __name__ == '__main__':
	global year, month, day, UA
	date = datetime.date.today()
	year, month, day = date.year, date.month, date.day
	#today = f'{date.year}-{date.month}-{date.day}'
	url = 'https://www.zhihu.com/people/mt36501/posts'
	UA = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
	Get_Web_Page(url)