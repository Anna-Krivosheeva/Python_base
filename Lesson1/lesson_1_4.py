n = int(input("Введите целое число: "))
# предполагаем, что последнняя цифра максимальная
m = n % 10
# убираем последнюю цифру из числа
n = n // 10
# извлекаем из числа последнюю цифру и сравниваем ее с ранее объявленной последней
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n//10
print("Максимальная цифра - ", m)
