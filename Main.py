from flask import Flask, request
from Function import Function as Fun
from Function import DebugConsole as DBC
from Function import GoCQHttpLog as GCQH
from threading import Thread
import os
from importlib import reload
from datetime import datetime as dt


app = Flask('Ginsakura\'s Bot Frame')

@app.route('/', methods=["POST"])
def PostData():##接收Json，传递给data
	data = request.get_json()
	# if not data["post_type"] == "meta_event":
	# 	# print(data)
	# 	messageData = Fun.MessageProcess(data)
	# 	if data['post_type'] == 'message':
	# 		statu = messageData.MessageBypass()
	# 	elif data['post_type'] == 'notice':
	# 		statu = messageData.NoticeBypass()
	try:
		if not data["post_type"] == "meta_event":
			# print(data)
			messageData = Fun.MessageProcess(data)
			if data['post_type'] == 'message':
				statu = messageData.MessageBypass()
			elif data['post_type'] == 'notice':
				statu = messageData.NoticeBypass()
			elif data['post_type'] == '':
				statu = messageData.RequestBypass()
			if statu[0] == 'reload':
				reload(Fun)
				reload(DBC)
				Fun.Send(gid=statu[1],msg='Reload Success.').Send()
			elif statu == 'unknown':
				with open('./error.log','a',encoding='utf8') as f:
					f.write(f'{dt.now()}  Unknown\n')
					f.write(str(data)+'\n')
	except Exception as e:
		print(e)
		print(data)
		with open('./error.log','a',encoding='utf8') as f:
			f.write(f'{dt.now()}  {str(e)}\n')
			f.write(str(data)+'\n')
	return 'OK'

def HTTP_Server():
	# 此处的 host和 port对应上面 yml文件的设置
	#保证和我们在配置里填的一致
	app.run(host='127.0.0.1', port=5710) 

def thread_start():##多线程（其实没必要）
	#Go_CQHttp = Thread(target=GCQH.CQhttp)
	#Go_CQHttp.start()
	#Go_CQHttp.join()

	HttpServer = Thread(target=HTTP_Server)
	HttpServer.start()
	HttpServer.join()

	# Debug_Console = Thread(target=DBC.DebugConsole)
	# Debug_Console.start()
	# Debug_Console.join()

if __name__ == '__main__':
	os.system('color 02')
	# thread_start()
	HTTP_Server()