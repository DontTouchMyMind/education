/*Выбрать заказы, вес которых больше равен 20 и меньше равен 40*/
SELECT *
FROM orders
WHERE freight >= 20 AND freight <= 40;

SELECT COUNT (*)
FROM orders
WHERE freight BETWEEN 20 AND 40;

SELECT *
FROM orders
WHERE order_date BETWEEN '1998-03-30' AND '1998-04-03';