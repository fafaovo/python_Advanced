
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





* 链接数据库 mysql -uroot -proot
* 链接数据库无密码 mysql -uroot -p
* 退出数据库 exit quit ctrl+d
* 显示数据库版本 select version();
* 显示时间 select now();
* 查看当前使用的数据库 select database();
* 查看所有数据库 show databases;
* 创建数据库 create database 数据库 charset=utf8;
* 删除数据库 drop database 数据库
