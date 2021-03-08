"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""


user_text = input("Введите текст через пробел: ")
user_text = user_text.split(" ")
# for index in range(0, len(new_str), 1):
# with open("python.txt", "w") as f_obj:
#     f_obj.write(user_text)
f = open("python.txt", "w")
f.writelines('%s\n' % i for i in user_text)
f.close()
