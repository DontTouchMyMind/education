/*Посчитать сумму на которую продается товаров в какой то категории*/
SELECT category_id, sum (unit_price * units_in_stock)
FROM products
WHERE discontinued != 1
GROUP BY category_id
HAVING sum (unit_price * units_in_stock) > 5000
ORDER BY sum (unit_price * units_in_stock) DESC