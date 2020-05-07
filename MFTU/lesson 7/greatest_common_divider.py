# Алгоритмы Эвклида
#   Какой длины отрезок будет наибольше кратным "а" и
#   одновременно кратным "b" (наибольший общий делитель - Greatest Common Divider)


def gcd_1(a, b):
    """
    Функция вычисляет наибольший общий делитель.
    Function calculates greatest common divider
    :param a: first number
    :param b: second number
    :return: greatest common divider
    """
    if a == b:
        return a
    elif a > b:
        return gcd_1(a - b, b)
    else:
        return gcd_1(a, b - a)


def gcd_2(a, b):
    """
    Модифицированная функция вычисления наибольшего общего делителя
    Modified function to calculate the greatest common divider
    :param a: first number
    :param b: second number
    :return: greatest common divider
    """
    if b == 0:
        return a
    return gcd_2(b, a % b)


def gcd_3(a, b):
    """
    Simple gcd_2 function code
    :param a: first number
    :param b: second number
    :return: greatest common divider
    """
    return a if b == 0 else gcd_3(b, a % b)


if __name__ == '__main__':
    print(gcd_1(12, 4))
    print(gcd_2(12, 4))
    print(gcd_3(12, 4))
