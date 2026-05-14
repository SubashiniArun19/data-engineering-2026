CREATE DATABASE customers_deliverydb;
USE customers_deliverydb;
CREATE TABLE customers (customer_id INT PRIMARY KEY,customer_name VARCHAR(100),city VARCHAR(50),phone VARCHAR(20));
CREATE TABLE orders (order_id INT PRIMARY KEY,customer_id INT,order_date DATE,expected_delivery DATE,actual_delivery DATE,
FOREIGN KEY (customer_id)REFERENCES customers(customer_id)ON DELETE CASCADE
);
CREATE TABLE delivery_status (status_id INT PRIMARY KEY,order_id INT,delivery_status VARCHAR(50),
issue_type VARCHAR(100),FOREIGN KEY (order_id)REFERENCES orders(order_id));
drop table delivery_status;
CREATE TABLE delivery_status (status_id INT PRIMARY KEY,order_id INT,delivery_status VARCHAR(50),
issue_type VARCHAR(100),FOREIGN KEY (order_id)REFERENCES orders(order_id)ON DELETE CASCADE);
INSERT INTO customers VALUES(101,'Arun','Chennai','9876543210');
INSERT INTO customers VALUES
(102,'Priya','Bangalore','9876543211'),
(103,'Karthik','Hyderabad','9876543212'),
(104,'Meena','Mumbai','9876543213'),
(105,'Rahul','Delhi','9876543214');
INSERT INTO orders VALUES
(1,101,'2026-05-01','2026-05-05','2026-05-07'),
(2,102,'2026-05-03','2026-05-08','2026-05-08'),
(3,101,'2026-05-04','2026-05-09','2026-05-11'),
(4,103,'2026-05-05','2026-05-10','2026-05-14'),
(5,104,'2026-05-06','2026-05-12','2026-05-12'),
(6,105,'2026-05-07','2026-05-13','2026-05-16');
INSERT INTO delivery_status VALUES
(1,1,'Delivered','Late Shipment'),
(2,2,'Delivered','No Issue'),
(3,3,'Delivered','Warehouse Delay'),
(4,4,'Delivered','Weather Delay'),
(5,5,'Delivered','No Issue'),
(6,6,'Delivered','Transport Delay');
SELECT * FROM orders;
SELECT * FROM orders WHERE customer_id = 101;
UPDATE orders SET actual_delivery = '2026-05-10' WHERE order_id = 2;
UPDATE orders SET expected_delivery = '2026-05-12' WHERE order_id = 3;
DELETE FROM orders WHERE customer_id = 102;
DELIMITER //
CREATE PROCEDURE get_delayed_deliveries(IN cust_id INT)
BEGIN
SELECT c.customer_id,c.customer_name,o.order_id,o.expected_delivery,o.actual_delivery,d.issue_type
FROM customers c JOIN orders o ON c.customer_id = o.customer_id
JOIN delivery_status d ON o.order_id = d.order_id
WHERE c.customer_id = cust_id AND o.actual_delivery > o.expected_delivery;
END //
DELIMITER ;
CALL get_delayed_deliveries(101);