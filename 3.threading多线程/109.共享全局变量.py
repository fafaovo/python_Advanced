import time
import threading
"""
多线程可以共享全局变量，当多个线程修改同一个资源的时候会导致资源竞争
同步:在多任务中,必须有一个先执行,另外一个才能继续执行
异步:在多任务中,可以同时执行
线程锁:每次访问资源后给一个线程增加一个锁，等访问完后解锁
互斥锁:线程锁的在代码中的方式，分为锁定和非锁定
互斥锁语法:
对象 = threading.Lock() 创建
对象.acquire() 锁定
对象.release() 解锁
使用锁时尽可能锁的最小.使用加锁都是加在紧缺资源上
"""
# 为了防止资源竞争
# 解决方式 1.设置优先级,先让work1优先执行，但是就变成单线程了
# work1.join()
# 解决方式 2.使用互斥锁,每次访问资源后给一个线程增加一个锁，等访问完后解锁
g_num1 = 0


def work1():
    global g_num1
    global lock1

    for i in range(1000000):
        # 上锁
        lock1.acquire()
        g_num1 += 1
        # 解锁
        lock1.release()
    print(f"work1:{g_num1}")


def work2():
    global g_num1
    global lock1

    for i in range(1000000):
        # 一二都要加锁，而且要加同一个锁
        lock1.acquire()
        g_num1 += 1
        lock1.release()

    print(f"work2:{g_num1}")


if __name__ == '__main__':
    # 创建互斥锁
    lock1 = threading.Lock()
    work1 = threading.Thread(target=work1)
    work2 = threading.Thread(target=work2)

    work1.start()
    work2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    # 假设线程不等于1，循环执行休眠
    # 即如果子线程全部执行完后才会跳出休眠
    print(f"main:{g_num1}")


