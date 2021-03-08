"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, *params = argv

rate_per_hour = 0
output_in_hours = 0
prize = 0

output_in_hours = float(params[output_in_hours])
rate_per_hour = float(params[rate_per_hour])
prize = float(params[prize])

result = (rate_per_hour * output_in_hours) + prize
print("Имя скрипта: ", script_name)
print(f'Заработная плата сотрудника = {result}')
