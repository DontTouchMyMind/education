#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    x = 0
    move_right()
    while not wall_is_on_the_right():
        x += 1
        fill_cell()
        for i in range(x):
            if wall_is_on_the_right():
                break
            move_right()


if __name__ == '__main__':
    run_tasks()
