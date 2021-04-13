from greenlet import greenlet
import time

"""
提供一个自行调度的微线程 即协程
步骤
1.创建任务work1 work2
2.创造greeniet 对象
3.手动 switch 任务

greeniet对象创建完后只需要指定谁先执行 剩下的让他自行调度
"""


def work1():
    while True:
        print("正在执行work1......")
        time.sleep(0.5)
        g2.switch()


def work2():
    while True:
        print("正在执行work2...")
        time.sleep(0.5)
        g1.switch()


if __name__ == '__main__':
    # 2.创造greeniet 对象
    g1 = greenlet(work1)
    g2 = greenlet(work2)
    # 3.手动 switch 任务 默认开始执行的
    g1.switch()
