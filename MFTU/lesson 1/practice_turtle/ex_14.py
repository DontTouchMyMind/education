# Draw a star

import turtle as t

t.shape('turtle')
t.speed(1)


def star(number):
    global angle

    for i in range(number):
        t.left(180 - angle)
        t.forward(150)


n = 5
angle = 180 / n
t.left(36)
star(n)
