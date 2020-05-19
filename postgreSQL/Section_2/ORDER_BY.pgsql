/**/
SELECT DISTINCT country
FROM customers
ORDER BY country ASC; 

SELECT DISTINCT country
FROM customers
ORDER BY country DESC; 



/*Сортировка по нескольким колонкам*/

SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city DESC;

SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city ASC;