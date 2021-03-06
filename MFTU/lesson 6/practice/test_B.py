# Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов,
# после чего дробная часть копеек отбрасывается.
# Каждый год сумма вклада становится больше.
# Надо определить, через сколько лет вклад составит не менее y рублей.
#
# Формат входных данных
#   Три натуральных числа: x, p, y.
#
# Формат выходных данных
#   Число лет, через сколько лет вклад составит не менее y рублей.


numbers = [int(n) for n in input().split()]

if numbers[0] == 0:
    print(int(0))
else:

    years = 0
    x = numbers[0]
    p = numbers[1]
    y = numbers[2]
    if x > y:
        print(int(0))
    else:
        while x < y:
            x *= 1 + p / 100
            x = int(100 * x) / 100
            years += 1
        print(years)
