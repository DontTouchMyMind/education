SELECT count(*) AS employees_count --Column name
FROM employees;

SELECT count(DISTINCT country) AS country
FROM employees;

SELECT category_id, sum(units_in_stock) AS units_in_stock
FROM products
GROUP BY category_id
ORDER BY units_in_stock DESC
LIMIT 5;


SELECT category_id, sum(unit_price * units_in_stock) AS total_price
FROM products
WHERE discontinued != 1
GROUP BY category_id
HAVING sum(unit_price * units_in_stock) > 5000
ORDER BY total_price DESC;