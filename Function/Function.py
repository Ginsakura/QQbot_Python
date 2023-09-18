import re
import os
import json
import requests
import base64
import sqlite3
from datetime import datetime as dt
from urllib import parse

'''
Unknown data
修改群名片
{'post_type': 'notice', 
	'notice_type': 'group_card', 
	'time': 1684236089, 
	'self_id': 3558323607, 
	'group_id': 590906542, 
	'user_id': 1176093801, 
	'card_new': '燃烧的羽翼，带我脱离凡间的沉沦', 
	'card_old': '逐龙'}
加好友
{'post_type': 'notice', 
	'notice_type': 'friend_add', 
	'time': 1684235345, 
	'self_id': 3558323607, 
	'user_id': 610365292}
客户端登录状态改变
{'post_type': 'notice', 
	'notice_type': 'client_status', 
	'time': 1684228833, 
	'self_id': 3558323607, 
	'online': False, 
	'client': {
		'app_id': 537158638, 
		'device_kind': 
		'Android', 
		'device_name': 'Android'
		}
	}
群文件
{'post_type': 'notice', 
	'notice_type': 'group_upload', 
	'time': 1684241014, 
	'self_id': 3558323607, 
	'group_id': 734026981, 
	'user_id': 1985298468, 
	'file': {
		'busid': 102, 
		'id': '/e0986e7e-1ba3-4d14-b98d-6adf48a481a9', 
		'name': '2.mp4', 
		'size': 50839573, 
		'url': 'http://183.60.225.93/ftn_handler/aef3c7918eb902b9bfa7c95ff7022c254e90231f004d9eacdfe2c5df8aae624f5764b4f184d4c6d17009015a675b2800db0e721eb035926ad681b56cce01064d/?fname=2f65303938366537652d316261332d346431342d623938642d366164663438613438316139'
		}
	}
{'post_type': 'notice', 
	'notice_type': 'group_decrease', 
	'time': 1684240295, 
	'self_id': 3558323607, 
	'sub_type': 'kick_me', 
	'user_id': 3558323607, 
	'group_id': 752285699, 
	'operator_id': 2602961063}

'''

