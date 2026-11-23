create table student(stu_id int,stu_name varchar(20),dep_name varchar(25));

alter table student add column gender varchar(10);

select * from student

insert into student values(1,'Riyas','MCA');
insert into student values(2,'Magu','MCA'),(3,'Kai','BTECH');

update student set dep_name='MCA' where dep_name='BTECH';

select stu_name,dep_name from student;
insert into student(stu_id,dep_name) values(4,'BTECH');
delete from student where stu_name='Kai'



-- Primary Key
-- its allow only unique elements it does not allow duplicate and null value it is also call as a constrain

create table emp(emp_id int primary key,name varchar(20),dept varchar(20));
alter table emp add column salary int;
alter table emp add column date_of_join date;
select * from emp;

-- create a table name employee id,empname,dept,salary,doj  100 data


create table employee (empid int primary key,empname varchar(20),dept varchar(20),salary int,date_of_join date);

INSERT INTO employee (empid, empname, dept, salary, date_of_join)
VALUES
(101, 'Arun', 'IT', 35000, '2022-01-15'),
(102, 'Priya', 'HR', 28000, '2021-03-20'),
(103, 'Karthik', 'Finance', 42000, '2020-06-10'),
(104, 'Divya', 'IT', 45000, '2019-08-12'),
(105, 'Vijay', 'Marketing', 30000, '2023-02-01'),
(106, 'Sneha', 'HR', 32000, '2022-04-18'),
(107, 'Ramesh', 'Sales', 27000, '2021-07-25'),
(108, 'Kavya', 'IT', 50000, '2018-11-05'),
(109, 'Suresh', 'Finance', 38000, '2022-09-14'),
(110, 'Meena', 'Marketing', 33000, '2020-12-01'),
(111, 'Ajith', 'IT', 40000, '2021-01-10'),
(112, 'Nithya', 'HR', 29000, '2023-05-22'),
(113, 'Prakash', 'Sales', 31000, '2022-02-16'),
(114, 'Ramya', 'Finance', 46000, '2019-04-08'),
(115, 'Dinesh', 'IT', 55000, '2017-10-19'),
(116, 'Lakshmi', 'Marketing', 36000, '2021-06-30'),
(117, 'Manoj', 'Sales', 34000, '2020-03-11'),
(118, 'Anitha', 'HR', 31000, '2022-08-09'),
(119, 'Saravanan', 'Finance', 48000, '2018-05-17'),
(120, 'Keerthi', 'IT', 37000, '2023-01-25'),
(121, 'Bala', 'Sales', 26000, '2023-07-12'),
(122, 'Pavithra', 'Marketing', 39000, '2019-09-21'),
(123, 'Gokul', 'IT', 43000, '2020-10-15'),
(124, 'Shalini', 'HR', 35000, '2021-12-05'),
(125, 'Mohan', 'Finance', 41000, '2022-06-19'),
(126, 'Deepa', 'Sales', 30000, '2022-11-23'),
(127, 'Surya', 'IT', 60000, '2016-04-14'),
(128, 'Aishwarya', 'Marketing', 32000, '2023-03-08'),
(129, 'Ravi', 'Finance', 44000, '2020-07-27'),
(130, 'Harini', 'HR', 30000, '2023-08-16'),
(131, 'Naveen', 'IT', 39000, '2021-05-03'),
(132, 'Swetha', 'Sales', 37000, '2019-02-28'),
(133, 'Kumar', 'Finance', 52000, '2017-12-11'),
(134, 'Monisha', 'Marketing', 34000, '2022-10-07'),
(135, 'Sanjay', 'IT', 47000, '2019-06-24'),
(136, 'Revathi', 'HR', 33000, '2020-09-13'),
(137, 'Hari', 'Sales', 29000, '2023-04-20'),
(138, 'Abinaya', 'Finance', 39000, '2021-08-02'),
(139, 'Vignesh', 'IT', 52000, '2018-03-16'),
(140, 'Janani', 'Marketing', 37000, '2020-11-29'),
(141, 'Praveen', 'Sales', 35000, '2021-10-06'),
(142, 'Gayathri', 'HR', 27000, '2023-06-14'),
(143, 'Senthil', 'Finance', 47000, '2019-01-19'),
(144, 'Yamuna', 'IT', 41000, '2022-07-04'),
(145, 'Ashok', 'Marketing', 31000, '2021-04-26'),
(146, 'Bhavani', 'Sales', 32000, '2022-12-15'),
(147, 'Lokesh', 'IT', 58000, '2017-07-09'),
(148, 'Madhavi', 'Finance', 36000, '2023-02-17'),
(149, 'Kishore', 'HR', 34000, '2020-05-31'),
(150, 'Sowmiya', 'Marketing', 40000, '2018-09-10');


select * from employee;
