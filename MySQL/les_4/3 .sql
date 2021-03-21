/*
 * Написать запрос для переименования названий типов медиа (колонка name в media_types) 
 * в осмысленные для полученного дампа с данными (например, в "фото", "видео", ...).
 * Долго мучался, не разобрался как сделать в списке
 */	
USE vk2; -- использовать бд

UPDATE media_types SET name = 'фото' WHERE id = 1;	
UPDATE media_types SET name = 'музыка' WHERE id = 2;
UPDATE media_types SET name = 'документ' WHERE id = 3;
UPDATE media_types SET name = 'видео' WHERE id = 4;

SELECT * FROM media_types; -- отобразить таблицу
