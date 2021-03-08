"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

firm_list = {}
total = 0
with open("les_5.7_input.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        firm_name, _, firm_proceeds, firm_cost = line.split()
        firm_list[firm_name] = float(firm_proceeds) - float(firm_cost)

for val in firm_list.values():
    if val > 0:
        total = total + val
average = total / len(firm_list)
print(firm_list)

with open("les_5.7_input.json", "w", encoding="utf-8") as w_j:
    json_d = [firm_list, {'average_profit': average}]
    json.dump(json_d, w_j)
