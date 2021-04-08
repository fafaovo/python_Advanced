import socket
import multiprocessing

# 如果你的子进程用掉了一个对象，你最后在外边再给他关闭一次或者del一次

class WebServer(object):
    def __init__(self):
        """初始化"""
        web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        web_server.bind(("", 8080))
        web_server.listen(128)
        self.web_server = web_server
        pass

    def start(self):
        """启动服务器"""
        while True:
            # 此处程序会阻塞
            new_socket, ip_data = self.web_server.accept()
            # self.ServerHandle(new_socket, ip_data)
            # 进程使用分三步 1.导入模块 2.创建进程对象 3.启动子进程
            p1 = multiprocessing.Process(target=self.ServerHandle, args=(new_socket, ip_data))
            # 启动子进程
            p1.start()
            # 引用会复制一份，所以需要再关闭一次
            new_socket.close()


    def ServerHandle(self, new_socket, ip_data):
        """处理new_socket的信息"""
        print(f"欢迎{ip_data}")
        request_data = new_socket.recv(1024)
        if not request_data:
            print(f"{ip_data}已下线")
            return
        """将接受到的东西转换成人看的"""
        request_text = request_data.decode()
        """切出响应行"""
        reqLine = request_text[:request_text.find("\r\n")]
        """将响应行用空格分隔"""
        reqList = reqLine.split(" ")
        """底数为1的就是访问的链接了"""
        file_path = reqList[1]
        """当直接访问ip地址时，连接到index"""
        if file_path == "/":
            file_path = "/index.html"

        data_line = "HTTP/1.1 200 OK\r\n"
        data_head = "Server/python\r\n"
        data_head += "Content-Type: text/html\r\n"
        """让浏览器以html解析"""
        data_blank = "\r\n"

        try:
            with open("limei" + file_path, 'rb') as limei:
                data_body = limei.read()
            data = (data_line + data_head + data_blank).encode() + data_body
        except Exception as e:
            with open("limei/index.html", 'rb') as limei:
                data_body = limei.read()
            data = (data_line + data_head + data_blank).encode() + data_body
        # 发送
        new_socket.send(data)
        new_socket.close()


class main(object):
    web = WebServer()
    web.start()


if __name__ == '__main__':
    main()
