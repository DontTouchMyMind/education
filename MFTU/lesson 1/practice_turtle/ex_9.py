# Draw 10 nested regular polygons
import turtle as t
from math import *

t.shape('turtle')
t.speed(10)
radius = 10


def polygons(number, base_polygon):
    angle = 360 / number
    while number != 0:
        t.left(angle)
        t.forward(base_polygon)
        number -= 1


for i in range(3, 13):
    base = 2 * radius * sin(pi / i)
    angle_pos = (180 - 360 / i) / 2
    t.left(angle_pos)
    polygons(i, base)
    t.right(angle_pos)
    t.penup()
    t.forward(10)
    t.pendown()
    radius += 10
