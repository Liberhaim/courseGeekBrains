/*
 * Задание №3
 * Выведите список товаров products и разделов catalogs, который соответствует товару.
 * (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name).
 * Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с
 * русскими названиями городов.
 */

DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  id SERIAL NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  from_ VARCHAR(255), -- eng
  to_ VARCHAR(255) -- eng
) ;


INSERT INTO `flights` (`from_`,`to_`)
	VALUES
  ('moscow', 'omsk'),
  ('novgorod', 'kazan'),
  ('irkutsk', 'moscow'),
  ('omsk', 'irkutsk'),
  ('moscow', 'kazan');

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  id SERIAL NOT NULL NOT NULL PRIMARY KEY AUTO_INCREMENT,
  label VARCHAR(255), -- eng
  name VARCHAR(255) -- RUS
) ;

INSERT INTO `cities` (`label`,`name`)
	VALUES
  ('moscow', 'Москва'),
  ('irkutsk', 'Иркутск'),
  ('novgorod', 'Новгород'),
  ('kazan', 'Казань'),
  ('omsk', 'Омск');


SELECT * FROM cities ;

SELECT  f.id, c1.name, c2.name
from flights f
         LEFT JOIN cities c1 on f.`from_` = c1.label
         LEFT JOIN cities c2 on f.`to_` = c2.label
ORDER BY f.id;