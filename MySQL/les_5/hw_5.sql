/*
 * ЗАДАНИЕ №5
 * (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса.
 * SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
 */

CREATE TABLE catalogs (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  name varchar(20)
);

INSERT INTO catalogs VALUES (1, 'Процессоры'),
							(2, 'Клавиатуры'),
							(3, 'Мыши'),
							(4, 'Материнки'),
							(5, 'Видеокарты');

SELECT
	*
FROM
	catalogs WHERE id IN (5, 1, 2)
ORDER BY CASE
	WHEN id = 5 THEN 0
	WHEN id = 1 THEN 1
	WHEN id = 2 THEN 2
END;
