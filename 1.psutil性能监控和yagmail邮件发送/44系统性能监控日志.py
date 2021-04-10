import psutil
import datetime

CPU = psutil.cpu_count(logical=False)
momory = (psutil.virtual_memory().total)/1024/1024/1024
disk = psutil.disk_usage("/").total/1024/1024/1024
net = psutil.net_io_counters()
# 获取系统当前时间
time = str(datetime.datetime.now().strftime("%F %T"))

CPU_per = psutil.cpu_percent(interval=0.5)
momory_per = psutil.virtual_memory().percent
disk_per = psutil.disk_usage("/").percent


log_str = "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n"
log_str += "|      监控时间        |      CPU使用率     |      内存使用率      |     磁盘使用率      |         网络收发量       |\n"
log_str += "|                     |    (总共%d核CPU)   |    (总计%.1fG内存)    |   (总共%.1fG硬盘)   |                        |\n" %(CPU, momory, disk, )
log_str += "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n"
log_str += "| %s |      %.2f%%       |       %.2f%%       |       %.2f%%      | 收:%d/发:%d |\n" %(time, CPU_per, momory_per, disk_per, net.bytes_recv, net.bytes_sent)
log_str += "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n\n"
print(log_str)
"""
f = open("storage/xtxn.txt", "a")
f.write(log_str)
f.close()
"""
