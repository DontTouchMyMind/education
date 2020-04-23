from graphics import *

SIZE_X = 400
SIZE_Y = 400

window = GraphWin('Model', SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = Point(200, 200)
#  Вектор скорости
velocity = Point(1, -2)


def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point


def draw_circle(coords):
    circle = Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


while True:
    draw_circle(coords)
    coords = add(coords, velocity)
