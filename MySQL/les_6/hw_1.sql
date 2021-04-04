/*
 *  Задача.1
 *  Пусть задан некоторый пользователь.
 *  Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.
 *  (можете взять пользователя с любым id).
 */

USE vk3;

SELECT  (SELECT	from_user_id FROM messages WHERE to_user_id = users.id AND from_user_id IN (
	SELECT IF(from_user_id = users.id, to_user_id, from_user_id)
	FROM friend_requests
	WHERE request_type = 1 AND (from_user_id = users.id or to_user_id = users.id))
  	GROUP BY from_user_id
  	ORDER BY COUNT(from_user_id) DESC LIMIT 1) AS best_friend_id
FROM users WHERE id = 10; -- 10 > общался c 4
