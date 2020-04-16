#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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

    move_down(2)
    chest()
    for i in range(4):
        move_right(3)
        move_down()
        chest()
    move_left()


if __name__ == '__main__':
    run_tasks()
