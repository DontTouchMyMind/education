CREATE OR REPLACE FUNCTION type_testing(money_val float8) RETURNS void AS
$$
BEGIN
    RAISE NOTICE 'ran %', money_val;
END;
$$ LANGUAGE plpgsql;

SELECT type_testing(0.5);
SELECT type_testing(0.5::float4);
SELECT type_testing(1); --неявное преобразование



CREATE OR REPLACE FUNCTION type_testing2(money_val int) RETURNS void AS
$$
BEGIN
    RAISE NOTICE 'ran %', money_val;
END;
$$ LANGUAGE plpgsql;
SELECT type_testing2(1);
SELECT type_testing2(0.5);
SELECT type_testing2(0.5::int);
SELECT type_testing2(CAST (0.5 AS int));


SELECT type_testing2('1.5');
SELECT type_testing2('1.5'::int);
SELECT type_testing2('1.5'::numeric::int);

SELECT type_testing2('1'::int);


SELECT 50! AS big_factorial;
SELECT CAST (50 AS bigint)! AS big_factorial;


/*неявные преобразования*/
SELECT 'abc' || 1;
SELECT '10' = 10; -- интерперетатор конвертирует строку в инт, в этом случае

