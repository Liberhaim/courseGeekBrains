"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""

import re
name = 'name'
salary = 'salary'
list_text = []
total_sum = 0

with open("5.3.txt", 'r', encoding='utf_8') as f:
    for text in f:
        name_worker, salary_worker = text.split()
        list_str = {name: name_worker, salary: int(salary_worker)}
        list_text.append(list_str)
        total_sum = total_sum + list_str[salary]

for el in list_text:
    if el[salary] < 20000:
        print(f"Сотрудник {el[name]} имеет оклад {el[salary]}")

    import re

    total_sum = 0
    max_num = 0
    max_index = 0
    with open("5.3.txt", 'r', encoding='utf_8') as f:
        text = f.read()
    minimum_salary = []

    text_list = re.sub('[а-яА-Я ]', '', text)

    text_list = text_list.split('\n')

    old_list = re.sub('[0-9 ]', '', text)
    old_list = old_list.split('\n')
    print(f'Изначально строка: {old_list}')
    max_num = text_list[0]
    for el in range(len(text_list)):
        if int(text_list[el]) < 20000:
            minimum_salary.append(el)
        total_sum = total_sum + int(text_list[el])
        average_income = total_sum / len(text_list)
    old_list.pop(max_index)
    print(f'Средний доход: {average_income} Минимальный доход имеют сотрудники {minimum_salary}')

    text = f.read()
minimum_salary = []

text_list = re.sub('[а-яА-Я ]', '', text)

text_list = text_list.split('\n')

old_list = re.sub('[0-9 ]', '', text)
old_list = old_list.split('\n')
print(f'Изначально строка: {old_list}')
max_num = text_list[0]
for el in range(len(text_list)):
    if int(text_list[el]) < 20000:
        minimum_salary.append(el)
    total_sum = total_sum + int(text_list[el])
    average_income = total_sum / len(text_list)
old_list.pop(max_index)
print(f'Средний доход: {average_income} Минимальный доход имеют сотрудники {minimum_salary}')
