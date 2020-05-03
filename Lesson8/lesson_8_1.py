"""
Задание 1
Реализовать класс «Дата», функция-конструктор
которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Дата корректна {day} - {month} - {year}'
                else:
                    return f'Неправильно введен год {year} в дате {day} - {month} - {year}'
            else:
                return f'Неправильно введен месяц {month} в дате {day} - {month} - {year}'
        else:
            return f'Неправильно введен день {day} в дате {day} - {month} - {year}'

    def __str__(self):
        return f'{Date.extract(self.day_month_year)}'


today = Date('03 - 05 - 2020')
print(f'Преобразование элементов даты к числу:\n{today}')
print(Date.extract('23 - 13 - 2022'))
print(today.extract('23 - 02 - 2020'))
print('\nПроверка корректности данных:')
print(Date.valid(1, 5, 2022))
print(today.valid(34, 5, 2020))
print(Date.valid(10, 9, 1989))
