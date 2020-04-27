# Reformat code using method 'move'
from graphics import *

SIZE_X = 800
SIZE_Y = 800

coord = Point(400, 700)  # Ball initial position
velocity = Point(2, 0)  #
acceleration = Point(0, 0)

window = GraphWin('Solar system model', SIZE_X, SIZE_Y)

ball = Circle(coord, 10)
ball.setFill('green')
ball.draw(window)

sun = Circle(Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)


def check_coord():
    if coord.x < 0 or coord.x > SIZE_X:
        velocity.x = - velocity.x
    if coord.y < 0 or coord.y > SIZE_Y:
        velocity.y = - velocity.y


def add(point_1, point_2):
    """
    Функция возвращает значение координат в следующий момент времени
    :param point_1: int (x,y)
    :param point_2: int (x,y)
    :return: Сумма двух векторов
    """
    new_point = Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point


def update_coords(coord, velocity):
    return add(coord, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    G = 2000
    return Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


def sub(point_1, point_2):
    new_point = Point(point_1.x - point_2.x,
                      point_1.y - point_2.y)
    return new_point


while True:
    # Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    acceleration = update_acceleration(coord, Point(400, 400))

    coord = update_coords(coord, velocity)
    velocity = update_velocity(velocity, acceleration)

    ball.move(coord.x, coord.y)
    check_coord()
    time.sleep(0.02)
