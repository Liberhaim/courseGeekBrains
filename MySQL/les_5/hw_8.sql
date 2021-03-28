/*
 * ЗАДАНИЕ №3.
 * (по желанию) Подсчитайте произведение чисел в столбце таблицы.
 */
DROP TABLE IF EXISTS x;
CREATE TABLE x (ID INT PRIMARY KEY AUTO_INCREMENT, value INT UNSIGNED NOT NULL);

INSERT INTO x VALUES (NULL, 1), (NULL, 2), (NULL, 3), (NULL, 4), (NULL, 5);

SELECT exp(sum(ln(value))) AS mux FROM x;