# Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе
# возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и
# печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции.
number = int(input('Enter your number'))


def func_1(input_val):
    if input_val != 13 and input_val in range(1, 101):
        input_val = input_val ** 2
    else:
        raise ValueError('error number')
    return input_val


result = func_1(number)
print(result)
