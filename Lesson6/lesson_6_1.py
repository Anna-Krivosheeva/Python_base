"""
Задание 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __color = None

    def running(self):
        print('Светофор:')

        self.__color = 'красный'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)

        self.__color = 'желтый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'зеленый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        while True:
            self.running()


traffic_light = TrafficLight()
print(traffic_light.running())