from turtle import *

shape('turtle')
speed(1)
size = 100


def koch_curve(length, n):
    """
    Function draws a koch curve
    :param length: simple line length
    :param n: recursion depth
    :return:
    """
    if n == 0:
        forward(length)
        return
    koch_curve(length, n - 1)
    left(60)
    koch_curve(length, n - 1)
    right(120)
    koch_curve(length, n - 1)
    left(60)
    koch_curve(length, n - 1)


def koch_snowflake(length, n):
    """
    Function draws a triangle of koch curve
    :param length: length for a koch curve
    :param n: recursion depth
    :return:
    """
    for i in range(3):
        koch_curve(length, n)
        right(120)


# koch_curve(size / 3, 5)
koch_snowflake(size / 3, 2)