class MessageProcess():
	def __init__(self,messageJson):
		self.messageJson = messageJson
		self.unknownData = False
		self.master = 2602961063
		
		#消息主类型筛选
		self.postType = messageJson['post_type']					#主类型: message/notice
		self.time = messageJson['time']								#UTC时间戳
		self.selfId = messageJson['self_id']						#本机ID
		self.groupId = messageJson['group_id'] if 'group_id' in messageJson else -1
																	#群聊消息存在group id
		self.userId = messageJson['user_id']						#消息发送者和触发者,禁言的被操作者

		if self.postType == 'message':								#message子类
			self.messageType = messageJson['message_type']			#消息类型: group/private
			self.subType = messageJson['sub_type'] 					#消息子类型: normal/friend
			self.messageId = messageJson['message_id']				#消息编号
			self.font = messageJson['font']								#字体(未收集数据)
			self.message = messageJson['message']					#消息(Json格式)
			# if self.message[0]['type'] == 'json':print(messageJson)
			self.rawMessage = messageJson['raw_message']			#消息(CQ转义与合并)
			self.senderNickname = messageJson['sender']['nickname']	#发送者昵称
			self.senderSex = messageJson['sender']['sex']				#性别?
			self.senderUserId = messageJson['sender']['user_id']	#发送者QQ号
			self.senderAge = messageJson['sender']['age']				#Q龄?

			if self.messageType == 'group':							#群聊消息子类
				self.anonymous = messageJson['anonymous']				#匿名消息字段(未收集数据)
				self.messageSeq = messageJson['message_seq']		#群聊消息序号
				self.senderArea = messageJson['sender']['area']			#发送者地区?
				self.senderCard = messageJson['sender']['card']		#发送者群昵称
				self.senderLevel = messageJson['sender']['level']	#发送者群等级
				self.senderRole = messageJson['sender']['role']		#发送者群权限: member/admin/owner

			elif self.messageType == 'private':						#私聊消息子类
				self.targetId = messageJson['target_id']			#私聊消息发送者
				if not self.subType == 'friend':
					print(messageJson)
					print('Unknown Private Message SubType.')

		elif self.postType == 'notice':								#notice子类
			self.noticeType = messageJson['notice_type']			#通知类型

			if self.noticeType == 'notify':							#普通通知(poke)子类
				self.subType = messageJson['sub_type'] 				#通知子类型: poke
				self.targetId = messageJson['target_id']			#通知的对象(被戳者)
				self.senderId = messageJson['sender_id']			#通知的发送者

			elif self.noticeType == 'group_ban':					#禁言通知子类
				self.subType = messageJson['sub_type'] 				#通知子类型: ban/lift_ban
				self.duration = messageJson['duration']				#禁言时间(秒)
				self.operatorId = messageJson['operator_id']		#操作员

			elif self.noticeType == 'group_recall':					#群聊撤回通知
				self.messageId = messageJson['message_id']			#撤回的消息id
				self.operatorId = messageJson['operator_id']		#撤回者

			elif self.noticeType == 'group_increase':				#新人入群
				self.subType = messageJson['sub_type']				#approve
				self.operatorId = messageJson['operator_id']

			elif self.noticeType == 'group_decrease':				#群员离群
				self.subType = messageJson['sub_type']				#leave/kick/kick_me
				self.operatorId = messageJson['operator_id']

			else:
				print(messageJson)
				print('Unknown Notice Type.')
				self.unknownData = True

		elif self.postType == 'request':							#request子类
			self.requestType = messageJson['request_type']			#
			self.subType = messageJson['sub_type']
			if self.requestType == 'group' and self.subType == 'invite':#群邀请
				self.comment = messageJson['comment']
				self.flag = messageJson['flag']
				self.invitorId = messageJson['invitor_id']
			else:
				print(messageJson)
				print('Unknown Request Type.')
				self.unknownData = True

		else:
			print(messageJson)
			print('Unknown Message Type.')
			self.unknownData = True

	def ResourceExtraction(self):
		imagere = '[CQ:image,file=([a-fA-F0-9]{32}).image'
		audiore = '[CQ:record,file=([a-fA-F0-9]{32}).amr'
		facere = '[CQ:face,id=([0-9]{1,3})]'

	def RequestBypass(self):
		if self.unknownData:
			return 'unknown'
		elif self.userId == self.master:
			result = requests.post(url=f'http://127.0.0.1:5700/set_group_add_request?flag={self.flag}&type={self.subType}')
			print(result)
		return 'Request Match Over'

	def NoticeBypass(self):
		if self.unknownData:
			return 'unknown'
		elif self.noticeType == 'group_increase':
			if self.userId == self.selfId:
				self.MessageSend('nya~')
				self.MessageSend(f'[CQ:image,file=file:///{os.getcwd()}/Images/help.png]')
			else:
				self.MessageSend(f"[CQ:at,qq={self.userId}]\n欢迎喵~\n[CQ:image,file=file:///{os.getcwd()}/Images/welcome.jpg]")
		elif self.noticeType == 'group_ban':
			if self.subType == 'ban':
				message = f'在群 {self.groupId}中, {self.userId}被 {self.operatorId}禁言 {self.duration//86400}天{(self.duration%86400)//3600}时{(self.duration%3600)//60}分{self.duration%60}秒'
			elif self.subType == 'lift_ban':
				message = f'在群 {self.groupId}中, {self.userId}被 {self.operatorId}解除禁言'
			Send(msg=f'{dt.now()}\n{message}').Send()
		elif self.noticeType == 'group_decrease':
			if self.subType == 'kick':
				message = f"在群 {self.groupId}中, {self.userId}被 {self.operatorId}踢出群聊"
			elif self.subType == 'leave':
				message = f"在群 {self.groupId}中, {self.userId}退出群聊"
			elif self.subType == 'kick_me':
				message = f"姐——我在{self.groupId}里被{self.operatorId}踢出来了————"
			Send(msg=f'{dt.now()}\n{message}').Send()
		# if self.sub_type == 'poke':
		# 	MessageProcess.Poke(self)
		# elif self.message_source == 'group':
		# 	MessageProcess.GroupMessage(self)
		# elif self.message_source == 'private':
		# 	MessageProcess.PrivateMessage(self)
		return 'Notice Match Over'

	def MessageBypass(self):
		#self.SQL_Write()
		#消息类型判断
		if self.unknownData:
			return 'unknown'
		elif re.search(r'(\.|。)?(jrys|今日运势)',self.rawMessage):
			from Plugins import Fortune
			self.MessageSend(Fortune.Fortune(self.userId,self.groupId).Main())
		elif '/help' == self.rawMessage:
			self.MessageSend(f'[CQ:image,file=file:///{os.getcwd()}/Images/help.png]')
		elif '网易云' == self.rawMessage[0:3]:
			res = requests.post(url=f'http://127.0.0.1:5700/can_send_record')
			print(res.text)
			from Plugins import Cloudmusic
			self.MessageSend(Cloudmusic.Cloudmusic(self.userId,self.rawMessage).Main())
		# elif self.rawMessage == 'image':
		# 	self.SendMessage = f'[CQ:image,file=file:///{os.getcwd()}/go-cqhttp/data/images/t.png]'
		# 	self.MessageSend()
		elif self.rawMessage[0:2] == '幻樱':
			if self.userId == 2602961063:
				self.MessageSend('贴姐姐)')
			else:
				import random
				recall = ['怎么了?','有什么事吗?','叫我吗?','呜喵?','需要帮忙吗?','?','']
				recall = recall[random.randint(0,len(recall)-1)]
				if not recall == '':
					self.MessageSend(recall)
		elif (self.userId == 2602961063) and (self.rawMessage == '系统状态'):
			from Plugins import System_Statu
			self.MessageSend(System_Statu.main())
		elif (self.userId == 2602961063) and (self.rawMessage == 'reload') :
			self.MessageSend('Function Reloading...')
			return 'reload',self.groupId
		elif self.rawMessage == '塔罗牌Test' or self.rawMessage == '塔罗牌':
			from Plugins import Tarot
			self.SendMessage = '暂未开放'
			self.MessageSend(Tarot.main(self.userId))
		elif re.search(r'(\.|。)?(jrxw|今日新闻)',self.rawMessage):
			from Plugins import Everyday60s
			ed60s = Everyday60s.ED60S().GetWebPage()
			print(ed60s)
			self.MessageSend(ed60s)
		elif (self.userId == 2602961063) and (self.rawMessage == '一键三联'):
			from Plugins import Fortune
			self.MessageSend(Fortune.Fortune(self.userId,self.groupId).Main())
			from Plugins import Everyday60s
			ed60s = Everyday60s.ED60S().GetWebPage()
			print(ed60s)
			self.MessageSend(ed60s)
			from Plugins import System_Statu
			self.MessageSend(System_Statu.main())
		elif (self.userId == 2602961063) and (self.rawMessage[0:4] == 'exec'):
			if self.rawMessage[4] == ' ':
				exec(self.rawMessage[5:])
			else:
				exec(self.rawMessage[4:])
		return 'Message Match Over'

	def SQL_Write(self):
		DB = sqlite3.connect('./Data/Message.db')
		cur = DB.cursor()
		cur.execute('insert into message values(NULL,?,?,?,?,?,?,?,?,?,?,?)', (self.font,self.sub_type,self.message_id,self.message_type,self.raw_message,self.sender_age,self.sender_nickname,self.sender_sex,self.sender_id,self.SubID,self.target_id,self.self_id,self.time))
		if self.message_type == 'group':
			cur.execute('insert into group_message values(?,?,?,?,?,?,?,?)', (self.SubID,self.anonymous,self.group_id,self.sender_area,self.sender_group_nickname,self.sender_level,self.sender_role,self.sender_title))
		DB.commit()
		DB.close()

	# def Poke(self):
	# 	#戳一戳
	# 	self.SendMessage = f'It\'s a poke by {self.sender_id}.'
	# 	MessageProcess.MessageSend()

	# def GroupMessage(self,):
	# 	#群组消息
	# 	self.SendMessage = f'It\'s a group message by {self.group_id} group and {self.sender_id} user.'
	# 	MessageProcess.MessageSend()

	# def PrivateMessage(self):
	# 	#私聊消息
	# 	self.SendMessage = f'It\'s a private message by {self.sender_id}.'
	# 	MessageProcess.MessageSend()

	def MessageSend(self,message):
		#消息发送
		if self.groupId == -1:
			result = requests.post(url=f'http://127.0.0.1:5700/send_private_msg?user_id={self.userId}&message={message}')
		else:
			result = requests.get(url=f'http://127.0.0.1:5700/send_group_msg?group_id={self.groupId}&message={message}')
		print(result)

class Send():
	def __init__(self, uid=-1, gid=-1, msg=''):
		self.uid = uid
		self.gid = gid
		self.message = msg

	def Send(self):
		if (self.gid == -1) and (self.uid == -1):
			result = requests.post(url=f'http://127.0.0.1:5700/send_private_msg?user_id=2602961063&message={self.message}')
		elif (self.gid == -1) and (not self.uid == -1):
			result = requests.post(url=f'http://127.0.0.1:5700/send_private_msg?user_id={self.uid}&message={self.message}')
		elif (not self.gid == -1) and (not self.uid == -1):
			result = requests.get(url=f'http://127.0.0.1:5700/send_group_msg?group_id={self.gid}&message=[CQ:at,qq={self.uid}]\n{self.message}')
		else:
			result = requests.get(url=f'http://127.0.0.1:5700/send_group_msg?group_id={self.gid}&message={self.message}')
		print(result)