CREATE TABLE author 
(
    autor_id int,
    full_name text,
    rating float
);
INSERT INTO author
VALUES (10, 'John Silver', 4.5);

SELECT * FROM author;

INSERT INTO author(autor_id, full_name)
VALUES 
(11,'John Silver'),
(12,'name1'),
(13,'name2');

SELECT *
INTO best_author
FROM author
WHERE rating >= 4.5;

SELECT * FROM best_author;