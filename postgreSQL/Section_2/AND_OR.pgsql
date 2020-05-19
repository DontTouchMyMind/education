/*Выбрать продукты цена которых больше 20, а также на складе больеше 40*/
SELECT *
FROM products
WHERE unit_price > 25 AND units_in_stock > 40;

/*Выбрать всех заказчиков, которые проживают в 
    Берлине, Лондоне и Сан-Франциско*/
SELECT *
FROM customers
WHERE city = 'Berlin' OR city = 'London' OR city = 'San Francisco';

/*Выбрать все заказы, отгруженные после 30.04.1998,
    и вес отгрузки меньше 75 или больше 150*/
SELECT *
FROM orders
WHERE shipped_date > '1998-04-30' AND (freight < 75 OR freight > 150);
