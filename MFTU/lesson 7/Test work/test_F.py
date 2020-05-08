# Необходимо найти НОД двух чисел, используя алгоритм Евклида.
#
# Формат входных данных
#   На вход подаются два натуральных числа, по числу в новой строке.
#
# Формат выходных данных
#   Одно число - НОД входных чисел.


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


n1 = int(input())
n2 = int(input())
print(gcd(n1, n2))
