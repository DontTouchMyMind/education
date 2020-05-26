from turtle import *

shape('turtle')
speed(1)
size = 100


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


def koch_snowflake(length, n):
    for i in range(3):
        koch_curve(length, n)
        right(120)


# koch_curve(size / 3, 5)
koch_snowflake(size / 3, 2)
