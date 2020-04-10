# Draw a butterfly using circles

import turtle as t

t.shape('turtle')
t.speed(15)


def circle(radius):
    t.seth(90)
    for i in range(90):
        t.forward(radius)
        t.left(4)
    for i in range(90):
        t.forward(radius)
        t.right(4)


for i in range(10):
    circle(i)
