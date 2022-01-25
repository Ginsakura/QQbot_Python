##Version 1.0.0##爬虫与框架##
import os
import re
import sys
import PIL
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
	imgf = open('./head.jpg','wb+')
	headimghtml = day60.html.find('figure>noscript>img',first=True).html
	headimgurl = re.findall(r'data-original="(.*)"/>',headimghtml)[0]
	headimg = html().get(url=headimgurl)
#	imgf.write(headimg.content)
#	imgf.close()
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
	Image(headimg, webdate, text, weiyu)

def Image(headimg, date, text, weiyu):


if __name__ == '__main__':
	global month,day,UA
	date = datetime.date.today()
	month,day = date.month,date.day
#	today = f'{date.year}-{date.month}-{date.day}'
	url = 'https://www.zhihu.com/people/mt36501/posts'
	UA = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
	Get_Web_Page(url)