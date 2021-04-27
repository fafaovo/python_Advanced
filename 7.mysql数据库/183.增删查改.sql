--创建(create)   -> insert
--更新(update)   -> update
--读取(retrieve/read)  -> select
--删除(delete)   -> delete

--查询所有列 select * from 表名
select * from classes;
--条件查询 select * from 表名 where 条件
select * from students where name='张三';
--* 全部 也可以替换成条件 先id然后name
select id,name from students;
-- as 别名
select id as '编号' ,name as '姓名' from students;

--插入表 insert into 表名 values(字段1,字段2)
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(10)      | NO   |     | NULL    |                |
| num   | int(11)          | YES  |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
insert into classes values(1,"张三",78);
--id是主键自动增长，所以可以传入一个null，让他自动增长
insert into classes values(null,"李四",78);
-- 假设只想插入某些字段
--+----------------------------+------+-----+---------+----------------+
| Field  | Type                       | Null | Key | Default | Extra          |
+--------+----------------------------+------+-----+---------+----------------+
| id     | int(10) unsigned           | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)                | NO   |     | NULL    |                |
| age    | tinyint(4)                 | YES  |     | NULL    |                |
| high   | decimal(3,2)               | YES  |     | NULL    |                |
| gender | enum('男','女','保密')     | YES  |     | NULL    |                |
| cls_id | int(10) unsigned           | YES  |     | NULL    |                |
+--------+----------------------------+------+-----+---------+----------------+
insert into students(id,name) values(null,"张三");
--多行插入
insert into students(id,name) values(null,"张三"),(null,"李四");

--修改 update 表名 set 列名 = 值 where 条件;
update students set age = 38 where name = '张三';
update students set name = '张三' where id = 1;
--多行修改依然使用,隔开
update students set age = 42,high = 1.58,gender='男',cls_id=35 where name = '张三';


