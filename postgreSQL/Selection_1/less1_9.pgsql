CREATE TABLE person
(
    person_id int PRIMARY KEY,
    first_name varchar(64) NOT NULL,
    second_name varchar(64) NOT NULL  
);
CREATE TABLE passport
(
    pasport_id int PRIMARY KEY,
    serial_number int NOT NULL,
    registration text NOT NULL,
    fk_passport_person int REFERENCES person(person_id)
)