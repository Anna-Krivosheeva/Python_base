"""
Задание 7

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + bi'

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = ComplexNumber(3, 5)
z_2 = ComplexNumber(1, -2)
print(f'Первое число: {z_1}')
print(f'Второе число: {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
