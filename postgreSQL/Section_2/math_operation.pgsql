/*Задача:
    вывести товары и посчитать их полную стоимость*/

SELECT product_id, product_name, unit_price * units_in_stock
FROM products 