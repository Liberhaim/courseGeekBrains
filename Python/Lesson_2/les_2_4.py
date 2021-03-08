while True:
    str_t = input("Введите строку из нескольких слов разделенными пробелами ")
    if str_t.find(' ') <= 0:
        print("Ввели не корректную строку, повторите еще раз: ")
        continue
    else:
        break

new_str = str_t.split(' ')
for index in range(0, len(new_str), 1):
    if len(new_str[index]) > 10:
        print(f'Строка {index+1}: {new_str[index][:10]}')
    else:
        print(f'Строка {index+1}: {new_str[index]}')
