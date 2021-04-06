"""
通过队列将数据放进去,然后把取出来实现进程共享数据

进程传输需要通过Queue实现数据传输
头取值，尾放值
"""
import multiprocessing
# multiprocessing.Queue(队列长度)
# 当放入的值超过队列长度时候，会进入阻塞状态，等待值被取走
# put_nowait()如果满了会直接报错
queue = multiprocessing.Queue(5)
queue.put("这是一个值")
queue.put([1, 2, 3, 4, 5])

"""get一次取一次"""
print(queue.get())
print(queue.get())