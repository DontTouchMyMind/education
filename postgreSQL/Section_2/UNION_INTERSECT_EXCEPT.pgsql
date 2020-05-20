/*Вывести все страны, из которых наши заказчики и работники*/
SELECT country
FROM customers
UNION   --Объединение
SELECT country
FROM employees;

SELECT country
FROM customers
UNION ALL
SELECT country
FROM employees;

/*Выбрать те страны из которых также есть доставщики*/
SELECT country
FROM customers
INTERSECT   --Пересечение
SELECT country
FROM suppliers;

/*Найти те страны, в которых проживают customers, 
но не проживают suplier */
SELECT country
FROM customers
EXCEPT ALL
SELECT country
FROM suppliers;