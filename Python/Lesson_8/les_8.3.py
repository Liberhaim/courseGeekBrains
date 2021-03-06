"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""


class Error:
    def __init__(self, _):
        self.my_list = []

    def input(self):
        while True:
            try:
                val = int(input('Введите значения: '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Введенный символ не является числом")
                input_user = input(f'Попробуете еще раз? Y/N ')

                if input_user == 'Y' or input_user == 'y':
                    print(try_except.input())
                elif input_user == 'N' or input_user == 'n':
                    return f'До свидания!'


try_except = Error(1)
print(try_except.input())
