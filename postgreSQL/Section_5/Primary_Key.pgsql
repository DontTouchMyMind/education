CREATE TABLE chair
(
    chair_id serial PRIMARY KEY,
    chair_name varchar,
    dean varchar
);

INSERT INTO chair
VALUES (1, 'name', 'dean');

SELECT * FROM chair;

DROP TABLE chair;

CREATE TABLE chair
(
    chair_id serial UNIQUE,
    chair_name varchar,
    dean varchar
);
INSERT INTO chair
VALUES (1, 'name', 'dean');
INSERT INTO chair
VALUES (NULL, 'name2', 'dean2');

SELECT constraint_name
FROM information_schema.key_column_usage
WHERE table_name = 'chair'
    AND table_schema = 'public'
    AND column_name = 'chair_id';

ALTER TABLE chair
DROP CONSTRAINT chair_chair_id_key;

ALTER TABLE chair
ADD PRIMARY KEY(chair_id);