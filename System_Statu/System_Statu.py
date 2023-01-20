##Version 1.0.2##修改输出结构标识##
import psutil
import sys
import datetime

def main():
    CPU = psutil.cpu_percent(interval=0.5)
    RAM_phi = psutil.virtual_memory()
    #RAM_Swap = psutil.swap_memory()
    ROM = psutil.disk_usage("C:/")
    #Network = psutil.net_if_stats()
    bootTime = datetime.datetime.utcfromtimestamp(psutil.boot_time())
    #print(bootTime)
    deltaTime = datetime.datetime.now() - bootTime
    print(f'''
╔系统信息:
╠═CPU利用率:{CPU}%
╠╦物理内存:
║╠═总内存:{round(RAM_phi[0]/1024/1024/1024,3)}GB
║╠═已用内存:{round(RAM_phi[3]/1024/1024/1024,3)}GB
║╠═可用内存:{round(RAM_phi[4]/1024/1024/1024,3)}GB
║╚═内存利用率:{round(RAM_phi[3]/RAM_phi[0],5)*100}%
╠╦硬盘利用率:
║╠═总空间:{round(ROM[0]/1024/1024/1024,3)}GB
║╠═已用空间:{round(ROM[1]/1024/1024/1024,3)}GB
║╠═可用空间:{round(ROM[2]/1024/1024/1024,3)}GB
║╚═磁盘使用率:{round(ROM[1]/ROM[0],5)*100}%
╚╦开机信息:
  ╠═开机时间:{bootTime}
  ╚═开机时长:{deltaTime}''')

'''CPU
psutil.cpu_count() # cpu数量
psutil.cpu_count(logical=True) # 逻辑CPU的数量
获取CPU每个CPU当前利用率:
psutil.cpu_percent(interval=1) # 1 秒后线束总的利用率结果
psutil.cpu_percent(interval=0, percpu=True) # 立马显示每个CPU结果
获取CPU的频率，包括最低、高频率，以及当前频率:
psutil.cpu_freq(percpu=True) #获取每个CPU的频率

内存
获取物理内存的利用情况:
psutil.virtual_memory() # 有点类似 free 命令
获取 Swap 交换内存:
psutil.swap_memory() # 有点类似 free 命令

硬盘
获取硬盘分区，返回的是分区格式类型，挂载点:
psutil.disk_partitions(all=False) #类似lsblk命令
获取硬盘利用率，返回的是使用多少、还剩多少，以及使用率:
psutil.disk_usage("C:/") # 查看C盘

网络
获取当前网络的IO情况，返回IO的字节、包的数量:
psutil.net_io_counters()
获取当前连接数，对于这个需要root用户权限，因此在运行python的时候加上sudo:
psutil.net_connections() # 返回连接详细信息
获取网口信息和状态:
psutil.net_if_addrs() # 获取网络接口信息
psutil.net_if_stats() # 获取网络接口状态

进程
获取所有进程PID:
psutil.pids() # 所有进程ID
可以通过指定进程PID来获取，进程名称、进程路径、状态以及结束进程等。
pid = psutil.Process(8888) # 获取进程pid为8888的进程
pid.name() # 进程名称
pid.status() # 进程状态
pid.terminate() # 终止进程
'''

if __name__ == '__main__':
    #command = sys.argv[-1]
    #purview = sys.argv[-1]
    purview = '2602961063'
    if purview == '2602961063' :
        main()