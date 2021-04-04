/*
 * Задача №3
 * Определить, кто больше поставил лайков (всего) - мужчины или женщины?
 */

USE vk3;

SELECT
	(SELECT gender FROM profiles WHERE user_id = posts_likes.user_id) AS gender,
	COUNT(user_id) AS count FROM posts_likes
GROUP BY gender
ORDER BY count DESC;