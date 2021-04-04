/*
 * ЗАДАНИЕ №4
 * (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы
 * заданы в виде списка английских названий (may, august)
 *
 * Добавляемс столбец birthday_at и наполняем
 */

CREATE TABLE userss (
   ID INT PRIMARY KEY AUTO_INCREMENT,
   name varchar(20),
   created_at varchar(20) DEFAULT NULL,
   updated_at varchar(20) DEFAULT NULL
)

INSERT INTO userss VALUES (Null,"Jos", NULL, NULL);     -- заполнил поля
INSERT INTO userss VALUES (NULL,"Mentol", NULL, NULL);
INSERT INTO userss VALUES (NULL,"Meol", NULL, NULL);

UPDATE userss SET created_at = NOW() WHERE created_at IS NULL; -- обновил тип поле датетайм
UPDATE userss SET updated_at = NOW() WHERE updated_at IS NULL;

ALTER TABLE userss ADD COLUMN birthday_at DATETIME  -- добавил столбец birthday_at

UPDATE userss SET birthday_at = "1985-05-20" WHERE id=1;    -- заполнил поля birthday_at
UPDATE userss SET birthday_at = "1985-08-20" WHERE id=2;
UPDATE userss SET birthday_at = "1989-10-20" WHERE id=3;

SELECT
	name, birthday_at,
	CASE
		WHEN DATE_FORMAT(birthday_at, '%m') = 05 THEN 'may'
		WHEN DATE_FORMAT(birthday_at, '%m') = 08 THEN 'august'
	END AS mounth
FROM userss WHERE DATE_FORMAT(birthday_at, '%m') = 05 OR DATE_FORMAT(birthday_at, '%m') = 08;