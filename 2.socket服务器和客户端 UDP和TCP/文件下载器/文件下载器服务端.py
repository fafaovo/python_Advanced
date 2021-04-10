"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，设置套接字将主动改为被动
5.接受客户端连接
6.接受客户端发送的文件名
7.根据文件名读取文件内容
8.把读取的内容发送给客户端(循环)
9.关闭和当前客户端的链接
10.关闭服务器
"""
# 1.导入模块
import socket
import os
# 2.创建套接字
os.chdir("服务端文件夹")
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
tcp_server.bind(("127.0.0.1", 8080))
# 4.设置监听，设置套接字将主动改为被动
tcp_server.listen(128)
# 5.接受客户端连接
while True:
    try:
        new_socket, ip = tcp_server.accept()
        print(f"欢迎新客户端:{ip}")
        # 6.接受客户端发送的文件名
        recv_data = new_socket.recv(1024)
        file_name = recv_data.decode()
        print(file_name)
        # 7.根据文件名读取文件内容
        with open(file_name, "rb") as file:
            while True:
                file_data = file.read(1024)
                if len(file_data) == 0:
                    break
                new_socket.send(file_data)
        # 8.把读取的内容发送给客户端(循环)
        # 9.关闭和当前客户端的链接
        # 10.关闭服务器
    except Exception as e:
        print(f"文件{file_name}下载失败\n,错误信息{e}")
    else:
        print(f"文件{file_name}下载成功")
        new_socket.close()
    # 一般服务器是断电的时候才会关闭
    # 所以说下面这句话其实不需要
# tcp_server.close()
