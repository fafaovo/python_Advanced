--1.比较运算符，除去正常的各种比较运算符之外
--还有一个 <> 不等于（等同于!=）

--查询年龄大于18岁的
select * from students where age>18;
--查询年龄不等于18岁的
select * from students where age != 18;
select * from students where age <> 18;


--逻辑运算符 