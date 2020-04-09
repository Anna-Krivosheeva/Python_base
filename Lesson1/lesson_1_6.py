a = 2
b = 4
day = 1
print(day, "-й день: ", "{:.2f}".format(a), "км", sep='')
while a < b:
    a *= 1.1
    day += 1
    print(day, "-й день: ", "{:.2f}".format(a), "км", sep='')
print("Ответ: на ", day, "-й день спортсмен достигнет результата не менее ", b, "км", sep='')
