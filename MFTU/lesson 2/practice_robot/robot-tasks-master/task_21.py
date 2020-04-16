#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n = 0
    move_right()
    move_down()
    fill_cell()
    while n != 12:
        move_down()
        n += 1
        for i in range(n):
            fill_cell()
            move_right()
        fill_cell()
        move_left(n)
    move_down()


if __name__ == '__main__':
    run_tasks()
