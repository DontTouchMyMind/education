# Mathematical model of the pendulum

from graphics import *
from math import *

SIZE_X = 600
SIZE_Y = 600

window = GraphWin('pendulum', SIZE_X, SIZE_Y)
# Координата шарика
coord = Point(300, 500)
# Вектор скорости
# Эта величина, на которую изменяется координата шарика
velocity = Point(1, 10)
# Ускорение
# Величина, на которую изменяется вектор скорости
acceleration = Point(0, 0)

ball = Circle(coord, 10)
ball.setFill('red')
ball.draw(window)


def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point


def check_coord():
    if coord.x < 0 or coord.x > SIZE_X:
        velocity.x = - velocity.x
    if coord.y < 0 or coord.y > SIZE_Y:
        velocity.y = - velocity.y


while True:
    # Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    ball.move(velocity.x, velocity.y)

    coord = add(coord, velocity)
    # velocity = add(velocity, acceleration)
    check_coord()

    print(coord)
    time.sleep(0.02)
