CREATE DATABASE capstone_sql;
USE capstone_sql;
CREATE TABLE students (student_id INT PRIMARY KEY,student_name VARCHAR(100),
city VARCHAR(50),age INT);
CREATE TABLE enrollments (enrollment_id INT PRIMARY KEY,student_id INT,
course_name VARCHAR(100),trainer VARCHAR(100),fee DECIMAL(10,2));
INSERT INTO students VALUES(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',NULL,21),(5,'Vikram Singh','Chennai',25),(6,NULL,'Delhi',22);
INSERT INTO enrollments VALUES(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),(105,NULL,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);
select s.student_name, e.course_name from students s
inner join enrollments e on s.student_id = e.student_id;
select s.student_name, e.course_name from students s
left join enrollments e on s.student_id = e.student_id;
select s.student_name, e.course_name from students s
right join enrollments e on s.student_id = e.student_id;
select s.student_id,s.student_name,s.city,s.age,e.enrollment_id, e.course_name,e.trainer,e.fee from students s
left join enrollments e on s.student_id = e.student_id union
select  s.student_id,s.student_name,s.city,s.age,e.enrollment_id, e.course_name,e.trainer,e.fee from students s
right join enrollments e on s.student_id = e.student_id;
select s.student_name, e.course_name from students s
cross join enrollments e on s.student_id = e.student_id;
select s.student_name, e.course_name from students s
join enrollments e on s.student_id = e.student_id where s.city='Hyderabad';
select course_name, fee from enrollments where fee > 6000;
select student_name, count(e.course_name) AS total_courses
from students s left join enrollments e on  s.student_id = e.student_id
group by s.student_name;
select student_name, sum(e.fee) AS total_fee
from students s  join enrollments e on  s.student_id = e.student_id
group by s.student_name;
select student_name, count(e.course_name) AS total_courses
from students s  join enrollments e on  s.student_id = e.student_id
group by s.student_name having count(e.course_name) > 1;
select trainer, sum(fee) AS total_fee from enrollments
group by trainer having sum(fee) > 10000;
select count(*) AS total_students from students
group by  city having count(*) > 1;
select  s.student_name,s.city,sum(e.fee) as total_fee_paid
from students s join enrollments e on s.student_id = e.student_id
group by s.student_name, s.city having sum(e.fee) > 5000
order by total_fee_paid desc;