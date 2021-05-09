/*
左连接:主表 left join 从表 on 连接条件
右链接:从表 right join 主表 on 连接条件

保留主表所有的结果，从表没连接成功则补null
*/
--查询每位学生对应的班级信息
select * from students left join classes on students.cls_id = classes.id;

--查询没有对应班级的学生
select students.* from students left join classes  
on students.cls_id = classes.id where classes.id is null;



