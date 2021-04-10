"""
进程也是实现多任务的
线程是CPU调度的基础单位
经常是资源分配的最小单位,也是线程的容器

程序指的是一个软件，进程就是打开软件后让操作系统动态分配各种资源

进程的参数传递和线程一模一样

进程在进行时候会拷贝一份全局变量的值
所以进程间不能实现全局变量的共享

"""
import multiprocessing
import time
import os

# 如何杀死一个进程
# kill -9 进程编号 强制杀死
# kill -15 等执行完后干掉



def work1():
    for i in range(10):
        # 获取当前进程的编号
        # print(f"work1():{multiprocessing.current_process().pid}")
        # 当然也可以用os模块获取
        print(f"进程编号:{os.getpid()}")
        # 当然，也可以获取父编号
        print(f"父进程编号:{os.getppid()}")
        time.sleep(0.5)


if __name__ == '__main__':
    # 获取主进程
    print(multiprocessing.current_process().pid)
    """
    程序启动有个默认的主进程，在主进程里面才有一个主线程
    """
    work = multiprocessing.Process(target=work1, name="p1")

    # 设置进程守护是用等号赋值
    work.daemon = True
    # 直接杀死子线程 work.terminate()
    work.start()



    """
    is_alive()判断子进程是否活着 multiprocessing.Process可以用name给进程起名字
     
    """