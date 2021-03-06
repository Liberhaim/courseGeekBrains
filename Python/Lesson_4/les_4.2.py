"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат:               [12, 44, 4, 10, 78, 123].
"""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def max(var1, var2):
    if var2 > var1:
        return var2


new_list = [max(my_list[el], my_list[el + 1]) for el in range(0, len(my_list) - 1, 1)]
new_list = [var for var in new_list if var]

print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
