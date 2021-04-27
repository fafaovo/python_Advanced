--1.修改表结构
--增加字段 alter table 表名 add 列名 类型
alter table students add birthday datetime;
--重命名字段 alter table 表名 change 原名 别名 类型及约束;
alter table students change birthday birth datetime;
--修改字段类型 alter table 表名 modify 列名 类型及约束;
alter table students modify birth date not null;
--删除字段 alter table 表名 drop 列名;
alter table students drop birth;

--2.删除表 drop table 表名