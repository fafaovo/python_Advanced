"""
进程池 有很多个进程组成

1.创建一个函数用于模拟文件拷贝
2.创建一个进程池长度为3（表示进程池最多可以创建3个进程）
3.先用进程池同步方式拷贝文件
4.再用进程池异步的工作方式拷贝文件
"""
import multiprocessing
import time


# 1.创建一个函数用于模拟文件拷贝
def copy_work():
    print(f"正在拷贝文件....{multiprocessing.current_process()}")
    time.sleep(0.5)


# 2.创建一个进程池长度为3（表示进程池最多可以创建3个进程）
if __name__ == '__main__':
    pool = multiprocessing.Pool(3)  # 最大允许2个 记住是大写的P
    for i in range(10):
        # pool.apply(函数名,传递的参数元组) 让进程已同步状态进行
        # pool.apply_async(copy_work) 让进城已异步状态进行
        # 但是需要两点 1.需要close() 表示不再结束后退出 2.主进程不再等待进程池结束后退出
        pool.apply_async(copy_work)
    pool.close()  # 不再接受新的任务，但是不代表关闭
    pool.join()  # 让主进程等待进程池执行后退出

# 3.先用进程池同步方式拷贝文件
# pool.apply(函数名,传递的参数元组) 让进程已同步状态进行
# 4.再用进程池异步的工作方式拷贝文件
# pool.apply_async(copy_work)
# pool.close()  # 不再接受新的任务，但是不代表关闭
# pool.join()  # 让主进程等待进程池执行后退出
