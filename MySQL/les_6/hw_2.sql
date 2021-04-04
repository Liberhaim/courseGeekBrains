/*
 * Задача №2
 * Подсчитать общее количество лайков на посты, которые получили пользователи младше 18 лет.
*/

USE vk3;

SELECT COUNT(*) likesY18
FROM posts_likes
WHERE user_id
    in (
    SELECT user_id
    FROM profiles
    WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) < 18);