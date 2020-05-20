/*Выбрать все записи где ship_region = NULL */
SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NULL;


SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NOT NULL;