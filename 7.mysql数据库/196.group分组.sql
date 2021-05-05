--group by 分组
--在mysql默认情况下，select后字段只能出现以下两种情况
--1.在group by后出现的 2.在聚合函数中出现的

--按照性别分组，查询所有性别
select gender from students group by gender;

--计算每一种性别的人数
select gender '性别',count(*) '人数' from students group by gender;

--计算每一个年龄的人数
select age '年龄',count(*) '人数' from students group by age;


--group by + group_concat(字段名); 将分组结果连接成一个字符串

--查询同种性别中的名字
select gender,group_concat(name) from students GROUP BY gender;
+--------+---------------------------------------------------------------------+
| gender | group_concat(name)                                                  |
+--------+---------------------------------------------------------------------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖,司马二狗                               |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰,凌小小                       |
| 中性   | 金星                                                                |
| 保密   | 凤姐                                                                |
+--------+---------------------------------------------------------------------+

--查询每组性别的平均年龄
select gender,round(avg(age),2) from students GROUP BY gender;

--group by + having 用于过滤 分组后结果 [where会在group之前执行]
--where是在查询时过滤的 having是在分组后进行过滤

--查询每组性别的平均年龄大于30的
select gender,round(avg(age),2) from students GROUP BY gender having avg(age)>30;
--你也可以起别名
select gender,round(avg(age),2) AVG from students GROUP BY gender having AVG>30;

--查询每种性别的平均年龄和名字
select gender,round(avg(age),2),group_concat(name) from students GROUP BY gender;

--查询每种性别中的人数多于两个的性别和名字
select gender,count(gender),group_concat(name) from students GROUP BY gender having count(gender) > 2;


--with rollup 汇总
select gender,count(*) from students GROUP BY gender with rollup;