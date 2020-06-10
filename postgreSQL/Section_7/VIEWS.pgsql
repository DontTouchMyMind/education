SELECT * FROM orders;

CREATE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 50;

SELECT *
FROM heavy_orders
ORDER BY freight;


CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100;

INSERT INTO heavy_orders
VALUES(
    11078, 'VINET', 5, '2019-12-10', '2019-12-15', '2019-12-14',
    1, 120, 'Hanari Carnes', 'Rua do Paco', 'Bern', NULL, 3012, 'Switzerland'
);

SELECT *
FROM heavy_orders
ORDER BY order_id DESC;

SELECT min(freight)
FROM heavy_orders;

DELETE FROM heavy_orders
WHERE freight < 100.25;

