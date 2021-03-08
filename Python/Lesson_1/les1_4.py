raw_data = int(input("Введите максимальное число: "))

max_value = raw_data % 10
raw_data = raw_data // 10

while raw_data > 0:
    if raw_data % 10 > max_value:
        max_value = raw_data % 10
    raw_data = raw_data // 10

print(max_value )
