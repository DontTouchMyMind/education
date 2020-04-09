# Draw a square spiral
import turtle

turtle.shape('turtle')
x = 5
for i in range(20):
    turtle.forward(x * i)
    turtle.left(90)
