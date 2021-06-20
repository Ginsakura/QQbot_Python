##Version 0.1.0##部分功能实现##稳定性极低##

import sys
import random
import re

def main_1(func,argu):
#接收参数，分割出功能参数
    if func == "fun":
        print(f"fun={argu}")
    elif func == "arg":
        print(f"arg={argu}")
    else:
        print("错误输入:main_1")
def main_2(func,argu):
#接收骰子参数，分割出骰子数量、面数,传递功能块参数
    num = 0
    #初始化循环变量
    #r(argu[0],argu[-1])
    for num in range(0, len(argu)+1, 1):
    #遍历骰子参数，找出特征点d/D位置
        if argu[num] == "d" :
        #找到特征点d的位置
            main_3(func,argu[0:num],argu[num+1:])
            #将骰子数量、面数两个参数传递到main_3模块进行参数正确性判断
        elif argu[num] == "D" :
        #找到特征点D的位置
            main_3(func,argu[0:num],argu[num+1:])
            #将骰子数量、面数两个参数传递到main_3模块进行参数正确性判断
        else :
        #？这是啥？
            pass
            #？？？
    else:
    #找不到特征点d/D
        print("错误骰子参数")
def main_3(func,number,randoms):
#执行参数正确性判断
    if number == '':
    #判断骰子数量是否为空
        if randoms == '':
        #骰子数量为空的基础上判断骰子面数是否为空
            #两个参数皆是空
            error("None_Randoms")
        elif randoms == 0:
        #骰子数量为空，且面数为0
            error("Zero_Randoms")
        else:
        #骰子数量为空，但面数不为空
            number = 1
            #骰子数量默认为1
            main_4(func,number,randoms)
            #将功能块、骰子数量、面数三个参数传递到main_4功能块
    elif randoms == '':
    #判断面数是否为空
        error("None_Randoms")
    elif int(number) == 0:
    #判断骰子数量是否为0
        error("Zero_Number")
    elif int(randoms) <= 0:
    #判断骰子面数是否为0
        error("Zero_Randoms")
    else:
    #均无错误
        main_4(func,number,randoms)
        #均无错误情况下，传递功能块、骰子数量、面数三个参数到main_4功能块
def main_4(func,number,randoms):
#从main_3接收功能块、骰子数量、面数三个参数
    if func == "r":
    #如果功能块参数为“r”
        r(number,randoms)
        #将骰子数量、面数传递到r功能块执行
    else:
    #如果均不符合功能块，则返回未定义
        print("Undef Function")
def r(number,randoms):
#投骰子
    ran,summ,num = 0,0,0
    resule = f"\n投掷:{number}d{randoms}="
    if number == "1":
        ran = random.randint(1,int(randoms))
        print(f"{resule[:-1]}={ran}")
    else :
        for num in range(0,int(number),1):
            ran = random.randint(1,int(randoms))
            summ = summ + ran
            resule = f"{resule}{ran}+"
        print(f"{resule[:-1]}={summ}")
def ra():
#技能成功判断
    if None:
        pass
def st():
#配置人物卡
    if None:
        pass
def sc():
#SanCheck
    if None:
        pass
def error(typ):
#错误处理与反馈
    if typ == "Zero_Number":
        print("零数错误")
    elif typ == "Zero_Randoms":
        print("零面错误")
    elif typ == "None_Number":
        print("无数错误")
    elif typ == "None_Randoms":
        print("无面错误")
if __name__ == '__main__':
#主函数
#接收功能块参数（sys.argv[1])、骰子参数（sys.argv[-1]）
    user = sys.argv[1]
    #获取发送者QQ号
    if len(sys.argv) == 4:
    #判断传递参数数量
        main_2(sys.argv[1],sys.argv[-1])
        #传递功能块、骰子参数到main_2模块进行参数分割
    else:
    #三个参数则传递到main_1模块进行功能参数分离
        main_1(sys.argv[1],sys.argv[-1])
        #这是干嘛的来着