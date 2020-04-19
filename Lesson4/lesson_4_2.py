"""
Задание 2
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random

list1 = random.sample(range(15, 525), 15)

print(f"Исходный список:\n {list1}")


def max_values_list(input_list: list):
    temp_list = []
    for key, val in enumerate(input_list):
        if key + 1 < len(input_list) and val < input_list[key + 1]:
            temp_list.append(input_list[key + 1])

    return temp_list


print(f"Элементы исходного списка, значения которых больше предыдущего элемента:"
      f"\n {max_values_list(list1)}")
