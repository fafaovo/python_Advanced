import socket

# 编码.encode("字符集") 将字符串转换成二进制
# 字符集填写GBK即为中文 UTF-8为万国码 python默认utf-8
# 编码.decode("字符集", 如果解码失败执行的东西) 将二进制转成字符串
aa = ["1111", ("127.0.0.1", 8080)]
aa[0].encode(encoding="UTF-8", errors="ignore")


# ignore 忽略错误 strict 默认严格模式(会报错)

# 我们注意到发送后 接收会收到端口号 每次运行都会收到不同的端口号
# 所以需要绑定发送端端口号
# bind(元组) 元组第一个元素是字符串类型的IP地址，
# 第二个元素是整数的端口号
def fasong():
    # 创建嵌套字
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口号 这个是绑定自己的IP地址和端口号 ip地址可不填
    udp.bind(("", 8888))
    # 发送数据 这个是绑定接收方的ip地址和端口号
    udp.sendto("hello world".encode(), ("127.0.0.1", 8080))
    udp.close()


# 接收端绑定接收绑定端口
# 创建嵌套字
udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口号
udp1.bind(("", 8080))

# 发送数据
fasong()

# 接收数据并且拆包
date, ip = udp1.recvfrom(1024)
# 打印数据
print(date.decode())
udp1.close()
