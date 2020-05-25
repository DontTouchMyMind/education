from sys import getrecursionlimit as get


def fac(n):
    """
    Function calculates factorial of the number
    :param n:
    :return:
    """
    global count
    if n == 0:
        return 1
    else:
        count += 1
        return n * fac(n-1)


count = 0
result = fac(5)
print(result)
print(get())
print(count)