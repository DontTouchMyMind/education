/*Выбрать все записи из таблицы orders, но взять две колонки: 
идентификатор заказа и колонку, значение в которой мы рассчитываем 
как разницу между датой отгрузки и датой формирования заказа.*/
SELECT order_id, shipped_date - order_date
FROM orders