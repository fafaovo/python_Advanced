import time
import threading


def sing(a, b, c):
    print(f"{a}{b}{c}")
    for i in range(5):
        print("唱歌", end="")
        time.sleep(0.5)


def dance():
    for i in range(5):
        time.sleep(0.5)
        print("跳舞", end="")


if __name__ == '__main__':
    # 在线程中传递参数有三种方法
    # 1.使用元组 threading.Thread(target=xxx, args=(参数1,参数2))
    dan = threading.Thread(target=dance)
    # sin = threading.Thread(target=sing, args=(10, 100, 1000))
    # 2.使用字典传递
    # threading.Thread(target=xxx, kwargs={参数名:参数值,...})
    sin = threading.Thread(target=sing, kwargs={'a': 100, 'b': 100, 'c': 100})
    # 3.使用混合使用元组和字典
    # threading.Thread(target=sing, args=(参数, ),)kwargs={参数名:参数值,...}
    dan.start()
    sin.start()
    # 线程的执行顺序是无序的,是由CPU调度执行,CPU会按照自己的调度算法去调度执行
    


