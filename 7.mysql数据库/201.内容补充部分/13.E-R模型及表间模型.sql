--E-R模型 即E-R图 即实体-联系图 
--是指提供了表示实体型 属性和联系的方法，用来描述现实世界的概念模型

--在设计阶段一般使用E-R模型进行建模power designer ,db desinger等工具
--然后才是设计数据库


--多对多时候，需要一个附加表

/*
表间关系：
一对一  一个表中的一条数据能够和另外一个表的唯一一条数据对于 人和常驻地址
一对多  一个表中的数据能够另外一个表中多条数据对于 一个班有多个学生
多对多  一个表中的一条数据能够和另外一个表的多条数据对应，反之也对应 一个学生有多个课程

处理多对多的关系,建立中间表
*/