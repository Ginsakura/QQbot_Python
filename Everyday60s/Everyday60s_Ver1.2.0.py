##Version 1.2.0##制图模块##修bug##
import io
import os
import re
import sys
from PIL import Image, ImageFont, ImageDraw, 
import sqlite3
import datetime
from requests_html import HTMLSession as html

def Get_Web_Page(url):
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
			Day60s(url60)
		else:
			return "Today not have Everyday 60 Second To Read The World's data."
	except:
		return "Not found the web page."

def Day60s(url60):
	day60 = html().get(url=url60, headers=UA)
	#imgf = open('./head.jpg','wb+')
	headimghtml = day60.html.find('figure>noscript>img',first=True).html
	headimgurl = re.findall(r'data-original="(.*)"/>',headimghtml)[0]
	headimg = html().get(url=headimgurl)
	#imgf.write(headimg.content)
	#imgf.close()
	headimg = headimg.content
	paragraph = day60.html.find('div.css-1yuhvjn>div>p')
	webdate = paragraph[1].text
	head = paragraph[2].text
	del paragraph[0:3]
	text = list()
	for i in paragraph:
		text.append(i.text)
	weiyu = text[len(text)-1]
	del text[len(text)-1]
	weiyu = re.findall(r'(【.*)')[0]
	text.append(weiyu)
	Image(headimg, webdate, text)

def Image(headimg, date, text):#头图bin，日期，正文传入
	#创建内存对象
	File = io.BytesIO()
	#字体路径
	fontPath = './LXGW.ttf'
	#创建字体对象
	font = ImageFont.truetype(fontPath, 25)
	#高度计算
	hight = Hight(text)
	#文本整合
	for i in text:
		textn += f'{i}\n'
	#新建图像对象
	img = Image.new('RGB', (750,hight), color="#f0f0f0")
	#创建绘图对象
	draw=ImageDraw.Draw(img)
	#文本写入
	ImageDraw.multiline_text((45, 490), text=textn, fill='#303030', font=font, spacing=25)
	#头图传入
	#标题写入
	#边框绘制
	#内存写入
	#图片存储
	img.show()#图像渲染与显示

def Hight(text):
	frame = 90			#上下留白高度
	headi = 300			#头图高度
	headt = 150			#头部文本高度
	lineNum = 1			#初始化正文部分（1行留白）
	for i in text:
		lineNum += len(i)//25+1		#25字/行，整除，行间距1行
		if not len(i)%25 == 0:		#判断是否满行
			lineNum += 1
	mainTextHight = lineNum*25		#正文总高度
	totalHight = frame+headi+headt+mainTextHight
	return totalHight


if __name__ == '__main__':
	global month,day,UA
	date = datetime.date.today()
	month,day = date.month,date.day
	#today = f'{date.year}-{date.month}-{date.day}'
	url = 'https://www.zhihu.com/people/mt36501/posts'
	UA = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
	Get_Web_Page(url)