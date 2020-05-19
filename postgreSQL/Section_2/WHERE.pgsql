/*Выбрать всех заказчиков из определенной страны*/
SELECT company_name, contact_name, phone, country
FROM customers
WHERE country = 'USA';


/*Выбрать все продукты, у которых цена больше 20*/
SELECT *
FROM products
WHERE unit_price > 20;

/*Посчитать кол-во продуктов, стоимостью болше 20*/
SELECT COUNT (*)
FROM products
WHERE unit_price > 20;

SELECT *
FROM products
WHERE discontinued = 1;

/*Выбрать тех заказчиков, которые не в Берлине*/
SELECT *
FROM customers
WHERE city != 'Berlin';

/*Выбрать все заказы после 1 марта 1998 года*/
SELECT *
FROM orders
WHERE order_date > '1998-03-01';

