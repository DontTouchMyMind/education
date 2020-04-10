# Draw a butterfly using circles

import turtle as t

t.shape('turtle')
t.speed(15)


def circle(x):
    t.seth(90)
    for i in range(90):
        t.forward(x)
        t.left(4)
    for i in range(90):
        t.forward(x)
        t.right(4)


for i in range(10):
    circle(i)
