"""
TCP 面向连接、可靠的、基于字节流的传输控制协议
TCP的特点
面向连接
可靠传输 :
    1.应答机制
    2.超时重传
    3.错误校验
    4.流量管控
客户端
socket对象->connet->send(recv)->close
服务端
socket对象->bind->listen->accept-send(recv)->close
"""
import socket
# 客户端
# 创建套接字(ipv4,tcp传输方式)
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接 ip地址和端口号
tcp_client.connect(("127.0.0.1", 8080))
# 发送数据
tcp_client.send("在吗？".encode())
# 接收数据,此时会直接受到一个二进制内容
recv_data = tcp_client.recv(1024)
print("收到数据"+recv_data.decode())

tcp_client.close()
# 关闭连接
