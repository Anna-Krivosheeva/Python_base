"""
Задание 2
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

print(f"Введите элементы списка через '-':\n")
my_list = input().split('-')
print(f"Вы ввели список:\n {my_list}")
tmp = 0
for i in range(int(len(my_list) / 2)):
    my_list[tmp], my_list[tmp + 1] = my_list[tmp + 1], my_list[tmp]
    tmp += 2
print(f"Значения соседних элементов списка изменены:\n {my_list}")