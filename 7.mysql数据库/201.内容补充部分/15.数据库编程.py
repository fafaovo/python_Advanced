"""数据库编程"""
import pymysql

# 连接数据库 需要创建一个connect(post,port,datebase,user,password,charset)   即Connection对象
"""
post连接的mysql主机
port连接的端口,默认是3306
database数据库名称
user连接的用户
password链接的密码
charset才用的编码方式
"""
# 获取游标 Cursor()
    # fetchone()从查询结果中取出一条数据
# 关闭连接 close()
# 提交数据 commit()
# 撤销数据 rollback()

# 1.建立连接对象 pymysql.connect()
conn = pymysql.connect(host='localhost', user='root', password='root', database='jing_dong', charset='utf8')
# 2.创建游标对象
cur = conn.cursor()
# 3.使用游标对象执行SQL语句 execute()可以传入sql语句 返回影响的行数
result = cur.execute('select * from goods')
# 4.获取执行的结果
print(f"查询到:{result}条数据")
# 5.打印输出获取的内容
# fetchone()从查询结果中取出一条数据  fetchall()全部数据
result_list = cur.fetchall()
for i in result_list:
    print(i)
# 6.关闭游标 关闭连接对象
cur.close()
conn.close()

