# Draw a flower using circles

import turtle as t

t.shape('turtle')
t.speed(15)


def circle(radius):
    for i in range(180):
        t.forward(radius)
        t.right(2)


def double_circle():
    for i in range(180):
        t.forward(2)
        t.left(2)
    for i in range(180):
        t.forward(2)
        t.right(2)


for i in range(60, 240, 60):
    double_circle()
    t.seth(i)
