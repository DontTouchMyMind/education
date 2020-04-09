# Draw 10 nested regular polygons
import turtle
from math import *


def polygons(number, base):
    corner = 360 / number
    while number != 0:
        turtle.left(corner)
        turtle.forward(base)
        number -= 1


turtle.shape('turtle')
turtle.speed(1)
a = 50

for i in range(3, 13, 1):
    polygons(i, a)
    radius = a / abs(2 * sin(pi / i))
    turtle.penup()
    # turtle.setx(radius+10)
    turtle.pendown()
    print(f'polygon number{i} radius{radius}')
