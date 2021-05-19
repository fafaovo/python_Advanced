--修改权限
grant 权限名称 on 数据库 to 账户@主机 with grant option;

--给老王多一个update权限
grant select,update on jing_dong.* to 'laowang'@'localhost' with grant option;

--修改密码
alter user 账户@主机 IDENTIFIED by '新密码';
--修改完密码记得刷新