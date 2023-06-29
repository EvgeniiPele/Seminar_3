CREATE DATABASE IF NOT EXISTS lesson2;
USE lesson2;
CREATE TABLE sales
(id INT PRIMARY KEY AUTO_INCREMENT,
order_date DATE NOT NULL,
counnt_product INT NOT NULL
);

INSERT INTO sales (order_date, counnt_product)
VALUES
('2022-01-01', 156),
('2022-01-02', 180),
('2022-01-03', 21),
('2022-01-04', 124),
('2022-01-05', 341);

ALTER TABLE sales
ADD COLUMN Тип_заказа​ VARCHAR(30);

SELECT 
id, 
IF (counnt_product < 100, "Маленький заказ",
	IF (counnt_product > 300, "Большой заказ", "Средний заказ"))
	AS "Тип заказа"
FROM sales;

CREATE TABLE orders
(id INT PRIMARY KEY AUTO_INCREMENT,
employ_id VARCHAR(30) NOT NULL,
amount DOUBLE NOT NULL,
order_status VARCHAR(30) NOT NULL
);

INSERT INTO orders (employ_id, amount, order_status)
VALUES
("e03​", 15.00, "OPEN"),
("e01​", 25.50, "OPEN"),
("e05​", 100.70, "CLOSED"),
("e01", 22.18, "OPEN"),
("e04​", 9.50, "CANCELLED"),
("e01​", 25.50, "OPEN");

SELECT *,
	CASE
	WHEN order_status = "OPEN" THEN "Order is in open state"
    WHEN order_status = "CLOSED" THEN "Order is closed"
    WHEN order_status = "CANCELLED" THEN "Order is cancelled"
	END AS full_order_status
FROM orders;