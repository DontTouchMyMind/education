#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    x = 0
    y = 0
    while not wall_is_on_the_right():
        fill_cell()
        x += 1
        move_right()
    while not wall_is_beneath():
        fill_cell()
        y += 1
        move_down()
    fill_cell()
    while x != 0:
        move_left()
        for i in range(y):
            fill_cell()
            move_up()
        move_down(y)
        x -= 1


if __name__ == '__main__':
    run_tasks()
