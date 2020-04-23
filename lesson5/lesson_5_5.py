"""
Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

nums_list = []

while True:
    try:
        num = float(input("Введите число: "))
        nums_list.append(str(num))
    except ValueError:
        print("Ввод чисел завершен")
        break

with open("file_5_5.txt", "w", encoding="utf-8") as file_write:
    print(f'{" ".join(nums_list)}', file=file_write)

with open("file_5_5.txt", "r", encoding="utf-8") as file_read:
    nums_list = file_read.readline().split()
    sum = 0
    for num in nums_list:
        sum += float(num)

print(f"Сумма чисел: {sum}")
