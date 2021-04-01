import socket
import threading
import time


def menu():
    """菜单"""
    time.sleep(0.05)
    print("*********************")
    print("*****1.发送信息  *****")
    print("*****2.退出系统  *****")
    print("*********************")
    pass


def sed_msg(udp_socket):
    """发送信息"""
    upd_ip = input("请输入ip地址")
    udp_port = input("请输入端口号")
    udp_text = input("请输入要发送的内容")
    udp_socket.sendto(udp_text.encode(), (upd_ip, int(udp_port)))
    pass


def recv_msg(udp_socket):
    """接收信息"""
    data, ip_port = udp_socket.recvfrom(1024)
    ip, port = ip_port
    print(f"接收来自{ip},的内容:{data.decode()}")
    pass


def Work(udp_socket):
    while True:
        recv_msg(udp_socket)
    pass


def main():
    # 设置套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定接口
    udp_socket.bind(("", 8080))
    select = 0
    # 创建线程
    work = threading.Thread(target=Work, args=(udp_socket,))
    # 设置守护主线程
    work.setDaemon(True)
    work.start()

    while True:
        menu()
        try:
            select = int(input("请选择:>"))
        except Exception as e:
            print("请重新输入")
        if select == 1:
            sed_msg(udp_socket)
            pass
        elif select == 2:
            udp_socket.close()
            exit()
            pass


if __name__ == '__main__':
    main()
