from flask import Flask, request
import json
 
import requests
import re
import random


app = Flask(__name__)

@app.route('/', methods=["POST"])
def PostData():
    data = request.get_json()
    print(data)
    if 'message_type' in data:
        if data['message_type'] == 'group':  # 如果是群聊信息
            gid = data['group_id']  # 获取群号
            uid = data['sender']['user_id']  # 获取信息发送者的 QQ号码
            message = data['raw_message']  #获取原始信息
            print(f'Group Msg:\tuid={uid}\tgid={gid}')
            keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        if data['message_type'] == 'private':
            uid = data['sender']['user_id']
            msg = data['raw_message']
            print(f'Private Msg:\tuid={uid}')
            keyword(msg,uid,gid=0)
    else:
        print("No Data.")
    return 'OK'
#{'interval': 5000, 'meta_event_type': 'heartbeat', 'post_type': 'meta_event', 'self_id': 3182043423, 'status': {'app_enabled': True, 'app_good': True, 'app_initialized': True, 'good': True, 'online': True, 'plugins_good': None, 'stat': {'packet_received': 32, 'packet_sent': 23, 'packet_lost': 0, 'message_received': 1, 'message_sent': 1, 'disconnect_times': 0, 'lost_times': 0, 'last_message_time': 1649341952}}, 'time': 1649342010}
#{'anonymous': None, 'font': 0, 'group_id': 755940124, 'message': [{'data': {'text': '？？？'}, 'type': 'text'}], 'message_id': 1166179725, 'message_seq': 1552, 'message_type': 'group', 'post_type': 'message', 'raw_message': '？？？', 'self_id': 3182043423, 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': '乐正银樱', 'role': 'member', 'sex': 'unknown', 'title': '', 'user_id': 2602961063}, 'sub_type': 'normal', 'time': 1649342041, 'user_id': 2602961063}

#'下面这个函数用来判断信息开头的几个字是否为关键词'
def keyword(message, uid, gid):
    if gid != 0:
        if message[0:2] == '你好':
            group_send(uid,gid,"你也好啊!@#$%^&*()_+！")
    else:
        if re.match(r'.*？.*',message) != None:
            private_send(uid,message)
 
def group_send(uid, gid, message):
    '''群消息'''
    message = str(message)
    sign = {"&": "%26", "+": "%2B", "#": "%23"}
    print(f'Group Send:\tuid={uid}\tgid={gid}')
    for i in sign:
        message = message.replace(i, sign[i]) #防止在请求中特殊符号出现消息错误
    if uid != 0:
        message = f"[CQ:at,qq={uid}]\n+{message}" #CQ码，这里是at某人的作用
    requests.get(url=f'http://127.0.0.1:5700/send_group_msg?group_id={gid}&message={message}')
    #发送群消息的api，前面的地址保证和配置中的一直

def private_send(uid,msg):
    msg = str(msg)
    sign = {"&": "%26", "+": "%2B", "#": "%23"}
    print(f'Private Send:\tuid={uid}\tMsg={msg}')
    for i in sign:
        msg = msg.replace(i, sign[i])
    js = requests.get(url=f'http://127.0.0.1:5700/send_msg?message_type=private&user_id={uid}&message={msg}')
    js=js.text.encode()
    requests.get(url=f'http://127.0.0.1:5700/send_msg?message_type=private&user_id={uid}&message={js}')

if __name__ == '__main__':
    # 此处的 host和 port对应上面 yml文件的设置
    app.run(host='127.0.0.1', port=5710) #保证和我们在配置里填的一致
