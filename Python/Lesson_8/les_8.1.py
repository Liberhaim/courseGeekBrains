"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print('Дата: ', self.day, '.', self.month, '.', self.year)

    @staticmethod
    def is_valid(day, month, year):
        if day >= 1 or day <= 31:
            if month >= 1 or month <= 12:
                if year >= 1976 or year < 2036:
                    return print('Всё верно')
                else:
                    return print('Измените год')
            else:
                return print('Измените месяц')
        else:
            return print('Измените день')


data = Data(26, 12, 2020)
Data.is_valid(20, 11, 2020)
