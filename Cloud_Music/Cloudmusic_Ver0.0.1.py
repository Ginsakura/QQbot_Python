##Version 0.0.1##开始之前##测试##

import re
import sys

def main(text,reg1,reg2):
    text2 = re.sub(r'\s','',text)
    m = re.match(reg1,text2)
    if m.group(2) == None :
        m = re.match(reg2,text)
        print(m.group(2))
    else:
        print(m.group(3))

if __name__ == '__main__':
    text = sys.argv[1]
    #text = '网易云点歌 I 45466'
    reg = r'网易云(点歌)?(ID|id)?(\d*)?'
    reg2 = r'网易云(点歌)?\s?(.*)'
    main(text,reg,reg2)