--创建商品分类的表
--if not exists 如果没有创建过则创建

CREATE TABLE if not exists goods_cates(
    id int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) not null
);

