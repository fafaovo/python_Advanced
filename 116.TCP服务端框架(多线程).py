import socket
import threading

"""
work = threading.Thread(target=Work, args=(tcp_socket,))
        work.setDaemon(True)
        work.start()

"""


def recv_msg(new_socket, ip_port):
    """当新用户进来时,会在此处循环"""
    while True:
        # 接收客户端发送的信息
        # 因为是通过python的客户端进行测试，是直接结束进程
        # 直接结束进程就不会进行四次挥手了
        # 固然会报错
        try:
            recv_data = new_socket.recv(1024)
            # 判断用户是否不发送信息
            if not recv_data:
                break
            else:
                # 将接收到的二进制转换
                recv_text = recv_data.decode()
                print(f"来自:{ip_port}的信息:{recv_text}")
        except Exception as a:
            print(a)
            break
    # 关闭
    new_socket.close()
    """
        正常使用时
        recv_data = new_socket.recv(1024)
        # 判断用户是否不发送信息
        if not recv_data:
            break
        else:
                # 将接收到的二进制转换
                recv_text = recv_data.decode()
                print(f"来自:{ip_port}的信息:{recv_text}")
    """


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置地址重用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_socket.bind(("", 8080))
    # 设置监听
    tcp_socket.listen(128)
    while True:
        # 接收客户端连接 此处会阻塞等待客户端连接
        new_socket, ip_port = tcp_socket.accept()
        print(f"新用户上线{ip_port}")
        # 创建线程
        work = threading.Thread(target=recv_msg, args=(new_socket, ip_port))
        work.setDaemon(True)
        work.start()


if __name__ == '__main__':
    main()
