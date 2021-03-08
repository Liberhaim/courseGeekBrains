a = int(input("Введите начальное значение: "))
b = int(input("Введите конечное значение: "))
day = 0
while True:
    if a <= b:
        a = a+(a*0.1)
        day += 1
        print(' {}-й день:{:.2f}'.format(day, a))
