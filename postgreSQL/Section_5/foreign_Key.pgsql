CREATE TABLE publisher
(
    publisher_id int,
    publisher_name varchar(128) NOT NULL,
    adress text,

    CONSTRAINT PK_publisher_publisher_id PRIMARY KEY(publisher_id)

);

CREATE TABLE book
(
    book_id int,
    title text NOT NULL,
    isbn varchar(32) NOT NULL,
    publisher_id int,

    CONSTRAINT PK_book_book_id PRIMARY KEY(book_id)
)

INSERT INTO publisher
VALUES
(1, 'Everyman''s Library', 'NY'),
(2, 'Oxford University Press', 'NY'),
(3, 'Grand Central Publishing', 'Washinglton'),
(4, 'Simon & Shuster', 'Chicago');

---Без FK мы можем сослаться на издателя,
---которого не существует(Напр. '10')
INSERT INTO book
VALUES
(1, 'The Diary of a Young Girl', '0199535566', 10);

SELECT * FROM book;
TRUNCATE TABLE book;

ALTER TABLE book
ADD CONSTRAINT FK_book_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id);