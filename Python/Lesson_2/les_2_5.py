list_rating = [70, 50, 30, 30, 20]
count_while = int(input("Количество добавляемых элементов: "))

while count_while:
    list_rating.append(int(input("Введите новый элемент рейтинга: ")))

    for index in range(len(list_rating) - 1, 0, -1):
        if list_rating[index] > list_rating[index - 1]:
            temp = list_rating[index - 1]
            list_rating[index - 1] = list_rating[index]
            list_rating[index] = temp
    count_while -= 1
print(list_rating)
