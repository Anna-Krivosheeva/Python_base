"""
Задание 2
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить
метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = None
    _width = None
    __mass_of_asphalt = float(input('Масса асфальта, кг: '))
    __weight_of_asphalt = float(input('Толщина асфальта, см: '))

    def __init__(self, width, length):

        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.__mass_of_asphalt * self.__weight_of_asphalt


road = Road(length=float(input("Введите длину дороги, м: ")), width=float(input("Введите ширину дороги, м: ")))
print(f'Масса асфальта, необходимого для покрытия дороги: {road.calculate()} т')