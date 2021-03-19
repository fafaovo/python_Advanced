"""
1.导入模块
2.创建套接字
3.建立连接
4.接收用户输入的文件名
5.发送文件名到服务端
6.创建文件并且准备保存
7.接收服务端发送的数据,保存到本地
8.关闭套接字
"""
# 1.导入模块
import socket
import os
os.chdir("客户端文件夹")
# 2.创建套接字
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
tcp_client.connect(("127.0.0.1", 8080))
# 4.接收用户输入的文件名
fileName = input("请输入要下载的文件名")
# 5.发送文件名到服务端
tcp_client.send(fileName.encode())
# 6.创建文件并且准备保存
with open(fileName, "wb") as file:
    """with:不需要关闭文件的操作"""
    """打开文件变量存到file里面，然后循环将读取到的文件放到新文件夹里面"""
    while True:
        fileData = tcp_client.recv(1024)
        if len(fileData) == 0:
            break
        file.write(fileData)
# 7.接收服务端发送的数据,保存到本地
# 8.关闭套接字
tcp_client.close()
