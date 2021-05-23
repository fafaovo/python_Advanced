create database movie_db charset=utf8;
use movie_db;
create table movie_link(
    id int(11) primary key AUTO_INCREMENT,
    film_name varchar(255) not null,
    film_link varchar(255) not null
)charset=utf8;

alter table movie_link modify film_link text;