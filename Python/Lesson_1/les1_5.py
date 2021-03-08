revenue = int(input("Введите значение прибыли фирмы: "))
cost = int(input("Введите значение издержки фирмы: "))

if revenue > cost:
    print(" Фирма успешно работает")
    effect = revenue // cost
    print(" Рентабильность выручки: ", effect)
    number_staff = int(input("Введите колличество сотрудников фирмы: "))
    revenue_staff = revenue // number_staff
    print(" Прибыль фирмы в расчете на одного сотрудника: ", revenue_staff)
else:
    print(" Фирма несет убытки")