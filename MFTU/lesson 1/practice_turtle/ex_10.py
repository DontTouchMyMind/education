# Draw a flower using circles

import turtle as t

t.shape('turtle')
t.speed(15)


def circle():
    for i in range(180):
        t.forward(2)
        t.left(2)
    for i in range(180):
        t.forward(2)
        t.right(2)


for i in range(60, 240, 60):
    circle()
    t.seth(i)
