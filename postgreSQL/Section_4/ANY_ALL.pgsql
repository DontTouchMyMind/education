/*Выбрать все уникальные компании заказчиков, 
которые делали заказов более чем на 40 ед. товара*/
SELECT DISTINCT company_name
FROM customers
JOIN orders USING(customer_id)
JOIN order_details USING(order_id)
WHERE quantity > 40;



SELECT DISTINCT company_name
FROM customers
WHERE customer_id = ANY(
    SELECT customer_id
    FROM orders
    JoIN order_details USING(order_id)
    WHERE quantity > 40
);


/*Выбрать кол-во продуктов, которых больше среднего по заказам*/
SELECT DISTINCT product_name, quantity
FROM products
JOIN order_details USING(product_id)
WHERE quantity > (
    SELECT avg(quantity)
    FROM order_details
)
ORDER BY quantity DESC;


/*Найти все продукты кол-во котрых больше среднего значения 
кол-ва заказанных товаров из групп
полученных по группированию product_id */
SELECT DISTINCT product_name, quantity
FROM products
JOIN order_details USING(product_id)
WHERE quantity > ALL(
    SELECT avg(quantity)
    FROM order_details
    GROUP BY product_id
)
ORDER BY quantity;