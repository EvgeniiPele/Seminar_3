SELECT * FROM lesson1.mobilephone;
-- Выведите название, производителя и цену для товаров, количество которых превышает 2
SELECT ProductName, Manufacturer, Price from lesson1.mobilephone
WHERE ProductCount > 2;

-- Выведите весь ассортимент товаров марки “Samsung”
SELECT ProductName, ProductCount, Price from lesson1.mobilephone
WHERE Manufacturer = 'Samsung';

-- С помощью регулярных выражений найти товары, в которых есть упоминание "Iphone"
SELECT ProductName, ProductCount, Price from lesson1.mobilephone
WHERE ProductName LIKE '%Iphone%';

-- С помощью регулярных выражений найти товары, в которых есть упоминание "Samsung"
SELECT ProductName, ProductCount, Price from lesson1.mobilephone
WHERE Manufacturer LIKE '%Samsung%';

-- С помощью регулярных выражений найти товары, в которых есть ЦИФРА "8"
SELECT ProductName, ProductCount, Price from lesson1.mobilephone
WHERE ProductName LIKE '%2%';