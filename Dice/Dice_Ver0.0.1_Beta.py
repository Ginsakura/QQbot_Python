##Version 0.0.1 Beta##
##注意：这是β分支##

###模块导入区域开始####
import sys
import random
import sqlite3
import datetime
import configparser
##模块导入区域结束##

####全局变量区域开始####
global User,Error,Command
##全局变量区域结束##

####功能实现区域开始####
def Separation_Command(Number,Cmd):##传递分割模块##
    Test_Output(f'Number={Number}\nCommand={Cmd}\nUser={User}')
    if Cmd[0][0:2].lower() == "ra" :
        Command = 'ra'
        surplus = Cmd[0][2:]
        x,lenth=1,len(Cmd)+1
        for x in range(1,lenth) :
        	surplus = f'{surplus} {Cmd[x]}'
        Test_Output(f'surplus=ra {surplus}')
    elif Cmd[0][0].lower() == 'r' :
        Command = 'r'
        surplus = Cmd[0][1:] + Cmd[1:]
        Test_Output(f'surplus=r {surplus}')
    else :
        Error_Type("argu err")
        #print(Command[0][0].lower())
    #Separation_Dice_Value()

def Separation_Dice_Value():##数值分离模块##
    pass

def Error_Type(Error_Text):##错误返回模块##
    print(Error_Text)

def Test_Output(Text):##测试输出模块##
    print(Text)
##功能实现区域结束##
if __name__ == '__main__' :##参数接收模块##
    num = len(sys.argv) - 2
    if num >= 1 :
        User = sys.argv[1]
        Separation_Command(num,sys.argv[2:])
    else :
        Error_Type('Command Error')