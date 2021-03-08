# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
#
# product_analysis[product_param] = param_result
#
# for i in product_analysis:
#     print(i)
# for param in product_params:
#     print(param, product_analysis[param])
# {}  - словарь  [] - список () - кортежи
#
list_products = []
count_products = int(input("Введите количество товара: "))
analytics = {}
dict_products = {}
cnt = 0
for count in range(0, count_products, 1):
    print(f"{count + 1}-й товар")
    name = input(f"Введите - название: ")
    price = int(input(f"Введите - цена: "))
    quantity = int(input(f"Введите - количество: "))
    unit = input(f"Введите - еденица измерения: ")
    dict_list = {"название": name, "цена": price, "количество": quantity, "еденица измерения": unit}
    list_products.append(dict_list)

    dict_products.setdefault("название", [])
    dict_products["название"].append(name)
    dict_products.setdefault("цена", [])
    dict_products["цена"].append(price)
    dict_products.setdefault("количество", [])
    dict_products["количество"].append(quantity)
    dict_products.setdefault("еденица измерения", [])
    dict_products["еденица измерения"].append(unit)

# Cтруктура товара список кортежей
for i in list_products:
    print(f"{cnt + 1}  - {i}")
    cnt += 1
# Аналитика
for key, val in dict.items(dict_products):
    print(f"{key} {val}")

