/*子查询 在一个select语句中 嵌入另外一个sellect语句 
那么被嵌入的select语句被称为子查询语句
子查询的种类
1.标量子查询 子查询返回结果是一个数据 select max(age) from students;
2.列子查询 返回结果是一列
3.行子查询 返回结果是一行
*/

--查询高于平均升高的所有人的信息
select avg(height) from students;
select * from students where height > 169.133333;
--用子查询显示
select * from students where height > (select avg(height) from students);
