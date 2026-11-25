select * from employee;

select distinct dept from employee;


select * from employee order by empid ;

select * from employee order by empid  desc;

---Aggregate function

 --sum,count,min,max,avg
select sum(salary) total_salary from employee;
select avg(salary) avg_salary from employee;
select min(salary) min_salary from employee;
select max(salary) max_salary from employee;


select * from emp;



--String Functions
   --upper,lower,length,concat,replace,left,rigt

select upper(dept),lower(empname) from employee;
select empname,length(empname) lengthofname from employee;
select empname,concat('₹ ',salary) from employee;
select empname,replace(dept,'HR','Developer') from employee;
select left(empname,3 ) from employee;
select right(empname,2) from employee


create table emp1(empname varchar(20) ,dept varchar(20),salary int,city varchar(20));
INSERT INTO emp1 (empname, dept, salary, city)
VALUES
('Riyas', 'Python', 45000, 'Chennai'),
('Arun', 'Java', 55000, 'Trichy'),
('Karthik', 'HR', 28000, 'Chennai'),
('Vijay', 'Python', 35000, 'Madurai'),
('Suresh', 'Java', 65000, 'Chennai'),
('Praveen', 'HR', 32000, 'Trichy'),
('Ajith', 'Python', 60000, 'Trichy'),
('Rahul', 'Java', 25000, 'Madurai'),
('Dinesh', 'Testing', 40000, 'Chennai'),
('Manoj', 'Python', 75000, 'Coimbatore'),
('Bala', 'Java', 42000, 'Trichy'),
('Santhosh', 'HR', 50000, 'Chennai'),
('Gokul', 'Testing', 30000, 'Madurai'),
('Hari', 'Python', 52000, 'Chennai'),
('Naveen', 'Java', 38000, 'Coimbatore'),
('Mohan', 'HR', 27000, 'Trichy'),
('Surya', 'Python', 68000, 'Madurai'),
('Kumar', 'Java', 48000, 'Chennai'),
('Prakash', 'Testing', 35000, 'Trichy'),
('Deepak', 'HR', 45000, 'Coimbatore'),
('Anand', 'Python', 29000, 'Chennai'),
('Ramesh', 'Java', 72000, 'Trichy'),
('Vimal', 'Testing', 55000, 'Madurai'),
('Sathish', 'HR', 38000, 'Chennai'),
('Kavin', 'Python', 80000, 'Trichy'),
('Ashwin', 'Java', 33000, 'Coimbatore'),
('Ganesh', 'Testing', 26000, 'Chennai'),
('Lokesh', 'HR', 62000, 'Madurai'),
('Muthu', 'Python', 41000, 'Trichy'),
('Sanjay', 'Java', 58000, 'Chennai'),
('Varun', 'Testing', 47000, 'Coimbatore'),
('Nithin', 'HR', 30000, 'Trichy'),
('Dharun', 'Python', 55000, 'Chennai'),
('Saravanan', 'Java', 44000, 'Madurai'),
('Bharath', 'Testing', 69000, 'Trichy'),
('Prem', 'HR', 35000, 'Coimbatore'),
('Yogesh', 'Python', 32000, 'Chennai'),
('Kishore', 'Java', 85000, 'Trichy'),
('Raghu', 'Testing', 39000, 'Madurai'),
('Elango', 'HR', 52000, 'Chennai'),
('Vasanth', 'Python', 47000, 'Coimbatore'),
('Ranjith', 'Java', 61000, 'Chennai'),
('Siva', 'Testing', 28000, 'Trichy'),
('Jeeva', 'HR', 43000, 'Madurai'),
('Akash', 'Python', 90000, 'Trichy'),
('Naveen Kumar', 'Java', 36000, 'Chennai'),
('Rohit', 'Testing', 50000, 'Coimbatore'),
('Karthikeyan', 'HR', 31000, 'Trichy'),
('Abinesh', 'Python', 64000, 'Madurai'),
('Madhan', 'Java', 49000, 'Chennai');

 --Task 1
 
select empname,dept,salary from emp1 where
  dept in ('Python','Java') 
  and salary>=30000
  and city in ('Chennai','Trichy')
  order by salary desc;

--Task 2

select distinct  dept from emp1 where salary>=23000 and salary<=50000
   and city != 'Chennai' order by dept;

-- Task 3
select * from emp1 where dept='Python';

select avg(salary)avg_salary from emp1 where dept='Python';


--Task 4

select empname,dept,length(empname) len_name from emp1 where (empname LIKE 'A%' OR empname LIKE 'R%') and salary >=30000
order by len_name desc;

--task 5

select max(salary) max_salary,min(salary) min_salary from emp1 where dept in ('Java','Python') and city in ('Chennai','Trichy');


--task 6
select distinct city from emp1  where (empname like '%a%') and salary>=35000  order by city desc;