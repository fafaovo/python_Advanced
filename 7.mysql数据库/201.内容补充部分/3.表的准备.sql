--创建
create database jing_dong charset = utf8;

use jing_dong;

--表的创建
CREATE TABLE goods(
    id int UNSIGNED PRIMARY KEY AUTO_INCREMENT not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null DEFAULT 0,
    is_show bit not null DEFAULT 1,
    is_saleoff bit not null DEFAULT 0
);

--数据
insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕',3399,default,default);
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想',4999,default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神',8499,default,default);
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕',2799,default,default);
insert into goods values(0,'x240 超极本','超极本','联想',4880,default,default);
insert into goods values(0,'u330p 13.3英寸超极本','超极本','联想',4299,default,default);
insert into goods values(0,'svp13226scb 触控超极本','超极本','索尼',7999,default,default);
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果',1998,default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果',3388,default,default);
insert into goods values(0,'ipad mini 配备 retina 显示器','平板电脑','苹果',2788,default,default);
insert into goods values(0,'ideacenter c340 20英寸一体电脑','台式机','联想',3499,default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔',2899,default,default);
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果',9188,default,default);
insert into goods values(0,'at7-7414lp 台式电脑 linux','台式机','宏基',3699,default,default);
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普',4288,default,default);
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔',5388,default,default);
insert into goods values(0,'mac pro 专业级台式电脑','服务器/工作站','苹果',28888,default,default);
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼',6999,default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼',99,default,default);
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm',6888,default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼',99,default,default);