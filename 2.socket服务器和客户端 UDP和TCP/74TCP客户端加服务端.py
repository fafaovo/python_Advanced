"""
TCP 面向连接、可靠的、基于字节流的传输控制协议
TCP的特点
面向连接
可靠传输 :
    1.应答机制
    2.超时重传
    3.错误校验
    4.流量管控
"""
import socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务端的ip地址和端口
udp_server.bind(("", 8080))
# 设置服务端为被动接收
udp_server.listen(128)

# 客户端发送连接
udp_client.connect(("127.0.0.1", 8080))
# 服务器链接[新的套接字和ip地址]
new_udp, ip_udp = udp_server.accept()

# 客户端发送东西
udp_client.send("这是客户端发送的信息".encode())
# 服务端接收东西
data = new_udp.recv(1024)
print(data.decode())

# 服务端发送东西
new_udp.send("这是服务端发送的信息".encode())
# 客户端接收东西
text = udp_client.recv(1024)
print(text.decode())

# 关闭程序
new_udp.close()
udp_client.close()
udp_server.close()