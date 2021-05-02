--创建数据库
create database python_test_1 charset=utf8;

--使用数据库
use python_test_1;

--stu表
create table students(
    id int UNSIGNED PRIMARY key AUTO_INCREMENT not null,
    name varchar(20) default '',
    age tinyint UNSIGNED default 0,
    height DECIMAL(5,2),
    gender enum('男','女','中性','保密') DEFAULT '保密',
    cls_id int UNSIGNED DEFAULT 0,
    is_delete bit DEFAULT 0
);

--class表
create table classes(
    id int UNSIGNED AUTO_INCREMENT PRIMARY key not null,
    name VARCHAR(30) not null
);


--准备数据
INSERT INTO students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,0),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,null,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,0),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0),
(0,'凌小小',28,180.00,2,1,0),
(0,'司马二狗',28,120.00,1,1,0);

INSERT into classes values(0,"python_01期"),(0,"python_02期"),(0,"python_03期");