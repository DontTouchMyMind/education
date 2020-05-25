def fibo(n):
    """
    Function calculates of fibonacci number
    :param n:
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n-1) + fibo(n-2)


print(fibo(7))