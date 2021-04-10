import threading
import time

# 并发:任务数多于cpu核数
# 并行:任务数少于cpu核数
# 自定义线程类 [多线程下载, python爬虫]
"""
1.让自定义类继承 threading.Thread 类
2.重写父类 （threading.Thread）run方法
3.通过创建子类对象,让子类对象.start() 启动子线程
"""


# 让自定义类继承 threading.Thread 类
class MyThread(threading.Thread):
    def __init__(self,num):
        super().__init__()
        """先调用父类的"""
        self.num = num

    # 重写父类 （threading.Thread）run方法
    def run(self):
        """run方法是执行到这个子线程时，自动调用的方法"""
        for i in range(5):
            print(f"正在执行子线程的run方法:{i}和{self.num}")
            time.sleep(0.5)
    pass


if __name__ == '__main__':
    myThread = MyThread(10)
    myThread.start()

