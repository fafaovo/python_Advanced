# 1.导入模块
import socket
import pymysql


def conMysql():
    conn = pymysql.connect(user="root", password="root", host="localhost", database="movie_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("select * from movie_link order by id desc")
    result = cur.fetchall()
    show = ''
    for row in result:
        show += "%d.%s  磁力链接<a href='%s'>%s</a><br>" % (row[0], row[1], row[2],row[2])
    cur.close()
    conn.close()
    return show


def request_handler(new_client_socket, ip_port):
    # 7.获取客户端发送的请求协议
    request_data = new_client_socket.recv(1024)
    # 8.判断协议是否为空
    if not request_data:
        print(f"{str(ip_port)}客户端已下线")
        new_client_socket.close()
        return
    # 9.拼接相应报文
    # 9.1响应行 9.2响应头 9.3响应空行 9.4响应主题
    response_line = "HTTP/1.1 200 OK\r\n"
    response_head = "Server:python20WS/2.1\r\n"  # 随意写个服务器
    response_head+= "Content-type:text/html;charset=utf-8\r\n"
    response_blank = "\r\n"
    # response_body = "<h1>HelloWorld!</h1>"
    response_body = conMysql()

    request_data = response_line + response_head + response_blank + response_body
    # 10.发送响应
    new_client_socket.send(request_data.encode())
    new_client_socket.close()
    pass


def main():
    """主函数"""
    # 2.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3.设置地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 4.绑定端口
    tcp_server_socket.bind(("", 8080))
    # 5.设置监听
    tcp_server_socket.listen(128)
    # 6.接收客户端连接
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print(f"{ip_port}来了")
        request_handler(new_client_socket, ip_port)
        # 这是一个函数
    pass


if __name__ == '__main__':
    main()
