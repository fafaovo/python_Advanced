--limit限制记录 limit一定要写在sql语句的最后面
--limit 起始位置,记录数 
--从起始位置开始取记录数跳
--底数从0开始
select * from students limit 0,3;
select * from students limit 3;

--分页查询 
--每页显示两条，显示第一页
select * from students limit 0,2;
select * from students limit 2,2;
select * from students limit 4,2;
select * from students limit 6,2;
select * from students limit 8,2;

--计算公式 limit (页码-1)*每页数量 , 每页数量;
