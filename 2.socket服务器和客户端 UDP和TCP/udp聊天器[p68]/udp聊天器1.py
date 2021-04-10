"""
一.功能
1.发送信息
2.接收信息
3.退出系统

二.框架的设计
1.发送信息 send_msg()   [message]
2.接收信息 recv_msg()
3.程序主入口 main()
4.当程序独立运行的时候才启动聊天器

三.实现步骤
1.发送信息 send_msg()
    1.定义变量接收用户输入的接收方的ip地址
    2.定义变量接收用户输入的接收方的端口号
    3.定义变量接收用户输入的接收方的内容
    4.使用socket的sendto()发送信息
2.接收信息 recv_msg()
    1.使用socket 接收数据
    2.解码数据
    3.输出显示
3.主入口main()
    1.创建套接字
    2.绑定端口
    3.打印菜单(循环)
    4.接收用户输入的选项
    5.判断用户选择并且调用对应的函数
    6.关闭套接字
"""
import socket


def sed_msg(udp_socket):
    """发送信息的函数"""
    ipaddr = input("请输入接收方的ip地址:")
    port = input("请输入接收方的端口号:")
    content = input("请输入要发送的内容:")
    udp_socket.sendto(content.encode(), (ipaddr, int(port)))
    pass


def recv_msg(udp_socket):
    """接收信息的函数"""
    data, ip_port = udp_socket.recvfrom(1024)
    ip, port = ip_port
    print(f"接收ip地址为{ip},端口号为{port},发送的信息为\n{data.decode()}")
    pass


def menu():
    """菜单"""
    print("*********************")
    print("*****1.发送信息  *****")
    print("*****2.接收信息  *****")
    print("*****3.退出系统  *****")
    print("*********************")
    pass


def main():
    """程序主函数入口"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 8080))
    # 打印菜单
    while True:
        menu()
        select = int(input("请选择:>"))
        if select == 1:
            print("你选择的是发送信息")
            sed_msg(udp_socket)
        elif select == 2:
            print("你选择的是接收信息")
            recv_msg(udp_socket)
        elif select == 3:
            print("退出系统")
            udp_socket.close()
            break
    pass


if __name__ == '__main__':
    """程序独立运行的时候启动聊天器 main+tab"""
    main()
