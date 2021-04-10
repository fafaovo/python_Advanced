"""
思路：
1.准备两个进程
2.准备一个队列 一个向队列中写入数据然后把队列传递到另外一个进程
3.另外一个进程读取数据
"""
import multiprocessing
import time


def write_queue(queue):
    for i in range(10):
        if queue.full():
            """判断队列是否为满"""
            print("队列已满")
            break
        queue.put(i)
        print(f"已写入成功{i}")
        time.sleep(0.5)


def read_queue(queue):
    while True:
        """判断是否为空"""
        if queue.qsize() == 0:
            print("队列已空")
            break
        value = queue.get()
        print(f"已读取:{value}")


if __name__ == '__main__':
    queue = multiprocessing.Queue(5)
    work1 = multiprocessing.Process(target=write_queue, args=(queue,))
    work2 = multiprocessing.Process(target=read_queue, args=(queue,))

    work1.start()
    # 所以先让写完成然后再进行读
    work1.join()

    work2.start()
