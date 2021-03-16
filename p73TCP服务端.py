import socket
# 服务端 socket对象->bind->listen->accept-send(recv)->close
# 1.创建套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定端口和ip
tcp_server.bind(("", 8080))
# 3.开启监听(设置套接字为被动模式)
# listen 设置这个套接字为被动监听模式,不能在主动发送数据
# 128允许接收最大的连接数,在window 128 有效,但是在linux此数字无效
tcp_server.listen(128)
# 4.等待客户端连接 accept 开始接收客户端连接 程序会阻塞等待连接
# recv_data 会得到一个新的套接字socket[对象]和客户端的ip地址和端口号[元组]
# 每来一个客户端就会产生一个新的套接字为这个客户端服务，
# 因为本身的套接字已经被动接收了
recv_data = tcp_server.accept()
new_client_socket, client_ip_port = recv_data
# 5.收发数据
# 接收数据
data = new_client_socket.recv(1024)
print(data.decode())
# 发送数据
new_client_socket.send("我在啊".encode())
# 6.关闭连接
new_client_socket.close()
tcp_server.close()