"""
Задание 5
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.
"""

ratings = [35, 7, 5, 4, 3, 1]
print(ratings)

while True:
    num = input("Введите элемент рейтинга: ")

    try:
        num = abs(int(num))
    except ValueError as e:
        print('Ошибка ввода')
        continue

    if not ratings.count(num):
        if num > ratings[0]:
            ratings.insert(0, num)
        elif num < ratings[-1]:
            ratings.append(num)
        else:
            for key, value in enumerate(ratings):
                if num > value:
                    ratings.insert(key, num)
                    break
    else:
        new_index = ratings.index(num) + ratings.count(num)
        ratings.insert(new_index, num)

    print(f"Обновленный рейтинг:\n {ratings}")






