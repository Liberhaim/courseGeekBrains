"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC


# одежда
class Cloth(ABC):
    order_number = 1

    def __init__(self, name):
        self.name = name
        self.order_number = Cloth.order_number

    @property
    def get_material(self):
        return self.material_consumpt


# пальто
class Coat(Cloth):
    summary_material = 0.0

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.material_consumpt = round(self.size / 6.5 + 0.5, 2)
        Coat.summary_material += self.material_consumpt

    def __str__(self):
        return f'Заказ {self.order_number} - [{self.name}], Размер {self.size}, ' + \
               f'расход материалала {self.get_material}.'


class Suit(Cloth):
    summary_material = 0.0

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self.material_consumpt = round(2 * self.height + 0.3, 2)
        Suit.summary_material += self.material_consumpt

    def __str__(self):
        return f'Заказ {self.order_number} - [ {self.name} ], рост {self.height}, ' + \
               f'расход мат-ла {self.get_material}.'


list_ = [
    Coat('Пальто_1', size=48),
    Coat('Пальто_2', size=54),
    Coat('Пальто_3', size=58),
    Suit('Костюм_1', height=170),
    Suit('Костюм_2', height=185)
]

for el in list_:
    print(el)

print(f'Итого материала: пальто - {Coat.summary_material}, костюм - {Suit.summary_material}')
