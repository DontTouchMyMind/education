CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100
WHITH LOCAL CHECK OPTION; -- Не позволит вставить в таблицу значение, обходящее фильтр!

SELECT *
FROM heavy_orders
ORDER BY freight;