"""
协程Coroutine，又称微线程
协程就是你可以暂停执行的函数 像生成器一样 协程就是个特殊的生成器

协程，只需要使用一个线程，在一个线程中规定某个执行顺序
协程就是不需要开辟新的线程实现多任务

把原来等待的时间拿出来去执行另外一个任务。反复横跳进一步提升了利用率

当程序中存在大量不需要CPU操作时,适用协程
"""
import time


def work1():
    while True:
        print("正在执行work1")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("正在执行work2")
        yield
        time.sleep(0.5)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)
    # 交替执行 顺序一定不会乱
