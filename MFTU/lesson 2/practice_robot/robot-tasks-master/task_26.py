#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def chest():
        fill_cell()
        move_right()
        fill_cell()
        move_right()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_up()
        move_up()
        fill_cell()

    for n in range(5):
        move_down()
        chest()
        for i in range(9):
            move_right(3)
            move_down()
            chest()
        move_left(37)
        if n < 4:
            move_down(4)

    # move_left()


if __name__ == '__main__':
    run_tasks()
