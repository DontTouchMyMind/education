from turtle import *

shape('turtle')
speed()

size = 50


def minkowski_curve(length, n):
    """
    Function draws a minkowski curve
    :param length: simple line length
    :param n: recursion depth
    :return:
    """
    if n == 0:
        forward(length)
        return
    minkowski_curve(length, n - 1)
    left(90)
    minkowski_curve(length, n - 1)
    right(90)
    minkowski_curve(length, n - 1)
    right(90)
    minkowski_curve(length, n - 1)
    minkowski_curve(length, n - 1)
    left(90)
    minkowski_curve(length, n - 1)
    left(90)
    minkowski_curve(length, n - 1)
    right(90)
    minkowski_curve(length, n - 1)


minkowski_curve(size / 4, 5)
