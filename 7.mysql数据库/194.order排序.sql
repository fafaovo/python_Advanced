--排序 order by
--select * from 表名 order by 列1 asc(升序)|desc(降序)
--年龄在18到34之间年龄为男性按照年龄升序排序
select * from students where 
age BETWEEN 18 and 34 and gender='男' 
order by age asc;

--年龄在18到34之间年龄为女性,
--按照身高降序排序年龄,
--如果身高相同按照年龄降序，
--如果年龄相同按照id升序
select * from students WHERE 
age between 18 and 34 and gender='女'
order by height desc,age desc,id asc;
