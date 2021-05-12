--视图 把链接的过程创建一个虚拟的表,然后去连接这个表,就是个快照 比如说让笔记本名字 类型 品牌都显示在一个表里面
select goods.name '名称',goods_cates.name '类型',
goods_brands.name '品牌' from goods 
inner join goods_brands 
inner join goods_cates
on goods.cate_id = goods_cates.id and 
goods.brand_id = goods_brands.id;

--于是我们可以把这个表建立一个快照（视图）
--视图就是怼若干张基本表的引用。一张虚表，只查询语句执行结果的字段类型和约束，不能存储数据(基本表改变了,视图也会发生改变)

--创建视图 规范v_开头
--create view 视图名称 as select语句
create view v_goods_info as 
select goods.name '名称',goods_cates.name '类型',
goods_brands.name '品牌' from goods 
inner join goods_brands 
inner join goods_cates
on goods.cate_id = goods_cates.id and 
goods.brand_id = goods_brands.id;

--之后就可以用v_goods_info来查询了
select * from v_goods_info;

--删除视图
drop view v_goods_info;