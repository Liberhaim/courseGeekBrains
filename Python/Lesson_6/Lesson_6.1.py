"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на
ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:

    def __init__(self):
        self.trafficLight = {"Красный": 7, "Желтый": 2, "Зеленый": 1}
        self.__color = ""

    def run(self):
        for key, value in self.trafficLight.items():
            self.__color = key
            print(f"Текущий цвет светофора: {key}, осталось ждать: {value} секунд")
            time.sleep(value)


traffic = TrafficLight()
traffic.run()