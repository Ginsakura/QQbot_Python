##AzurLane Script##Version 0.0.1##结构框架搭建##

import os
import re
import sys
import sqlite3
import datetime
import requests
import subprocess

def main(cmd, argu):
	if cmd == '虚拟机列表':
		subprocess.call('powershell memuc listvms', shell=True)
	elif cmd == "启动虚拟机":
		if argu == None:
			print("Place input VMS index number:")
			argu = sys.stdin.readline()
		subprocess.call(f'powershell memuc start -i {argu[0]}', shell=True)
	elif cmd == "启动AzurLane":
		subprocess.call(f'powershell memuc -i 0 adb shell am start com.bilibili.azurlane/com.manjuu.azurlane.MainActivity', shell=True)
	elif cmd == "屏幕快照":
		subprocess.call(f'powershell memuc -i 0 adb shell screencap /storage/emulated/0/Pictures/screen.png', shell=True)
		subprocess.call(f'powershell memuc -i 0 adb pull /storage/emulated/0/Pictures/screen.png T:/temp/screen.png', shell=True)
	elif cmd == "":
	pass

#subprocess.call(f'powershell memuc -i 0 adb shell', shell=True)

if __name__ == '__main__':
	command = sys.argv[1]
	if len(sys.argv) > 2:
		argument = sys.argv[2:]
	else:
		argument = None
	main(command, argument)