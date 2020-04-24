from graphics import *

SIZE_X = 400
SIZE_Y = 400

window = GraphWin('Model', SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = Point(200, 200)
#  Вектор скорости
velocity = Point(1, -2)
acceleration = Point(0, 0.1)


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


def check_coords():
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = - velocity.x
    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = - velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_coords(coords, velocity):
    return add(coords, velocity)


while True:
    clear_window()
    draw_ball(coords)

    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords()

    time.sleep(0.02)
