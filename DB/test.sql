create table student(stu_id int,stu_name varchar(20),dep_name varchar(25));

alter table student add column gender varchar(10);
alter table student alter column gender type integer
using gender :: integer;
alter table student drop column gender;