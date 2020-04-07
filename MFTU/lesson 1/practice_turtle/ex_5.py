# 10 nested squares
import turtle


def square(width):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)


turtle.shape('turtle')
y = 5
x = 0

for i in range(0, 25):
    x += y
    square(2 * x)
    turtle.penup()
    turtle.goto(-x, -x)
    turtle.pendown()
