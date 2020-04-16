#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def chest():
        move_right()
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
    move_left()

if __name__ == '__main__':
    run_tasks()
