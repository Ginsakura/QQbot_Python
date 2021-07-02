import sys
import random
import re


# 骰子命令解析函数
def dice(cmd: str) -> str:
    s = int()
    res = str()
    cmd = cmd.lower()
    try:
        if "d" in cmd:
            tmp = cmd.replace("r", "").split("d")
            t = 1 if tmp[0] == "" else int(tmp[0])
            m = 100 if tmp[1] == "" else int(tmp[1])
            rea = ""
        elif "r" in cmd:
            t = 1
            m = 100
            rea = f"因为{cmd[1:]}" if cmd[1:] != "" else ""
        # 投掷骰子
        for _ in range(0, t):
            n = random.randint(1, m)
            res = f"{res}+{n}"
            s += n

        # 输出结果
        return f'{f"{rea}您掷得的点数是 R{t}D{m}={res[1:]}"}{f"={s}" if t != 1 else ""}'

    # 有任何错误都一定是命令错了
    except Exception as e:
        return "指令错误！"


if __name__ == '__main__':
    if len(sys.argv) > 1:

        if re.match(r'^((r\d*d\d*)|(r.*)|(\d*d\d*))$', sys.argv[2]):
            print(dice(sys.argv[-1]))
        # 暂未实现功能
        elif re.match(r'^(sc)$', sys.argv[2]):
            pass
        elif re.match(r'^(ra)$', sys.argv[2]):
            pass
        elif re.match(r'^(ep)$', sys.argv[2]):
            pass

        # 无匹配项
        else:
            print("未知命令")
