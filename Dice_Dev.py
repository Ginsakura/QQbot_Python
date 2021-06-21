import sys
import random
import re


# 骰子命令解析函数
def dice(cmd: str) -> str:
    try:
        # 处理标准的骰子命令
        tmp = cmd.replace("r", "").split("d")
        t = int(tmp[0])
        m = int(tmp[1])
        s = int()
        res = str()

        # 投掷骰子
        for _ in range(0, t):
            n = random.randint(1, m)
            res = f"{res}+{n}"
            s += n

        # 输出结果
        return f"您掷得的点数是 R{t}D{m}={res[1:]}={s}。"

    # 有任何错误都一定是命令错了
    except:
        return "指令错误！"


if __name__ == '__main__':
    if len(sys.argv) > 1:

        # 在第三个参数中匹配形如 r (一串数字) d (一串数字) 或者单独 r 的字符串
        if re.match(r'^(r\d*d\d*)|(r)$', sys.argv[2]):
            print(dice(sys.argv[-1]))  # 最后一个参数必定为标准骰子命令

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
