SELECT company_name
FROM suppliers
WHERE country IN (
    SELECT DISTINCT country
    FROM customers
)
ORDER BY company_name;

SELECT DISTINCT suppliers.company_name
FROM suppliers
JOIN customers USING(country)
ORDER BY company_name;


SELECT category_name, SUM (units_in_stock)
FROM products
JOIN categories USING(category_id)
GROUP BY category_name
ORDER BY sum(units_in_stock) DESC
LIMIT (
    SELECT min(product_id) + 4
    FROM products
);


SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock > (
    SELECT avg(units_in_stock)
    FROM products
)
ORDER BY units_in_stock;

/*Как выбрать компании и имена заказчиков, 
кот-е делали заказы весом от 50 до 100*/

SELECT company_name, contact_name
FROM customers
WHERE EXISTS (
    SELECT customer_id
    FROM orders
    WHERE customer_id = customers.customer_id
    AND freight BETWEEN 50 AND 100
);


SELECT company_name, contact_name
FROM customers
WHERE NOT EXISTS (
    SELECT customer_id
    FROM orders
    WHERE customer_id = customers.customer_id
    AND order_date BETWEEN '1995-02-01' AND '1995-02-15'
);


SELECT product_name
FROM products
WHERE NOT EXISTS(
    SELECT product_name
    FROM orders
    JOIN order_details USING(order_id)
    WHERE order_details.product_id = product_id
    AND order_date BETWEEN '1995-02-01' AND '1995-02-15'
);