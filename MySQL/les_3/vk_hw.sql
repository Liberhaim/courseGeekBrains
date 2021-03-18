DROP DATABASE IF EXISTS vk;

CREATE DATABASE vk;

USE vk;

SHOW tables;

/*
 * Многострочный комментарий
 */

CREATE TABLE users (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(145) NOT NULL, -- COMMENT "Имя",
  last_name VARCHAR(145) NOT NULL,
  email VARCHAR(145) NOT NULL,
  phone INT UNSIGNED NOT NULL,
  password_hash CHAR(65) DEFAULT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- NOW()
  UNIQUE INDEX email_unique (email),
  UNIQUE INDEX phone_unique (phone)
) ENGINE=InnoDB;


ALTER TABLE users ADD COLUMN passport_number VARCHAR(10);

ALTER TABLE users MODIFY COLUMN passport_number VARCHAR(20);

ALTER TABLE users RENAME COLUMN passport_number TO passport;

ALTER TABLE users ADD UNIQUE KEY passport_unique (passport);

ALTER TABLE users DROP INDEX passport_unique;

ALTER TABLE users DROP COLUMN passport;


SELECT * FROM users;

DESCRIBE users; -- описание таблицы

-- 1:1 связь
CREATE TABLE profiles (
  user_id BIGINT UNSIGNED NOT NULL,
  gender ENUM('f', 'm', 'x') NOT NULL, -- CHAR(1)
  birthday DATE NOT NULL,
  photo_id INT UNSIGNED,
  user_status VARCHAR(30),
  city VARCHAR(130),
  country VARCHAR(130),
  UNIQUE INDEX fk_profiles_users_to_idx (user_id),
  CONSTRAINT fk_profiles_users FOREIGN KEY (user_id) REFERENCES users (id) -- ON DELETE CASCADE
);

DESCRIBE profiles;


-- n:m

CREATE TABLE messages (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- 1
  from_user_id BIGINT UNSIGNED NOT NULL, -- id = 1, Вася
  to_user_id BIGINT UNSIGNED NOT NULL, -- id = 2, Петя
  txt TEXT NOT NULL, -- txt = ПРИВЕТ
  is_delivered BOOLEAN DEFAULT False,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- NOW()
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- ON UPDATE CURRENT_TIMESTAMP COMMENT "Время обновления строки",
  INDEX fk_messages_from_user_idx (from_user_id),
  INDEX fk_messages_to_user_idx (to_user_id),
  CONSTRAINT fk_messages_users_1 FOREIGN KEY (from_user_id) REFERENCES users (id),
  CONSTRAINT fk_messages_users_2 FOREIGN KEY (to_user_id) REFERENCES users (id)
);

DESCRIBE messages;


-- n:m

CREATE TABLE friend_requests (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- 1
  from_user_id BIGINT UNSIGNED NOT NULL, -- id = 1, Вася
  to_user_id BIGINT UNSIGNED NOT NULL, -- id = 2, Петя
  accepted BOOLEAN DEFAULT False,
  INDEX fk_friend_requests_from_user_idx (from_user_id),
  INDEX fk_friend_requests_to_user_idx (to_user_id),
  CONSTRAINT fk_friend_requests_users_1 FOREIGN KEY (from_user_id) REFERENCES users (id),
  CONSTRAINT fk_friend_requests_users_2 FOREIGN KEY (to_user_id) REFERENCES users (id)
);



CREATE TABLE communities (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(145) NOT NULL,
  description VARCHAR(245) DEFAULT NULL,
  admin_id BIGINT UNSIGNED NOT NULL,
  category ENUM('развлекательный', 'политический', 'обучающий', 'познавательный') NOT NULL, -- CHAR(1) / тематика сообщества /
  time_of_visit_per_day_of_the_user_in_the_community DATETIME NOT NULL,
  INDEX fk_communities_users_admin_idx (admin_id),
  CONSTRAINT fk_communities_users FOREIGN KEY (admin_id) REFERENCES users (id)
) ENGINE=InnoDB;


-- n:m

