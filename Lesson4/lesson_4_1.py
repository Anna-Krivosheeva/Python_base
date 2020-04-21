"""
Задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
import argparse

parser = argparse.ArgumentParser(description='Calculate salary')
parser.add_argument("--prod", type=float, required=True)
parser.add_argument("--hours", type=float, required=True)
parser.add_argument("--bonus", type=float, required=True)

args = parser.parse_args(argv[1:])


def salary(prod: float, hours: float, bonus: float):
    return prod * hours + bonus


print(f"Заработная плата: {salary(prod=args.prod, hours=args.hours, bonus=args.bonus)} руб")
