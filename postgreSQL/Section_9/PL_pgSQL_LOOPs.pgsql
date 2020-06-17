CREATE OR REPLACE FUNCTION fib(n INT) RETURNS INT AS $$
DECLARE
    counter INT = 0;
    i INT = 0;
    j INT = 1;
BEGIN
    IF n < 1 THEN
        RETURN 0;
    END IF;

    WHILE counter < n
    LOOP
        counter = counter + 1;
        SELECT j, i + j INTO i, j;
    END LOOP;

    RETURN i;
END;
$$ LANGUAGE plpgsql;

SELECT fib(8);

CREATE OR REPLACE FUNCTION fib1(n INT) RETURNS INT AS $$
DECLARE
    counter INT = 0;
    i INT = 0;
    j INT = 1;
BEGIN
    IF n < 1 THEN
        RETURN 0;
    END IF;

    LOOP
        EXIT WHEN counter >= n;
        counter = counter + 1;
        SELECT j, i + j INTO i, j;
    END LOOP;

    RETURN i;
END;
$$ LANGUAGE plpgsql;
SELECT fib1(8);

DO $$
BEGIN
    FOR counter IN 1..5
    LOOP
        RAISE NOTICE 'counter: %', counter;
    END LOOP;

END $$;