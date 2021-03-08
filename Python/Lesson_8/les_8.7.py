"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class Operation:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def __add__(self, other):
        print('Сумма двух комплексных чисел')
        return print(f'c = {self.var1 + other.var1} + {self.var2 + other.var2}j')

    def __mul__(self, other):
        print('Умножение комплексных чисел')
        return print(f'c = {self.var1 - other.var1} + {self.var2 + other.var2}j')


op_1 = Operation(8, 9)
op_2 = Operation(4, 8)
op_1 + op_2
op_1 * op_2
