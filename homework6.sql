REATE DATABASE lesson6;
USE lesson6;

-- Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов. Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '
delimiter //
CREATE FUNCTION proc1(sec INT)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE days INT DEFAULT 0;
DECLARE hours INT DEFAULT 0;
DECLARE minutes INT DEFAULT 0;
DECLARE result VARCHAR(50);
SET days = ROUND(sec / 86400);
SET sec = sec % 86400;
SET hours = ROUND(sec / 3600);
SET sec = sec % 3600;
SET minutes = ROUND(sec / 60);
SET sec = sec % 60;
SET result = CONCAT(days, 'days, ', hours, 'hours, ', minutes, 'minutes, ', sec, 'second');
RETURN result;
END //
delimiter ;

SELECT proc1(110000);

-- Создайте процедуру которая, выводит только четные числа от 1 до 10. Пример: 2,4,6,8,10

delimiter //
CREATE PROCEDURE even_numbers()
BEGIN
DECLARE ten INT DEFAULT 0;
CREATE TABLE write_number(ten INT);
WHILE ten <= 8 DO
SET ten = ten + 2;
INSERT INTO write_number VALUES(ten);
END WHILE;
SELECT * FROM write_number;
END //
delimiter ;

CALL even_numbers();