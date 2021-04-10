# 发送UDP广播
import socket


def fasong():
    # 1.创建套接字
    UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.设置广播权限(套接字默认不允许发送广播，需要开启权限)
    # setsockopt(套接字,属性,属性值)
    UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # socket.SOL_SOCKET ->当前套接字
    # socket.SO_BROADCAST ->广播
    # 3.发送数据
    UDP.sendto("python测试".encode(), ("255.255.255.255", 8080))
    # 255.255.255.255 广播地址 xxx.xxx.xxx.255 这个网络号下所有主机
    # 4.关闭套接字
    UDP.close()


UDP1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP1.bind(("", 8080))

fasong()

data, ip = UDP1.recvfrom(1024)
print(data.decode())
UDP1.close()

