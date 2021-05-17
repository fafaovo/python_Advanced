import pymysql
conn = pymysql.connect(host='localhost', user='root', password='root', database='jing_dong', charset='utf8')
cur = conn.cursor()
# sql = "insert into goods values(null,'老王牌拖拉机',1,1,9998,1,1)"
sql = "delete from goods where id = 22"
result = cur.execute(sql)
print(f"影响行数:{result}")
# 修改需要提交 conn.commit() 刚刚提交的结果
conn.commit()

cur.close()
conn.close()
