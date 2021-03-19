/*	ПЗ №2	*/

/*
 * Задание №2. Создайте базу данных example, разместите в ней таблицу users, 
 * состоящую из двух столбцов, числового id и строкового name. 
*/
-- создание базы данных example
create database example;
-- создание таблицы user
CREATE TABLE user (
  id SERIAL,
  name VARCHAR(255)
);
