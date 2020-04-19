"""
Задание 5
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, \
    cycle

print("Итератор, генерирующий целые числа:")
stop = 15
val = 0
for el in count(int(input("Введите число: "))):
    val += 1
    print(el)
    if val >= stop:
        val = 0
        break

print("Итератор, повторяющий элементы списка:")
my_list = {"самоизоляция", "скоро", "закончится", "!", 111}
for el in cycle(my_list):
    val += 1
    print(el)
    if val >= stop:
        val = 0
        break
