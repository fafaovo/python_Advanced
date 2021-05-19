--root超级管理员，可以对mysql进行任何操作
use mysql;
select Host '主机',User '用户名',authentication_string ‘加密后的密码’ from user;
--如果主机显示% 则可以在任何地方使用 密码使用的md5加密

--创建用户
--常用权限 create alter drop insert update delete select
--所有权限 all privileges

--创建用户
 create user '用户名' @'主机' identified by '密码';
 --授权 数据库.表名都可以用* *.*
 grant 权限 on 数据库.表名 to '用户名'@'主机名';

 --创建一个laowang的账号 密码为123456,只能本地登录，并且只能查询
 create user 'laowang' @'localhost' IDENTIFIED by '123456';
 grant select on *.* to 'laowang'@'localhost';

--刷新权限
 flush privileges;

 --创建一个laoli的账号，密码为123456，可以在任意电脑进行访问，并且对jing_dong表拥有所有权限
 create user 'laoli'@'%' identified by '123456';
 grant all PRIVILEGES on jing_dong.* to 'laoli'@'%';