import socket
# 创建嵌套字，已ipv4的方式 已UDP的传输方式
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据 要发送数据的二进制格式，对方的ip地址和端口号(此处需要元组)
udp_socket.sendto("你好".encode(), ("127.0.0.1", 8080))
# 解码数据， 得到字符串 从套接中接收1024个字节，会发送堵塞
# 注意,如果前面的ip地址填写的127.0.0.1 就会出现问题
recv_date = udp_socket.recvfrom(1024)
# 输出接收到的内容
# 接收到的数据会是一个元组，第一个接收到数据的二进制，
# 发送方的ip地址和端口号 decode("GBK")将二进制转成字符串,并且以GBK的方式解码
print(recv_date[0].decode("GBK"))


# 结束
udp_socket.close()

