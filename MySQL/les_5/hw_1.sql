/*
 * ЗАДАНИЕ №1.
 * Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»
 *
 * 1.Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
 */

CREATE TABLE userss (
   ID INT PRIMARY KEY AUTO_INCREMENT,
   name varchar(20),
   created_at varchar(20) DEFAULT NULL,
   updated_at varchar(20) DEFAULT NULL
)

INSERT INTO userss VALUES (Null,"Jos", NULL, NULL);
INSERT INTO userss VALUES (NULL,"Mentol", NULL, NULL);
INSERT INTO userss VALUES (NULL,"Meol", NULL, NULL);

UPDATE userss SET created_at = NOW() WHERE created_at IS NULL;
UPDATE userss SET updated_at = NOW() WHERE updated_at IS NULL;

SELECT * FROM userss