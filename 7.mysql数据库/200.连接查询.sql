/*
内连接查询 查询两个表匹配的数据    ([)(])
右(外)连接查询 查询结果为两个表匹配的数据和右表特有的数据  ([)()]
左(内)连接查询 查询结果为两个表匹配的数据和左表特有的数据  [()(])
内外连接查询对于另外一张表中不存在的数据使用null填充
*/


--进行两个表的链接 inner join 字段数等于两个表之和
select * from students inner join classes;
--这种叫笛卡尔积 全连接
select * from students inner join classes where students.cls_id = classes.id;
select * from students,classes where students.cls_id = classes.id;

--只显示姓名和班级
select stu.name '姓名',cla.name '班级' from 
students stu,classes cla WHERE 
stu.cls_id =  cla.id;