import multiprocessing
import time
queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(2)
queue.put(3)
# 此处
time.sleep(0.0001)

isEMPTY = queue.empty()
print(f"isEmtpy = {isEMPTY}")
# 此处得到的结果很随机
# 可以这么理解,底层会让两个语句一块执行，放值和取值是两个进程完成的

# 所以给个time.sleep可以避免这种情况
# 或者使用qsize来判断是否为空
