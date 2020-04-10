# Draw a spring. Use the function drawing an arc

import turtle as t

t.shape('turtle')
t.left(90)


def semicircle(radius):
    for i in range(90):
        t.forward(radius)
        t.right(2)


if __name__ == '__main__':
    t.penup()
    t.goto(-250, 0)
    t.pendown()
    for i in range(5):
        semicircle(2)
        semicircle(0.5)
