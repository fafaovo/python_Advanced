import psutil
# 系统监控及进程的管理工具
# 获取CPU的核心数 获取CPU的使用率
print("CPU的核心数:"+str(psutil.cpu_count()))
print("CPU的物理核心数:"+str(psutil.cpu_count(logical=False)))
# 获取CPU的使用率 和 每个核心的使用率
print("CPU的使用率:"+str(psutil.cpu_percent(interval=0.5)))
print("CPU每个核心的使用率:"+str(psutil.cpu_percent(interval=0.5, percpu=True)))
# 获取内存信息 内存的整体信息 内存的使用率
print("内存信息:"+str(psutil.virtual_memory()))
print("内存的使用率:"+str(psutil.virtual_memory().percent))
# 获取硬盘的信息 分区信息 指定目录的磁盘信息 硬盘的使用率
print("硬盘的分区信息:"+str(psutil.disk_partitions()))
print("获取指定目录信息"+str(psutil.disk_usage("c:")))
print("获取指定目录的使用率"+str(psutil.disk_usage("c:").percent))
# 获取网络信息 获取接收的数据包数量 获取发送的数量
print("获取网络信息"+str(psutil.net_io_counters().bytes_recv))
print("获取网络信息"+str(psutil.net_io_counters().bytes_sent))
# 获取开机时间
print("获取开机时间:"+str(psutil.boot_time()))