"""
Задание 6
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

product_list = []
i = 1
while True:
    product_list.append(
        (int(input("Введите номер товара: ")), dict({
            "название": str(input("Введите название: ")),
            "цена": float(input("Введите цену: ")),
            "количество": int(input("Введите количество: ")),
            "ЕИ": str(input("Введите единцы измерения: ")),
        }))
    )

    if input("Добавить еще один товар? (да/нет): ") == "нет":
        break
    i += 1

print(f"Список товаров:\n {product_list}")

ready_dict = dict({})
for product in product_list:
    for key, value in product[-1].items():
        if key in ready_dict:
            if value not in ready_dict.get(key):
                ready_dict.get(key).append(value)
        else:
            ready_dict.update({key: [value]})

print(f"Итоговые данные по товарам в разрезе характеристик\n: {ready_dict}")
