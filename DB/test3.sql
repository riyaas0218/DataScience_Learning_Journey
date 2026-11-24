select * from employee;

select * from employee where empname like 'A%';
select * from employee where empname like '%h';
select * from employee where empname like '_e%';
select * from employee where empname like 'R%s';
select * from employee where empname like '%w%';


                         -- constrains


--constrains means rules applied to table columns to maintain data accuracy and intgratity
--important 6 type of constains
--Notnull,unique,Primary key,forign key,check,defauld,serial


create table emptest(emp_id serial primary key,ename varchar(20) not null);
insert into emptest(ename) values('Riyas');
insert into emptest(ename) values('Ajmal');

alter table emptest add column card varchar(10) unique;
alter table emptest add column age int check(>20);

alter table emptest add column course varchar(20) default 'python';

select * from emptest;


      -- Foreign key

	  --Foreign key is the constrain used to connect two table in a database
	  --Foreign relationship between tables by referring to the primary key of another table


create table dept(dept_id int primary key,dname varchar(20),empid int,constraint for_key foreign key(empid) references emptest(empid));

alter table dept drop constraint for_key;