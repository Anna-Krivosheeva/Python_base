#Задание 5

rev = float(input("Введите сумму выручки, руб.: "))
cost = float(input("Введите сумму издержек, руб.: "))
prof = rev - cost
if rev > cost:
    print("\nВы работаете с прибылью!")
    efficiency = rev / (rev - cost)
    print("Рентабельность фирмы: ", "{:.2f}".format(efficiency), "%", sep='')
    worker = int(input("\nВведите количество сотрудников: "))
    one_worker = prof / worker
    print("Прибыль на одного сотрудника составляет, руб.:", "{:.2f}".format(one_worker))
else:
    print("\nВы работаете с убытками!")
