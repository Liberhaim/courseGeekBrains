"""
    функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


def division_light(x, y):
    if y > 0:
        y *= -1
    result = abs(x) ** y

    print(f"result: division_light: {result}")


def division_hard(x, y):
    result = x
    if y > 0:
        y *= -1
    if y < 0:
        for ind in range(-1, y, -1):
            result *= x
            if ind == y + 1:
                result = 1 / result
    else:
        for ind in range(1, abs(y), 1):
            result *= x
    print(f"result: division_hard: {result}")


division_light(3, -5)
division_hard(3, -5)
