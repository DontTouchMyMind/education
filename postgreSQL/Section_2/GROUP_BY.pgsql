/*Посчитать кол-во заказов, вес которых превышает 50, 
сгрупировав по странам */
SELECT ship_country, COUNT (*)
FROM orders
WHERE freight > 50
GROUP BY ship_country
ORDER BY count (*) DESC;


/*Посчитать сумму всех продуктов в продаже, 
сгруппированных по категории id */
SELECT category_id, sum(units_in_stock)
FROM products
GROUP BY category_id
ORDER BY sum(units_in_stock) DESC
LIMIT 5;
