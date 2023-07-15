CREATE DATABASE IF NOT EXISTS lesson5;
USE lesson5;
CREATE TABLE cars
(
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(45),
    cost INT
);

INSERT cars
VALUES
	(1, "Audi", 52642),
    (2, "Mercedes", 57127 ),
    (3, "Skoda", 9000 ),
    (4, "Volvo", 29000),
	(5, "Bentley", 350000),
    (6, "Citroen ", 21000 ), 
    (7, "Hummer", 41400), 
    (8, "Volkswagen ", 21600);
    
SELECT *
FROM cars;

-- Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов
CREATE OR REPLACE VIEW find_cars AS
SELECT * FROM cars
WHERE cost <= 25000
ORDER BY cost;

SELECT * FROM find_cars;

-- Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)
ALTER VIEW find_cars AS 
SELECT * FROM cars
WHERE cost <= 30000
ORDER BY cost;

SELECT * FROM find_cars;
-- Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди” (аналогично)
CREATE OR REPLACE VIEW skoda_audi AS
SELECT * FROM cars
WHERE name = "Audi" OR name = "Skoda";

SELECT * FROM skoda_audi;

--  Получить ранжированный список автомобилей по цене в порядке возрастания
SELECT 
DENSE_RANK() OVER W AS 'rank', name, cost
FROM cars
WINDOW W AS (ORDER BY cost);

-- Получить топ-3 самых дорогих автомобилей, а также их общую стоимость
SELECT 
DENSE_RANK() OVER W AS 'rank', 
SUM(cost) OVER W AS 'Sum',
name, cost
FROM cars
WINDOW W AS (ORDER BY cost DESC)
LIMIT 3;
-- Получить список автомобилей, у которых цена больше предыдущей цены
SELECT id, name, cost, 
LAG(cost) OVER() AS 'Lag'
FROM cars
WHERE 0 < ANY(SELECT cost - LAG(cost) OVER() FROM cars);