/*Найти заказчиков и обслуживающих их заказы сотрудников таких, 
что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. 
Вывести компанию заказчика и ФИО сотрудника.

Для вывода ФИО одним столбцом можно использовать в секции 
SELECT функцию CONCAT(first_name, ' ', last_name), которая "склеивает" строчные аргументы.*/


SELECT customers.company_name, concat(first_name, ' ', last_name) AS employee
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)
JOIN shippers ON orders.ship_via = shippers.shipper_id
WHERE customers.city = 'London' AND employees.city = 'London' AND shippers.company_name = 'Speedy Express';


/*Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, 
которых в продаже менее 20 единиц. 
Вывести наименование продуктов, кол-во единиц в продаже, 
имя контакта поставщика и его телефонный номер*/
SELECT product_name, units_in_stock, suppliers.contact_name, suppliers.phone
FROM products
JOIN suppliers USING(supplier_id)
JOIN categories USING(category_id)
WHERE category_name IN ('Beverages', 'Seafood') AND discontinued != 1 AND units_in_stock <20
ORDER BY units_in_stock;


/* Найти заказчиков, не сделавших ни одного заказа. 
Вывести имя заказчика и order_id.*/

SELECT company_name, order_id
FROM customers
LEFT JOIN orders USING(customer_id)
WHERE ship_via IS NULL;



/*Переписать предыдущий запрос, использовав симметричный вид джойна 
(подсказка: речь о LEFT и RIGHT).*/

SELECT company_name, order_id
FROM orders
RIGHT JOIN customers USING(customer_id)
WHERE ship_via IS NULL;


