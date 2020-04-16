#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    x = 0
    while not wall_is_on_the_right():
        move_right()
        x += 1
        if not wall_is_above():
            y = 0
            while not wall_is_above():
                move_up()
                y += 1
                fill_cell()
            move_down(y)
    move_left(x)


if __name__ == '__main__':
    run_tasks()
