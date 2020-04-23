"""
Задание 2
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_f = open("test_5_2.txt", "r", encoding="utf-8")
lines = my_f.readlines()

print(f"В файле {len(lines)} строк(и):")

num = 1
for string in lines:
    print(f"В строке {num} - {len(string.split())} слов(а)")
    num += 1
