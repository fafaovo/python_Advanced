/*
当多个表有关联时，可以使用外键约束来避免
数据乱用

一个表的主键A在另外一个表B中出现我们说A是B表的应该外键

在存在的表中建立关联
 alter table 表名 add foreign (字段名) references 要关联的表名(字段名);
 对于已经存在的表如果要关联，要先把无效的数据干掉

 在建立表时建立关联
 foreign key(字段名) references 已存在的表(以及他的字段名)
*/
alter table goods add foreign key (brand_id) references goods_brands(id);

CREATE table goods_test(
    id int PRIMARY AUTO_INCREMENT ,
    name VARCHAR (150) not null,
    cate_id int UNSIGNED not null,
    brand_id int UNSIGNED not null,
    FOREIGN KEY (cate_id) REFERENCES goods_cates(id),
);

--删除外键
--首先我们要通过show create table 表名; 来查看外键名称
--外键名称通奶草在 xxx 名称 FOREIGN KEY 里面
--alter table 表名 drop foreign key 外键名称