
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





* 链接数据库 mysql -uroot -proot
* 链接数据库无密码 mysql -uroot -p
* 退出数据库 exit quit ctrl+d
* 显示数据库版本 select version();
* 显示时间 select now();
* 查看当前使用的数据库 select database();
* 查看所有数据库 show databases;
* 创建数据库 create database 数据库 charset=utf8;
* 删除数据库 drop database 数据库
