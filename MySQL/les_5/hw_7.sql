/*
 * ЗАДАНИЕ №2.
 * Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
 * Следует учесть, что необходимы дни недели текущего года, а не года рождения.
 */

SELECT
	name,
	birthday_at,
	concat(YEAR(now()), '-', substring(birthday_at, 6, 10)) AS data_birthday_at_in_year,
	dayname(concat(YEAR(now()), '-', substring(birthday_at, 6, 10))) AS week_day_birthday_at_year
FROM
	users
ORDER BY
	week_day_birthday_at_year;