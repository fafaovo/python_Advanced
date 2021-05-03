--在mysql中有个 null 空值
--查询没有填写身高的学生
select * from students WHERE height is null;
--查询填写了

select * from students WHERE height is not null;