CREATE OR REPLACE FUNCTION get_square(ab REAL, bc REAL, ac REAL) RETURNS REAL AS $$
DECLARE
    perimetr REAL;
BEGIN
    perimetr := (ab + bc + ac) / 2;
    RETURN sqrt(perimetr * (perimetr - ab) * (perimetr - bc) * (perimetr - ac));
END;
$$ LANGUAGE plpgsql;

SELECT get_square(6, 6, 6);


CREATE OR REPLACE FUNCTION calc_middle_price() RETURNS SETOF products AS $$
DECLARE
    avg_price REAL;
    low_price REAL;
    high_price REAL;
BEGIN
    SELECT avg(unit_price)
    INTO avg_price
    FROM products;

    low_price = avg_price * 0.75;
    high_price = avg_price * 1.25;

    RETURN QUERY
    SELECT * FROM products
    WHERE unit_price BETWEEN low_price AND high_price; 
END;
$$ LANGUAGE plpgsql;

SELECT * FROM calc_middle_price();