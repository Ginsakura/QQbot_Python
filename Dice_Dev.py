import sys, random, re

def dice(cmd: str) -> str:
    try: 
        tmp = cmd.replace("r", "").split("d")
        t = int(tmp[0]); m = int(tmp[1])
        s = int(); res = str()
        for _ in range(0, t):
            n = random.randint(1,m)
            res = f"{res}+{n}"
            s += n
        return f"您掷得的点数是 R{t}D{m}={res[1:]}={s}。"
    except:
        return "指令错误！" 

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.match(r'^(r{0,1}\d*d\d*)$', sys.argv[2]):
            print(dice(sys.argv[-1]))
        elif re.match(r'^(sc)$', sys.argv[2]):
            pass
        elif re.match(r'^(ra)$', sys.argv[2]):
            pass
        elif re.match(r'^(ep)$', sys.argv[2]):
            pass