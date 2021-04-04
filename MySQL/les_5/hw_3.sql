/*
 * ЗАДАНИЕ №3
 * В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры:
 * 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом,
 * чтобы они выводились в порядке увеличения значения value. Однако нулевые запасы должны выводиться в конце, после
 * всех записей.
 */

CREATE TABLE storehouses_products (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  value INT UNSIGNED NOT NULL
);

SELECT * FROM storehouses_products

INSERT INTO storehouses_products VALUES (1, 0);
INSERT
	INTO storehouses_products
	VALUES (2, 2500),
		   (3, 0),
		   (4, 30),
		   (5, 500),
		   (6, 2500);

SELECT value FROM storehouses_products ORDER BY CASE WHEN value = 0 THEN 1 ELSE 0 END, value;