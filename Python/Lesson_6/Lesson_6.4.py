"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""

auto = []


class Car:
    abrib = "км/ч"

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Цвет машины: {self.color}, Марка авто: {self.name}, Полицейская: {self.is_police}')

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction='shop'):
        print(f"Машина напрaвляется: {direction}")

    def show_speed(self):
        print(f"Скорость составляет: {self.speed}{self.abrib}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._speed_limit = 60

    def show_speed(self):
        if self.speed > self._speed_limit:
            message = f'Ваша скорость составляет {self.speed}{self.abrib}, вы превысили лимит скорость в {self._speed_limit}{self.abrib}'
        else:
            message = f'Скорость составляет: {self.speed}{self.abrib}'

        print(message)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._speed_limit = 40

    def show_speed(self):
        if self.speed > self._speed_limit:
            message = f'Ваша скорость составляет {self.speed}{self.abrib}, вы превысили лимит скорость в {self._speed_limit}{self.abrib}'
        else:
            message = f'Скорость составляет: {self.speed}{self.abrib}'

        print(message)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


# auto.append(TownCar(speed=30, color='white', name='BMW'))
# auto.append(WorkCar(speed=70, color='grey', name='ISUZU'))
# auto.append(SportCar(speed=150, color='red', name='PORSCHE'))
# auto.append(PoliceCar(speed=100, color='black', name='FORD'))
#
# print(auto)
town_car = TownCar(61, "yellow", "Lifan")
town_car.go()
town_car.turn('up')
town_car.show_speed()
town_car.stop()

print("...")

sport_car = SportCar(100, "green", "Tesla")
sport_car.go()
sport_car.turn()
sport_car.show_speed()
sport_car.stop()

print("...")

work_car = WorkCar(50, "blue", "Ikarus")
work_car.go()
work_car.turn("right")
work_car.show_speed()
work_car.stop()

print("...")

polic = PoliceCar(80, "black", "Cardon")
polic.go()
polic.turn('down')
polic.show_speed()
polic.stop()
