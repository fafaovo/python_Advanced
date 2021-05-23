"""
思路
1.定义专门的函数，负责保存数据 add_film()
    1.定义SQL准备插入数据
    2.执行SQL语句
2.定义专门函数，负责检测数据库中是否存在 film_exist()
    1.定义sql，根据影片和地址查询
    2.执行查询，并获取查询的记录数
    3.如果获取的记录数>0 就返回值
3.创建连接对象 全局
4.创建游标对象 全局
5.关闭

"""

import urllib.request
import re
import pymysql


def add_film(film_name, film_link):
    """保存影片到数据库中"""
    # print("电影名称:" + film_name + ",磁力链接:" + film_link)
    if film_exist(film_name, film_link):
        print(f"保存失败{film_name},数据库中已存在")
        return
    else:
        sql = "insert into movie_link values(null,%s,%s)"
        ret = cur.execute(sql, [film_name, film_link])
        if ret:
            print(f"保存成功:{film_name}")
    pass


def film_exist(film_name, film_link):
    """用于检测数据是否已经存在"""
    sql = "select id from movie_link where film_name = %s and film_link = %s limit 1"
    """limit 1 查询完后如果返回多行 其实可以只显示一行，就表明其实已经有数据了，不需要插入了"""
    ret = cur.execute(sql, [film_name,film_link])
    if ret:
        return True
    else:
        return False
    pass


def get_mover_links():
    """获取列表页信息"""
    # 1.定义列表页的地址
    file_list_url = "https://www.ygdy8.net/html/gndy/dyzz/index.html"
    # 2.打开url地址，获取数据
    response_list = urllib.request.urlopen(file_list_url)
    # 2.1 通过read()读取网络资源数据
    response_list_data = response_list.read()
    # 3.解码获取到的数据
    response_list_text = response_list_data.decode("GBK", "ignore")  # ignore:忽视错误符
    # 4.使用正则得到所有影片内容页地址
    # 4.1 使用findall() 根据正则查找影片内容的地址
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)
    # 4.2 循环遍历 url_list 给获取到的网页前面加上 https://www.ygdy8.net
    for content, film_name in url_list:
        content = "https://www.ygdy8.net" + content
        # 4.3 打开内容页 接收内容页的数据
        res_cont = urllib.request.urlopen(content)
        # 4.4 读取网络资源
        res_cont_data = res_cont.read()
        # 4.5 解码得到内容页的文本内容
        res_cont_text = res_cont_data.decode("GBK", "ignore")
        # 4.6 取出下载地址
        result = re.search(r"<a target=\"_blank\" href=\"(.*?)\">", res_cont_text)
        add_film(film_name, result.group(1))
    pass


def main():
    get_mover_links()
    pass


if __name__ == '__main__':
    # 3.创建连接对象 全局
    conn = pymysql.connect(user="root", password="root", host="localhost", database="movie_db")
    # 4.创建游标对象 全局
    cur = conn.cursor()
    # 5.关闭
    main()
    conn.commit()
    cur.close()
    conn.close()
