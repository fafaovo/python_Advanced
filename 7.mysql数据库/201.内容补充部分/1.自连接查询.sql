--特殊的内连接 自连接查询 自连接 左手拉右手 自己连接自己
create table city(
    id int UNSIGNED PRIMARY key AUTO_INCREMENT not null,
    atitle VARCHAR(30) not null,
    pid int UNSIGNED DEFAULT NULL
);

INSERT into city values
(0,'广东省',null),(0,'河南省',null),
(0,'深圳市',1),(0,'广州市',1),
(0,'南山区',3),(0,'宝安区',3);

--查看有多少个省
select count(*) from city where pid is null;

--查看广东省的市

select * from city p inner join city c on c.pid = p.id WHERE p.atitle = '广东省';