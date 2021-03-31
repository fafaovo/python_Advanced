import time
import threading

"""python代码默认是单任务"""
"""
线程可以理解为程序执行的分支,线程是系统独立调度和分配的基本单元
程序启动就会创建一个主线程,默认情况下主线程会等待子线程执行完才会结束
核心方法
    threading.Thread(target=函数名) 创建子线程对象 函数名不要括号
    线程对象.start()启动子线程
    threading.enumerate() 获取线程，len()包起来即可得到线程数量
    threading.current_thread() 获取线程对象

"""


def sing():
    for i in range(5):
        print("唱歌", end="")
        time.sleep(0.5)


def dance():
    for i in range(5):
        time.sleep(0.5)
        print("跳舞", end="")


def hs():
    for i in range(5):
        time.sleep(0.5)
        print("喝水", end="")


if __name__ == '__main__':
    print(threading.current_thread())
    dan = threading.Thread(target=dance)
    sin = threading.Thread(target=sing)

    dan.start()
    sin.start()
    hs()

    print(f"\n{len(threading.enumerate())}")

