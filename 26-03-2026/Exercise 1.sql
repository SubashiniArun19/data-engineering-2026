create database company_training;
use company_training;
create table employees(emp_id int primary key,
emp_name varchar(100),department varchar(50),
city varchar(50));
create table projects(project_id int primary key,
emp_id int,project_name varchar(100),
project_budget decimal(12,2),project_status varchar(50));
insert into employees values(1,'Rohan Mehta','IT','Hyderabad'),
(2,'Sneha Iyer','IT','Bangalore'),(3,'Kiran Patel','Finance','Mumbai'),
(4,'Ananya Das','HR',NULL),(5,'Rahul Sharma','IT','Delhi'),
(6,NULL,'Marketing','Chennai');
insert into projects value(101,1,'AI Chatbot',120000,'Active'),
(102,1,'ML Prediction',90000,'Active'),(103,2,'Data Warehouse',150000,'Active'),
(104,3,'Financial Dashboard',80000,'Completed'),(105,NULL,'Website Revamp',60000,'Pending'),
(106,8,'Mobile App',100000,'Active');
SELECT e.emp_name, p.project_name, p.project_budget
from employees e INNER JOIN projects p ON e.emp_id = p.emp_id;
SELECT e.emp_name, p.project_name, p.project_budget
from employees e left join projects p on e.emp_id = p.emp_id;
SELECT e.emp_name,p.project_id, p.project_name, p.project_budget,p.project_status
FROM employees e RIGHT JOIN projects p ON e.emp_id = p.emp_id;
select e.emp_id,e.emp_name, e.department,e.city,p.project_id,p.project_name, p.project_budget,p.project_status FROM employees e
left join projects p ON e.emp_id = p.emp_id union select  e.emp_id,e.emp_name, e.department,e.city,p.project_id,p.project_name, 
p.project_budget,p.project_status FROM employees e right join projects p ON e.emp_id = p.emp_id;
SELECT e.emp_name, p.project_name from employees e cross join projects p;
select  p.project_name from employees e join projects p ON e.emp_id = p.emp_id WHERE e.department = 'IT';
select  p.project_name from employees e join projects p ON e.emp_id = p.emp_id WHERE project_budget > 100000;
SELECT e.emp_name, p.project_name from  employees e
left join projects p ON e.emp_id = p.emp_id where e.city = 'Hyderabad';
SELECT e.emp_name, count(p.project_id) as total_projects FROM employees e
left join projects p ON e.emp_id = p.emp_id GROUP BY e.emp_name;
SELECT e.emp_name, sum(p.project_budget) as total_budget from employees e
left join projects p ON e.emp_id = p.emp_id GROUP BY e.emp_name;
Select e.department, avg(p.project_budget) as avg_budget from employees e
join projects p on e.emp_id = p.emp_id group by e.department;
Select e.department, count(p.project_id) as total_projects from employees e
join projects p on e.emp_id = p.emp_id group by e.department;
Select e.department, sum(p.project_budget) as total_budget from employees e
join projects p on e.emp_id = p.emp_id group by e.department;
select city, count(emp_id) AS total_employees from employees group by city;
SELECT e.emp_name, Count(p.project_id) as total_projects from employees e
join projects p ON e.emp_id = p.emp_id GROUP BY e.emp_name having count(p.project_id) > 1;
Select e.department, Sum(p.project_budget) AS total_budget from employees e
join projects p on e.emp_id = p.emp_id group by e.department
having sum(p.project_budget) > 150000;
select e.emp_name, sum(p.project_budget) as total_budget
from employees e join projects p on e.emp_id = p.emp_id
group by e.emp_name having sum(p.project_budget) > 100000;
select emp_name,e.department,sum(p.project_budget) as total_budget
from employees e join projects p  on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name, e.department having sum(p.project_budget) > 100000
order by total_budget desc;
