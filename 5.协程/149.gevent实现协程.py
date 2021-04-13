from gevent import monkey
monkey.patch_all()
"""
    打补丁
    1.导入模块 monkey 模块 from gevent import monkey
    2.破解所有 monkey.patch_all()
"""
import gevent
import time

"""
gevent可以自动检测那些代码是耗时操作,当进行时,立即切换
"""


def work1():
    while True:
        print(f"正在执行work1{gevent.getcurrent()}")
        """默认情况下这个time.sleep不能被识别为耗时操作"""
        # time.sleep(0.5)
        gevent.sleep(0.5)


def work2():
    while True:
        print(f"正在执行work2{gevent.getcurrent()}")
        """
        当然也可以把这个变成耗时操作
        给 gevent 打补丁(目的：让gevent识别time.sleep)
        打补丁:在不修改程序源代码给程序增加新功能
        """
        time.sleep(0.5)


if __name__ == '__main__':
    # 指定任务 gevent.spawn(函数名,参数1,参数2,...)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)
    # 程序有个主线程,虽然指派任务了，但是主线程结束了
    # 所以需要让主线程等待协程
    g1.join()
    g2.join()
