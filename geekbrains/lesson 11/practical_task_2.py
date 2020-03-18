# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
import sys
import random


my_list = [sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]


def max_list():
    print(max(my_list))


def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result


if __name__ == '__main__':
    max_list()
    get_random()
