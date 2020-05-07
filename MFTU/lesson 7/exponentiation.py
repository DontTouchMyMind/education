def classical_exp(a: float, n: int):
    """
    Classic method to calculate to exponentiation
    Classical calculation method before exponentiation
    :param a: type: float, number
    :param n: type: int, exponent
    :return: result
    """
    assert n >= 0, 'Exponent must be positive'
    if n == 0:
        return 1
    return classical_exp(a, n - 1) * a


def fast_exp(a: float, n: int):
    """
    Fast calculation method before exponentiation
    :param a:
    :param n:
    :return:
    """
    assert n >= 0, 'Exponent must be positive'
    if n == 0:
        return 1
    elif n % 2 == 1:  # odd number
        return fast_exp(a, n - 1) * a
    else:  # even number
        return fast_exp(a ** 2, n // 2)


if __name__ == '__main__':
    print(classical_exp(4, 2))
    print(classical_exp(4, 3))
    print(classical_exp(4, 4))

    print(fast_exp(4, 2))
    print(fast_exp(4, 3))
    print(fast_exp(4, 4))
