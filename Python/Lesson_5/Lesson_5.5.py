"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("les_5.txt", "w") as f_obj:
    for el in range(10):
        f_obj.write(str(el) + " ")

with open("les_5.txt", "r") as f_obj:
    for text in f_obj:
        number = text.split()

number_summ = sum(map(int, number))
print(f'Сумма чиcел равна: {number_summ}')
