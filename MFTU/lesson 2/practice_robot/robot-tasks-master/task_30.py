#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x = 0
    y = 0

    while not wall_is_on_the_right():
        move_right()
        x += 1
    move_left(x)
    while not wall_is_beneath():
        move_down()
        y += 1
    move_up(y)

    for j in range(y):
        e = 0
        for i in range(x):
            e += 1
            if e == j + 1 or e == (x + 1) - j:
                move_right()
                continue
            fill_cell()
            move_right()

        if j != 0:
            fill_cell()
        move_down()
        move_left(x)
    move_right()
    for i in range(x - 1):
        fill_cell()
        move_right()
    move_left(x)


if __name__ == '__main__':
    run_tasks()
