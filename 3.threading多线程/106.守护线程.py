import threading
import time

"""
守护线程:主线程强行结束时,也要结束子线程
"""


def work1():
    for i in range(10):
        print(f'work1:{i}')
        time.sleep(0.5)


if __name__ == '__main__':
    work = threading.Thread(target=work1)
    # 这句话就表示子线程守护主线程，主线程结束后子线程也结束
    work.setDaemon(True)

    work.start()

    time.sleep(2)
    print("game over!")
    # 让程序退出,主线程挂了
    exit()
