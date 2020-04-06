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

for i in range(0, 11):
    x += y
    square(x)

    turtle.goto(10, 10)

    # turtle.penup()
    # turtle.left(180)
    # turtle.forward(y)
    # turtle.left(90)
    # turtle.forward(y)
    #
    # turtle.pendown()
