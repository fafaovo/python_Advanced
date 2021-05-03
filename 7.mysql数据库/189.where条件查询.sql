--1.比较运算符，除去正常的各种比较运算符之外
--还有一个 <> 不等于（等同于!=）

--查询年龄不等于18岁的
select * from students where age != 18;
select * from students where age <> 18;


--逻辑运算符
--和python一样 and 表示&& ,or 表示||,not 表示!

--模糊查询 like
-- $表示任意多个任意字符
-- _表示一个任意字符

--查询姓黄的学生
select * from students where name like '黄%';

--查询有两个字的名字

select * from students where name like '__';