"""
Задание 4

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""

import random


class Car:
    is_police: bool

    def __init__(self, name: str, color: str, speed: float):
        self.speed = speed
        self.name = name
        self.color = color

    @property
    def go(self):
        print('Начало движения')
        return print(f'Марка {self.name}, цвет {self.color}')

    @property
    def show_speed(self):
        print(f'Cо скоростью {self.speed}км/ч')
        if self.speed > 60:
            tmp_s = self.speed - 60
            return 'Превышение скорости на ' + str(tmp_s) + 'км/ч'

    @property
    def turn(self):
        return print(f'Повернула налево')

    @property
    def stop(self):
        return print('Конец движения')

class PoliceCar(Car):
    is_police = True

    def __init__(self, name='ВАЗ 2110', color='Синий', speed=random.randint(40, 120)):
        self.speed = speed
        self.name = name
        self.color = color


class TownCar(Car):
    is_police = False

    def __init__(self, name="Mazda RX", color="Серый", speed=random.randint(30, 80)):
        self.speed = speed
        self.name = name
        self.color = color


class WorkCar(Car):

    def __init__(self, name='Газель', color='Зеленый', speed=random.randint(30, 100)):

        self.speed = speed
        self.name = name
        self.color = color


class SportCar(Car):
    is_police = False

    def __init__(self, name='Audi R8', color='белый', speed=random.randint(100, 300)):
        self.speed = speed
        self.name = name
        self.color = color


tc = TownCar()
pc = PoliceCar()
sc = SportCar()
wc = WorkCar()

print('__ПОЛИЦЕЙСКАЯ МАШИНА__')
print(f'{pc.go} {pc.show_speed} {pc.turn} {pc.stop}')

print('__ГОРОДСКАЯ МАШИНА__')
print(f'{tc.go} {tc.show_speed} {tc.turn} {tc.stop}')

print('__СПОРТИВНАЯ МАШИНА__')
print(f'{sc.go} {sc.show_speed} {sc.turn} {sc.stop}')

print('__РАБОЧАЯ МАШИНА__')
print(f'{wc.go} {wc.show_speed} {wc.turn} {wc.stop}')
