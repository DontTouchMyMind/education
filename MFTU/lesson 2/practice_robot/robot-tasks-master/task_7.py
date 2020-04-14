#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    count = 0
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        move_right()
        count += 1
    move_down()
    move_left(count)



if __name__ == '__main__':
    run_tasks()
