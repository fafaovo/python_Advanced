--1.停止mysql服务
--2.编辑msql配置文件
    --/mysql/mysql.conf.d/mysqld/cnf
    --在{mysqlid}段下加入一行 "skip-grant-table" 让mysql跳过正常验证
--3.重启mysql服务
--4.直接进入控制台
--5.修改密码，先设置root 为空
    --使用这句话: update user set authentication_string='' where user='root';
--6.退出控制台并且删除/注释2加入的那句话
--7.重启，然后修改密码