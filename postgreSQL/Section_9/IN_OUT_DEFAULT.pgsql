CREATE OR REPLACE FUNCTION get_product_price_by_name(prod_name varchar) RETURNS REAL AS $$
    SELECT unit_price
    FROM products
    WHERE product_name = prod_name
$$ LANGUAGE SQL;

SELECT get_product_price_by_name('Chocolade') AS price;


CREATE OR REPLACE FUNCTION get_price_boundaries(OUT max_price REAL, OUT min_price REAL) AS $$
    SELECT max(unit_price), min(unit_price)
    FROM products
$$ LANGUAGE SQL;

SELECT get_price_boundaries();
SELECT * FROM get_price_boundaries();


CREATE OR REPLACE FUNCTION get_price_boundaries_by_discont(IN is_discontinued int DEFAULT 1 , OUT max_price REAL, OUT min_price REAL) AS $$
    SELECT max(unit_price), min(unit_price)
    FROM products
    WHERE discontinued = is_discontinued
$$ LANGUAGE SQL;

SELECT get_price_boundaries_by_discont();
SELECT * FROM get_price_boundaries_by_discont();
SELECT * FROM get_price_boundaries_by_discont(1);
SELECT * FROM get_price_boundaries_by_discont(0);