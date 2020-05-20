/*Выбрать всех содрудников с именами, заканчивающимися на n*/
SELECT product_name, unit_price
FROM products
WHERE discontinued != 1
ORDER BY unit_price DESC
LIMIT 10