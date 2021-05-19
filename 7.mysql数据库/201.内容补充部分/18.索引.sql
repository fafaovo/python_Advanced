/*
索引：参考字段目录
底层：B+树

sql语句
创建索引: show index from 表名
创建索引：create index 索引名称 on 表名(字段名称(长度))
如果不是字符串类型则不需要字段长度
删错索引：drop index 索引名称 on 表名
*/
-- 给name创建索引
-- create index idx_1 on goods (name(150));
