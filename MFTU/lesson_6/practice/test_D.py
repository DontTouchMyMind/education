# На вход программа получает набор чисел, заканчивающихся решеткой.
# Вам требуется найти: среднее, максимальное и минимальное число в последовательности.
# Так же нужно вывести cумму остатков от деления суммы троек на последнее число тройки
# (каждые 3 введеных числа образуют тройку).
#
# Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6
#       среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
#       максимум: 6
#       минимум: 1
# сумма остатков троек: (1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3
#
# Среднее выводить, округлив до трех знаков после запятой. Для этого нужно использовать функцию round(x, 3)
#
# Того ваша программа должна вывести: 3.5 6 1 3
#
# Подумайте, имеет ли смысл хранить всю последовательность.
#
# Формат входных данных
#   Последовательность чисел, заканчивающися '#'.
#   Все числа от 1 до 100. Количество чисел в последовательности кратно трем.
#   Одно число на строку.
#
# Формат выходных данных
#   Четыре числа, разделенных пробелом.

from sys import exit
numbers = []  # Empty list
len_list = 0  # List length
division = 0

while True:
    x = input()
    if x == '#':
        break
    elif len(x) > 3:
        numbers = x.split(sep=' ')
        tmp = int(numbers[0])
        for i in range(len(numbers) - 1):
            numbers[i] = int(numbers[i + 1])
        numbers[len(numbers) - 1] = tmp

        # for i in range(len(numbers)):
        #     print(numbers[i], end='')
        #     print(' ', end='')
        print(*numbers)
        exit()
    else:
        numbers.append(int(x))
        len_list += 1

mean = sum(numbers) / len_list  # Arithmetical mean value
max_value = max(numbers)
min_value = min(numbers)


def sum_of_triples():
    """
    Функция считает сумму первых трех чисел списка,
    удаляет их, затем делит сумму на последний элемент списка.
    Function calculates the sum of the first three numbers of the list,
    deletes them, then divides the sum by the last elements of the list.
    :return: Остаток от деления.
             Modulo
    """
    sum_var = 0
    divider = numbers[2]
    for i in range(3):
        sum_var += numbers.pop(0)
    result = sum_var % divider
    return result


while len_list != 0:
    division += sum_of_triples()
    len_list -= 3

print(round(mean, 3), max_value, min_value, division, sep=' ')
