"""
Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
import os
import random

file = os.path.join(os.path.dirname(__file__), "file_5_5.txt")
file_numbers = [random.randint(1, 100) for _ in range(random.randint(10, 20))]

with open(file, "w", encoding="utf-8") as file_write:
    file_str = " ".join(map(str, file_numbers))
    file_write.write(file_str)

with open(file, "r", encoding="utf-8") as file_read:
    nums = map(float, file_read.read().split(" "))

print(f"Сумма чисел: {sum(nums)}")
