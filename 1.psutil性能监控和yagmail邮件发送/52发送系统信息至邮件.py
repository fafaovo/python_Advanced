import psutil
import datetime
import yagmail



def win_monitor(time):
    """定义函数实现硬件信息的获取"""
    CPU_per = psutil.cpu_percent(interval=time)
    CPU = psutil.cpu_count(logical=False)
    momory = psutil.virtual_memory().total / 1024 / 1024 / 1024
    disk = psutil.disk_usage("/").total / 1024 / 1024 / 1024
    net = psutil.net_io_counters()
    # 获取系统当前时间
    time = str(datetime.datetime.now().strftime("%F %T"))
    momory_per = psutil.virtual_memory().percent
    disk_per = psutil.disk_usage("/").percent

    log_str = "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n"
    log_str += "|      监控时间        |      CPU使用率     |      内存使用率      |     磁盘使用率      |         网络收发量       |\n"
    log_str += "|                     |     (总共%d核CPU)   |    (总计%.1fG内存)    |   (总共%.1fG硬盘)   |                        |\n" % (
    CPU, momory, disk,)
    log_str += "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n"
    log_str += "| %s |      %.2f%%       |       %.2f%%       |       %.2f%%      | 收:%d/发:%d |\n" % (
    time, CPU_per, momory_per, disk_per, net.bytes_recv, net.bytes_sent)
    log_str += "|---------------------|-------------------|--------------------|-------------------|-------------------------|\n\n"
    print(log_str)
    my_maill = yagmail.SMTP(user="1016828446@qq.com", password="oufrkrrkxfqcbbjb", host="smtp.qq.com")
    my_maill.send("1206180803@qq.com", "我的系统信息[测试使用]", log_str)

def main():
    """程序入口"""
    win_monitor(0.5)



if __name__ == '__main__':
    """
    __name__:如果这个模块被其他文件导入了此时__name__他指的是就是这个文件名
    如果没有被导入,直接运行的话__name__会得到__main__
    """
    main()