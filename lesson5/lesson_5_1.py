"""
Задание 1
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f_name = input("Имя файла: ")
f = open(f_name, "w", encoding="utf-8")

while True:
    s = input()
    if s == "":
        break
    f.write(s + "\n")

f.close()