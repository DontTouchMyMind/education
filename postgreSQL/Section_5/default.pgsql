CREATE TABLE customer
(
    customer_id serial,
    full_name text,
    status char DEFAULT 'r', -- regularly по умолчанию

    CONSTRAINT PK_customer_customer_id PRIMARY KEY(customer_id),
    CONSTRAINT CHK_customer_status CHECK (status = 'r' OR status = 'p')

);

INSERT INTO customer (full_name)
VALUES
('name');

SELECT * FROM customer;

ALTER TABLE customer
ALTER COLUMN status SET DEFAULT 'r';