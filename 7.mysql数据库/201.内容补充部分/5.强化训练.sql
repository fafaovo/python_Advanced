--查询类型 cate_name 为超级本 商品名称 name 价格 price
select name,price from goods where cate_name = '超极本';

--显示商品种类 分组和去重
select cate_name from goods group by cate_name;
select distinct cate_name from goods;

--求所有电脑的平均价格

select round(avg(price),2) as '平均价格' from goods;

--显示每种类型平均价格
select cate_name,round(avg(price),2) as '平均价格' from goods GROUP BY cate_name asc;


--查询每种商品中最贵最便宜平均价数量
select cate_name,min(price),max(price),round(avg(price),2) '平均价格',count(price) from goods GROUP BY cate_name asc;

--查询所有价格大于 平均价格的商品 并且按价格降序排序order by
select * from goods where price > (select round(avg(price),2) from goods) order by price desc;

--查收每种电脑最贵的所有信息
--1.查收每种电脑最贵的
select cate_name,max(price) from goods GROUP BY cate_name asc;
--2.自连接
select goods.* from goods
inner join 
(select cate_name,max(price) as max_price from goods GROUP BY cate_name asc) as max_price_goods     --给表起别名
on goods.cate_name = max_price_goods.cate_name and
goods.price = max_price_goods.max_price;




