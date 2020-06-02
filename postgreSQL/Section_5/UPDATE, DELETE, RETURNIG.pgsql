 SELECT * FROM author;

UPDATE author
SET full_name = 'Elias', rating = 5
WHERE autor_id = 12;

DELETE FROM author
WHERE rating IS NULL --AND full_name != 'John Silver'
RETURNING *