import pymysql

def main():
    conn = pymysql.connect(host='localhost', user='root', password='root', database='python_index_db', charset='utf8')
    cur = conn.cursor()
    for i in range(100000):
        result = cur.execute('insert into test_index(title) values("ha-%d")' % i)
    conn.commit()

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()

"""
在mysql中可以使用
set profiling = 1; 来开启时间监测
show profiles; 查看执行时间

--创建索引
create index idx_1 on test_index(title(10));


没有索引   0.15456500
有索引     0.00033075

索引虽好。但是不要贪杯，仅限不经常变化的表中使用
"""
