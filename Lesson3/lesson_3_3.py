"""
Задание 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def my_func(arg_1, arg_2, arg_3):
    print(f"Сумма двух наибольших аргументов равна: {arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])}")


my_func(
    int(input("Аргумент 1 - ")),
    int(input("Аргумент 2 - ")),
    int(input("Аргумент 3 - ")),
)