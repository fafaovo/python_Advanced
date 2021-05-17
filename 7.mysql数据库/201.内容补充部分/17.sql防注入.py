"""
注入：用于在输入中使用mysql语句，造成数据泄露
"""
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='root', database='jing_dong', charset='utf8')
cur = conn.cursor()
# sql = "insert into goods values(null,'老王牌拖拉机',1,1,9998,1,1)"
input_name = input("请输入要查询的名称:\n")
# 注入输入 ' or 1 or ' 数据库就沦陷了全出来了，就是被注入了
# 如何防止植入呢
# 1) 构建参数列表 params = [input_name]
# 2) 把列表传递给 execute(sql,params)
params = [input_name]
# 此处的%s就是对应params里面的[0] 允许多个占位符
sql = "select * from goods where name = %s"
result = cur.execute(sql, params)
# sql = "select * from goods where name = '%s'" % input_name
# result = cur.execute(sql)
print(f"查询到:{result}")
for i in cur.fetchall():
    print(i)

cur.close()
conn.close()
