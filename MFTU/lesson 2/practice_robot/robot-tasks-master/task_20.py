#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    n = 0
    #move_right()
    while n != 6:
        for i in range(27):
            move_right()
            fill_cell()

        move_down()
        for i in range(27):
            fill_cell()
            move_left()
        move_down()
        n += 1
    move_right()


if __name__ == '__main__':
    run_tasks()
