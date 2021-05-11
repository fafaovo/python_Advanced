
* select version(); 显示版本
* select now(); 显示时间
* show databases 查看所有数据库
* show:查看 use:使用 create:创建 drop:删除
    + create database 数据库名 用于创建数据库
        + create database 数据库名 charset=utf8;
        + show create database 数据库名;查看数据库的创建过程 \G 不格式化显示
    + drop database 数据库名字 用于删除数据库
    + use 数据库 切换数据库
    + select database() 查看当前数据库
    + show tables; 查看当前数据库表的名称
    + desc 表; 查看表结构
* 创建数据表
    > create table 表名{  
    >    字段名称 数据类型 可选的约束条件 [在约束后面写上auto_increment表示自动增长]  
    >    colum1 datatype contrai,  
    >    colum1 datatype,  
    >    colum1 datatype,  
    >};  
* 修改表结构
    + 增加字段 alter table 表名 add 列名 类型
    + 重命名字段 alter table 表名 change 原名 别名 类型及约束;
    + 修改字段类型 alter table 表名 modify 列名 类型及约束;
    + 删除字段 alter table 表名 drop 列名;
    + 创建项目后最好不要修改表的结构，可以额外增加三四个预留字段
* 增删查改
    + 查询所有列 select * from 表名
    + 插入表 
        + 全部插入 insert into 表名 values(字段1,字段2)
        + 指定插入 insert into 表名(字段,字段) values(字段1,字段2) 多行插入使用,隔开
    + 修改 update 表名 set 列名 = 值 where 条件;
    + 删除 delete from 表名 where 条件;
* 数据库的备份 命令行内
    + 备份 mysqldump -uroot -p 数据库名 > 文件名.sql
    + 倒入 mysql -uroot -p 数据库名 < 要导入的脚本.sql
* 范围查询
    + in()表示在一个非连续的范围内
    + between...and...表示一个连续的范围内
* 排序 order by
    + select * from 表名 order by 列1 asc(升序)|desc(降序)
* 聚合函数 求集合中的最大值最小值 数量 和 平均值 等等 又称为组函数
    + 语法: select 聚合函数 from 数据库 [可选where条件查询];
    + 常见的聚合函数
    + 1.count(*) 计算总行数
    + 2.max(列) 求此列的最大值
    + 3.min(列) 求此列的最小值
    + 4.sum(列) 求此列的和
    + 5.avg(列) 球平均值
    + round(值,小数点保留的位数) round不是聚合函数,所以可以嵌套
* group by 分组
    + 在mysql默认情况下，select后字段只能出现以下两种情况
        + 1.在group by后出现的 
        + 2.在聚合函数中出现的
    + 语法 group by 按照什么分组
* limit限制记录 limit一定要写在sql语句的最后面
    + limit 起始位置,记录数 
* 连接查询
    + 内连接 inner join 可以使用 on 代替where





