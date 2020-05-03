"""
Задание 2
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dev_1 = int(input('Введите частное: '))
    div_2 = int(input('Введите делитель: '))
    if not div_2:
        raise DivisionZero('Деление на 0 запрещено')
    print(f'Результат {dev_1/div_2}')

except ValueError:
    print('Введены не числа')
except DivisionZero as error:
    print(error)
