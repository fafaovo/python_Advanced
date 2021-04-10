import socket
import os
import threading


def fasong(new_socket, ip_data):
    request_data = new_socket.recv(1024)
    if not request_data:
        print(f"{ip_data}客户端已下线!")
        new_socket.close()
        return
    # 处理接收到的消息
    #       （1）先查找第一个\r\n出现的位置，并且进行截取
    reText = request_data.decode()
    ioc = reText.find("\r\n")
    #       （2）请求行进行按照空格拆分得到列表
    request_line = reText[:ioc]
    requset_list = request_line.split(" ")
    file_path = requset_list[1]
    # 此处判断是否是直接访问，如果是直接访问则链接到index
    if file_path == "/":
        file_path = "/index.html"
    print(file_path)

    # 发送行 头 空行 内容
    data_line = "HTTP/1.1 200 OK\r\n"
    data_head = "server/python\r\n"
    data_blank = "\r\n"
    # 打开limei
    try:
        with open("limei"+ file_path, 'rb') as limei:
            data_body = limei.read()
        data = (data_line + data_head + data_blank).encode() + data_body
    except Exception as e:
        with open("limei/index.html", 'rb') as limei:
            data_body = limei.read()
        data = (data_line + data_head + data_blank).encode() + data_body
    # 发送
    new_socket.send(data)
    new_socket.close()


web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置地址重用
web_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定端口
web_socket.bind(("", 8080))
# 监听
web_socket.listen(128)
# 接收客户端
while True:
    new_socket, ip_data = web_socket.accept()
    print(f"欢迎{ip_data}")
    # 接收客户端发送的内容
    work = threading.Thread(target=fasong, args=(new_socket, ip_data))
    work.setDaemon(True)
    work.start()
