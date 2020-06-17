CREATE OR REPLACE FUNCTION convert_temp_to(temperature REAL, to_celsius bool DEFAULT TRUE) RETURNS REAL AS $$
DECLARE
    result_temp REAL;
BEGIN
    IF to_celsius THEN
        result_temp := (5.0/9.0)*(temperature - 32);
    ELSE
        result_temp := (9.0 * temperature + (32 * 5)) / 5.0;
    END IF;

    RETURN result_temp;
END;
$$ LANGUAGE plpgsql;

SELECT convert_temp_to(80);
SELECT convert_temp_to(26.6667, FALSE);



CREATE OR REPLACE FUNCTION get_season(month_number INT) RETURNS TEXT AS $$
DECLARE
    season TEXT;
BEGIN
    IF month_number BETWEEN 3 AND 5 THEN
        season := 'spring';
    ELSEIF month_number BETWEEN 6 AND 8 THEN
        season := 'summer';
    ELSEIF month_number BETWEEN 9 AND 11 THEN
        season := 'authom';
    ELSEIF month_number = 12 OR month_number BETWEEN 1 AND 2 THEN
        season := 'winter';
    ELSE
        season := 'error_month';
    END IF;

    RETURN season;
END;
$$ LANGUAGE plpgsql;
SELECT get_season(12);
