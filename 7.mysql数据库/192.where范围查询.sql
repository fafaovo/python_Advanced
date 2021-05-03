--范围查询 
--in表示在一个非连续的范围内
--between...and...表示一个连续的范围内
--查询编号为1 3 8的学生
select * from students where id = 1 or id = 3 or id = 3;
--使用in
select * from students where id in(1,3,8);

--between...and...表示一个连续的范围内
--查询编号3至8的学生
select * from students WHERE  age>=3 and age<=8;
select * from students where age between 3 and 8;
