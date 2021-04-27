CREATE TABLE classes(
    -- PRIMARY KEY 主键 自动增长
    id int unsigned PRIMARY KEY auto_increment,
    name VARCHAR(10) not null,
    num TINYINT
);


CREATE TABLE students(
    --   字段名称 数据类型 可选的约束条件 [在约束后面写上auto_increment表示自动增长]
    id int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) not null,
    age TINYINT,
    -- DECIMAL(总位数,小数位)
    high DECIMAL(3,2),
    gender enum("男","女","保密"),
    cls_id INT UNSIGNED 
);