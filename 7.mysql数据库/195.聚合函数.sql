--聚合函数 求集合中的最大值最小值 数量 和 平均值 等等 又称为组函数
--语法: select 聚合函数 from 数据库 [可选where条件查询];
--常见的聚合函数
--1.count(*) 计算总行数
--2.max(列) 求此列的最大值
--3.min(列) 求此列的最小值
--4.sum(列) 求此列的和
--5.avg(列) 球平均值

--聚合函数不能嵌套 不能识别null


--计算总人数 并且给别名
select count(*) '总人数' from students;

--查询男性总人数
select count(*) '总人数' from students where gender='男';

--查询最大年龄
select max(age) '年龄最大' from students;

--查询女性的最高升高
select max(height) '最高升高' from students where gender='女';

--求年龄总和
select sum(age) '年龄总和' FROM students;

--求平均值
select avg(age) from students;
select sum(age)/count(*) '平均值' from students;

--四舍五入 round(值,小数点保留的位数) round不是聚合函数,所以可以嵌套
select round(avg(age),2) '平均值' from students;

--计算男性的平均身高
select round(avg(height),2) '男均高' from students where gender='男';