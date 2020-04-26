from graphics import *

SIZE_X = 800
SIZE_Y = 800

window = GraphWin('Model', SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = Point(400, 700)
#  Вектор скорости
velocity = Point(2, 0)
acceleration = Point(0, 0)


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


def sub(point_1, point_2):
    new_point = Point(point_1.x - point_2.x,
                      point_1.y - point_2.y)
    return new_point


def draw_ball(coords):
    """
    Функция отвечает за процесс отрисовки шарика
    :param coords: int (x,y) - координаты положения шарика
    """
    circle = Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def clear_window():
    """
    Функция очистки экрана
    """
    rectangle = Rectangle(Point(0, 0), Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)

    sun = Circle(Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def check_coords():
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = - velocity.x
    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = - velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    G = 2000

    return Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


while True:
    clear_window()
    draw_ball(coords)

    acceleration = update_acceleration(coords, Point(400, 400))

    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords()

    time.sleep(0.02)
