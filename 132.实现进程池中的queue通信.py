import time
import multiprocessing


def queue_put(queue):
    for i in range(10):
        if queue.full():
            print("进程池已满!")
            break
        queue.put(i)
        print(f"已写入:{i}")
        time.sleep(0.5)
        pass


def queue_get(queue):
    while True:
        if queue.qsize() == 0:
            print("进程池已空！")
            break
        print(f"正在读取{queue.get()}")
        pass


if __name__ == '__main__':
    """进程池中的队列需要加上Manager()"""
    queue = multiprocessing.Manager().Queue(5)
    """创建进程池"""
    pool = multiprocessing.Pool(2)

    # 同步方式
    # pool.apply(queue_put, (queue, ))
    # pool.apply(queue_get, (queue, ))
    # 异步的方式 这个方法会返回一个applyresult改对象有一个 wait() 该方法类似join()
    result = pool.apply_async(queue_put, (queue, ))
    result.wait()  # 变回同步了
    pool.apply_async(queue_get, (queue, ))


    pool.close()
    pool.join()
