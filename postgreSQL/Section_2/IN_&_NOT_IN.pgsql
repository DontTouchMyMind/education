/*Выбрать всех клиентов из каких то стран*/
SELECT *
FROM customers
WHERE country = 'Mexico' OR country = 'Germany' OR country = 'USA' OR country = 'Canada';


SELECT *
FROM customers
WHERE country IN ('Mexico', 'Germany', 'USA', 'Canada');


SELECT *
FROM products
WHERE category_id IN (1, 3, 5, 7);

/*Выбрать всех заказчиков из стран, исключая
    определенный список стран*/
SELECT *
FROM customers
WHERE country NOT IN ('Mexico', 'Germany', 'USA', 'Canada');
