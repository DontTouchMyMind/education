from turtle import *

shape('turtle')
speed(1)
size = 50


def koch_curve(length, n):
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


koch_curve(size / 3, 5)
