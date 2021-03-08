count_index_list_t = int(input("Введите размерность желаемого списка: "))
list_t = []
for i in range(0, count_index_list_t, 1):
    new_element = input("Введите элемент списка: ")
    list_t.append(new_element)

print(f"Начальный список: {list_t}")
for index in range(0, len(list_t), 2):
    temp = list_t[index]
    if index + 1 != len(list_t):
        list_t[index] = list_t[index + 1]
        list_t[index + 1] = temp

print(f"Конечный список:  {list_t}")