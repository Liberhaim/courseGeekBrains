"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


summ = 0
exit_code = ''
symbol_exit = 'q'
while exit_code != 'q':
    str_user = input("Для выхода нажмите клавишу 'q' или введите строку чисел разделенными пробелами: ")
    if str_user == 'q':
        break
    if symbol_exit in str_user:
        str_user = str_user.replace('q', '')
        exit_code = 'q'
    str_user = str_user.split(" ")
    for index in range(len(str_user)):
        summ += float(str_user[index])
    print(f"Сумма чисел равна: {summ}")
