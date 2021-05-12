--用于存储goods的分类信息
--查看goods的分类信息
select cate_name from goods group by cate_name;

--一条语句插入
insert INTO goods_cates(name) (select cate_name from goods group by cate_name);

--此时，将goods表中的cate_name 替换成 goods_cates表中的id
update goods inner join goods_cates 
on goods.cate_name = goods_cates.name 
set goods.cate_name = goods_cates.id;

--查看
select * from goods INNER JOIN goods_cates
where goods.cate_id = goods_cates.id;

--修改表结构 将cate_name改成cate_id 
alter table goods change cate_name cate_id int unsigned not null;


--goods_brands品牌的表 一条语句插入
insert into goods_brands(name) (select brand_name from goods group by brand_name);
--将品牌替换为id
update goods inner join goods_brands
on goods.brand_name = goods_brands.name
set goods.brand_name = goods_brands.id;

--将cate_name 改为cate_id
alter table goods change brand_name brand_id int unsigned not null;
