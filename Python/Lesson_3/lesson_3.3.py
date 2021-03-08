"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    temp_list = []
    temp = var1
    summ = 0
    temp_list.append(var1)
    temp_list.append(var2)
    temp_list.append(var3)
    index_last = 0
    for index in range(0, len(temp_list), 1):
        if temp_list[index] < temp:
            index_last = index
    for count in range(0, len(temp_list), 1):
        if index_last != count:
            summ += temp_list[count]
    print(f"Сумма наибольших 2-х чисел составляет: {summ}")


my_func(0, 9, 2)