-- Таблица связи пользователей и сообществ
CREATE TABLE communities_users (
  community_id BIGINT UNSIGNED NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY (community_id, user_id),
  INDEX fk_communities_users_comm_idx (community_id),
  INDEX fk_communities_users_users_idx (user_id),
  CONSTRAINT fk_communities_users_comm FOREIGN KEY (community_id) REFERENCES communities (id),
  CONSTRAINT fk_communities_users_users FOREIGN KEY (user_id) REFERENCES users (id)
) ENGINE=InnoDB;


CREATE TABLE media_types (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(45) NOT NULL -- фото, музыка, документы
) ENGINE=InnoDB;


-- 1:n

CREATE TABLE media (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Картинка 1
  user_id BIGINT UNSIGNED NOT NULL,
  media_types_id INT UNSIGNED NOT NULL, -- фото
  file_name VARCHAR(245) DEFAULT NULL COMMENT '/files/folder/img.png',
  file_size BIGINT DEFAULT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX fk_media_media_types_idx (media_types_id),
  INDEX fk_media_users_idx (user_id),
  CONSTRAINT fk_media_media_types FOREIGN KEY (media_types_id) REFERENCES media_types (id),
  CONSTRAINT fk_media_users FOREIGN KEY (user_id) REFERENCES users (id)
);


CREATE TABLE bonus_types (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name_bonus varchar(45) NOT NULL -- ('финансовый', 'социальный', 'культурный', 'наказание')
--  bonus_types_name ENUM('финансовый', 'социальный', 'культурный', 'наказание') NOT NULL,
)ENGINE=InnoDB;

/*
 * ИДЕАЛЛОГИЯ. Рейтинг нужен чтобы вытенуть его из - зависимости социльныйх сетей (которые тормозят развитие человека), стимулировать к развитию, понять его социальную значимость в обществе,
 * поощьрять правильные поступки в назидание его "неудачных сверсников". АЛЯ одна серия из сериал Черное зеркало, но не совсем то =)  
 */
  /*
   * Расчитывается из time_of_visit_per_week_of_the_user_in_the_community and category_id
   * проведенного времени в сообществе за неделю, учитывая, category_id, где наивысший рейтинг дается за правильный контент c учетом рейтинг за прошлую неделю! 
   * при положительном рейтинге получает некий бонус "который все хотят"
   */ 
CREATE TABLE rating (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- 1
  user_id BIGINT UNSIGNED NOT NULL,
  bonus_types_id INT UNSIGNED NOT NULL, -- не связывает с bonus_types 
  category_id ENUM('развлекательный', 'политический', 'обучающий', 'познавательный') NOT NULL, -- CHAR(1) / тематика сообщества
  total_time_week_for_user_id_current_week DATETIME NOT NULL, -- проведенное время в соообществе за неделю 24ч * 7 дней / на общее время
  calculation_rating_for_user_id_last_week INT UNSIGNED NOT NULL, -- рейтинг за прошлые 7 дней
  INDEX fk_rating_bonus_types_idx (bonus_types_id),
  INDEX fk_rating_users_idx (user_id),
  -- CONSTRAINT fk_rating_bonus_types FOREIGN KEY (bonus_types_id) REFERENCES bonus_types (id), -- из за того что не связывает, закоментировал строчку тк. эта строка не давала создать таблицу
  CONSTRAINT fk_rating_users FOREIGN KEY (user_id) REFERENCES users (id)
);

SELECT * FROM bonus_types;

/*
CREATE TABLE black_list (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- 1
  user_id BIGINT UNSIGNED NOT NULL,
  list_user_id BIGINT UNSIGNED NOT NULL,                -- список людей игнор
  calculation_rating_for_user_id INT UNSIGNED NOT NULL,	-- подсчитаный рейтинг юзера из таблицы рейтинг //-- низкий рейтинг исползуется в качстве защиты как антиспам.
  INDEX list_user_id_idx (list_user_id), 
  CONSTRAINT fk_messages_users_1 FOREIGN KEY (list_user_id) REFERENCES users (id),
  CONSTRAINT fk_black_list_rating FOREIGN KEY (calculation_rating_for_user_id) REFERENCES rating (calculation_rating_for_user_id_last_week), 
  CONSTRAINT fk_black_list_users FOREIGN KEY (user_id) REFERENCES users (id)
);

*/
