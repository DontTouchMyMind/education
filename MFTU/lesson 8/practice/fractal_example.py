from turtle import *

def draw(l, n):
    """
    Function draws a simple fractal
    :param l: length
    :param n: recursion depth
    :return:
    """
    if n == 0:
        left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        forward(x)
        left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        right(135)

    forward(x)
    left(180)
    forward(l)

draw(400, 3)