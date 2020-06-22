DROP FUNCTION IF EXISTS get_season;
CREATE OR REPLACE FUNCTION get_season(month_number INT) RETURNS TEXT AS $$
DECLARE
    season TEXT;
BEGIN

    IF month_number not BETWEEN 1 AND 12 THEN
        RAISE EXCEPTION 'Invalid month. You passed: (%)', month_number USING HINT='Allowed from 1 up to 12', ERRCODE = 12882;
    END IF;

    IF month_number BETWEEN 3 AND 5 THEN
        season := 'spring';
    ELSEIF month_number BETWEEN 6 AND 8 THEN
        season := 'summer';
    ELSEIF month_number BETWEEN 9 AND 11 THEN
        season := 'authom';
    ELSE
        season := 'winter';
    END IF;

    RETURN season;
END;
$$ LANGUAGE plpgsql;
SELECT get_season(12);
SELECT get_season(15);

CREATE OR REPLACE FUNCTION get_season_caller(month_number int) RETURNS text AS
$$
DECLARE
    err_ctx text;
    err_msg text;
    err_details text;
    err_code text;
BEGIN
    RETURN get_season(month_number);
EXCEPTION WHEN SQLSTATE '12882' THEN
    GET STACKED DIAGNOSTICS 
        err_ctx = PG_EXEPTION_CONTEXT,
        err_msg = MESSAGE_TEXT,
        err_details = PG_EXEPTION_DETAIL,
        err_code = RETURNED_SQLSTATE;
    RAISE INFO 'A problem. Nothing special.';
    RAISE INFO 'My custom handler: ';
    RAISE INFO 'Error msg:%', err_msg;
    RAISE INFO 'Error details:%', details;
    RAISE INFO 'Error code:%', err_code;
    RAISE INFO 'Error context:%', err_ctx;
    RETURN NULL;

END;
$$ LANGUAGE plpgsql;
SELECT get_season_caller(15);


CREATE OR REPLACE FUNCTION get_season_caller2(month_number int) RETURNS text AS
$$
BEGIN
    RETURN get_season(month_number);
EXCEPTION WHEN SQLSTATE '12882' THEN
    RAISE INFO 'My custom handler: ';
    RAISE INFO 'Error msg:%', SQLERRM;
    RAISE INFO 'Error details:%', SQLSTATE;
    RETURN NULL;

END;
$$ LANGUAGE plpgsql;
SELECT get_season_caller2(15);
