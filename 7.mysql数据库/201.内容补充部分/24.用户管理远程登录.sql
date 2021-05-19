--授权root远程登录权限,慎用
grant all on *.* to 'root'@'%';

--登录 在控制台中
mysql -h主机名 -uroot -proot