# Draw a spider with n legs
import turtle


def spider(corner_legs):
    turtle.forward(90)
    turtle.stamp()
    turtle.backward(90)
    turtle.left(-corner_legs)


turtle.shape('turtle')

number = 12
corner = 360 / number
for i in range(0, number):
    spider(corner)
    i += 1
