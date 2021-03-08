"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов
должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы
асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, weight, blade_thickness):
        thickness = 1
        mass_of_asphalt = self._length * self._width * thickness * blade_thickness * weight
        return mass_of_asphalt


road = Road(20, 5000)
print(f"Требуемая масса полотна составляет: {road.calculation(25, 5) / 1000}т")
