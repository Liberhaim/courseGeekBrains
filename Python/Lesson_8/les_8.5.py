"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.my_store = []
        self._dict = {'Наименование': self.name, 'Количество': self.number}

    def mov(self):
        try:
            unit = input(f'Введите модель устрйства: ')
            unit_q = int(input(f'Введите количество: '))
            product = {'Модель устройства': unit, 'Количество': unit_q}
            self._dict.update(product)
            self.my_store.append(self._dict)
            print(f'Текущий список - {self.my_store}')
        except:
            return f'Неккоректно введены данные'


unit_1 = Warehouse('Xerox', 6)
print(unit_1.mov())
