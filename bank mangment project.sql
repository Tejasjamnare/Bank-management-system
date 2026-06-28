CREATE DATABASE bank_system;
USE bank_system;

CREATE TABLE customers(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
account_no BIGINT UNIQUE,
name VARCHAR(100),
phone VARCHAR(15),
balance DECIMAL(10,2)
);
select * from customer 

