CREATE OR REPLACE FUNCTION get_average_price_by_prod_categories()
RETURNS SETOF DOUBLE PRECISION AS $$
    SELECT avg(unit_price)
    FROM products
    GROUP BY category_id
$$ LANGUAGE SQL;

SELECT * FROM get_average_price_by_prod_categories() AS avarage_prices;


CREATE OR REPLACE FUNCTION get_avg_prices_by_prod_cats(OUT sum_price real, OUT avg_price float8)
RETURNS SETOF RECORD AS $$
    SELECT sum(unit_price), avg(unit_price)
    FROM products
    GROUP BY category_id
$$ LANGUAGE SQL; 

SELECT sum_price FROM get_avg_prices_by_prod_cats();
SELECT sum_price, avg_price FROM get_avg_prices_by_prod_cats();
SELECT sum_price AS sum_of, avg_price AS in_avg FROM get_avg_prices_by_prod_cats();

DROP FUNCTION get_avg_prices_by_prod_cats;

CREATE OR REPLACE FUNCTION get_avg_prices_by_prod_cats()
RETURNS SETOF RECORD AS $$
    SELECT sum(unit_price), avg(unit_price)
    FROM products
    GROUP BY category_id
$$ LANGUAGE SQL; 

-- НЕВЕРНЫЕ СЕЛЕКТЫ
SELECT sum_price FROM get_avg_prices_by_prod_cats();
SELECT sum_price, avg_price FROM get_avg_prices_by_prod_cats();
SELECT sum_price AS sum_of, avg_price AS in_avg FROM get_avg_prices_by_prod_cats();
SELECT * FROM get_avg_prices_by_prod_cats();
-- ВЕРНЫЙ СЕЛЕКТ
SELECT * FROM get_avg_prices_by_prod_cats() AS (sum_price real,avg_price float8);


CREATE OR REPLACE FUNCTION get_customers_by_count(customer_country varchar)
RETURNS TABLE(char_code char, company_name varchar) AS $$
    SELECT customer_id, company_name
    FROM customers
    WHERE country = customer_country
$$ LANGUAGE SQL;
SELECT * FROM get_customers_by_count('USA');
SELECT company_name FROM get_customers_by_count('USA');


DROP FUNCTION get_customers_by_count;
CREATE OR REPLACE FUNCTION get_customers_by_count(customer_country varchar)
RETURNS SETOF customers AS $$
    SELECT *
    FROM customers
    WHERE country = customer_country
$$ LANGUAGE SQL;
SELECT * FROM get_customers_by_count('USA');
SELECT company_name FROM get_customers_by_count('USA');
SELECT company_name AS company FROM get_customers_by_count('USA');