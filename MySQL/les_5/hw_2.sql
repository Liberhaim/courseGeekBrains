/*
 * ЗАДАНИЕ №2.
 * Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались
 * значения в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
 *
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

ALTER TABLE userss
			CHANGE COLUMN `created_at` `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
 			CHANGE COLUMN `updated_at` `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;