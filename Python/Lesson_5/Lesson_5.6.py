"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
"""

#         number = text.split()
# print(dict(text))
import re

dict_les = {}
count = 0
FILE_NAME_INPUT = "les_5.6_input.txt"


# преобразовать вычитаную строку в словарь
def cont(file):
    numm = 0
    number = content.split(":")
    num = re.findall(r'\d+', number[1])
    for el in num:
        numm += int(el)

    return {number[0]: numm}


# определить кол-во строк в файле
def line_file(text_name):
    with open(text_name, 'r', encoding='utf_8') as f:
        text = f.read()
    count = 0
    for _ in text:
        count += 1
    return text.count("\n") + 1


my_f = open(FILE_NAME_INPUT, "r", encoding="utf-8")

for el in range(line_file(FILE_NAME_INPUT)):
    content = my_f.readline()
    dict_les.update(cont(content))  # добавить словарь к словарю

my_f.close()

print(f' Полученный словарь имеет вид: {dict_les}')
