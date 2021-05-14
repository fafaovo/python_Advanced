--创建一个顾客表 订单表 详细订单表
create table customer(
    id int unsigned AUTO_INCREMENT PRIMARY key not null,
    name VARCHAR(30) not null,
    addr VARCHAR(100),
    tel VARCHAR(11) not null
);

create table orders(
    id int unsigned AUTO_INCREMENT PRIMARY key not null,
    order_date_time DATETIME not null,
    customer_id int unsigned,
    foreign key(customer_id) REFERENCES customer(id)
);

create table order_detail(
    id int unsigned AUTO_INCREMENT PRIMARY key not null,
    order_id int UNSIGNED not null,
    goods_id int UNSIGNED not null,
    quantity tinyint UNSIGNED not null,
);
alter table  order_detail add foreign key (order_id) REFERENCES orders(id);
alter table order_detail add foreign key (goods_id) REFERENCES goods(id);

