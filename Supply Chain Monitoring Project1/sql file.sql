CREATE DATABASE supply_chain_db;
USE supply_chain_db;
CREATE TABLE suppliers (supplier_id INT PRIMARY KEY,supplier_name VARCHAR(100),
city VARCHAR(50),contact_email VARCHAR(100));
CREATE TABLE orders (order_id INT PRIMARY KEY,product_id INT,quantity INT,
order_date DATE,delivery_date DATE,order_status VARCHAR(30),FOREIGN KEY (product_id)
REFERENCES inventory(product_id));
INSERT INTO suppliers VALUES(101,'ABC Supplies','Chennai','abc@gmail.com');
SELECT * FROM suppliers;
UPDATE inventory SET stock_quantity = 50 WHERE product_id = 1;
DELETE FROM orders WHERE order_id = 10;
DELIMITER //
CREATE PROCEDURE check_reorder()
BEGIN
    SELECT
        product_id,
        product_name,
        stock_quantity
    FROM inventory
    WHERE stock_quantity < reorder_level;
END //
DELIMITER ;
CALL check_reorder();