"""
1.导入模块
2.创建套接字
3.建立连接
4.拼接请求协议
5.发送请求报文
6.接收服务器返回的内容
7.保存内容
8.断开连接
"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
tcp_client_socket.connect(("localhost", 8080))
# 4.拼接请求协议
# 4.1 请求行
request_line = "GET / HTTP/1.1\r\n"
# 4.2 请求头
request_header = "Host:localhost\r\n"
# 4.3 请求空行
request_blank = "\r\n"
# 整体连接[注意连接头和空行有双重\r\n]
request_data = request_line + request_header + request_blank
# 5.发送请求报文
tcp_client_socket.send(request_data.encode())
# 6.接收服务器返回的内容
recv_data = tcp_client_socket.recv(409600)
recv_text = recv_data.decode('GBK')
# 7.保存内容
"""
保存内容需要先找到位置也就是\r\n\r\n的空行
，空行后面的即内容
"""
loc = recv_text.find("\r\n\r\n")
html_data = recv_text[loc+4:]
print(html_data)
with open('cpp.html', 'w') as file:
    file.write(html_data)
# 8.断开连接
tcp_client_socket.close()

