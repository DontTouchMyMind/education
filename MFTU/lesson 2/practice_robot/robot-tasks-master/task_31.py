#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def left():
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                break
            move_left()

    def right():
        while not wall_is_on_the_right():
            if not wall_is_beneath():
                break
            move_right()

    while True:
        while wall_is_beneath():
            right()
            left()
            if wall_is_beneath():
                break
        if wall_is_beneath():
            break
        move_down()


if __name__ == '__main__':
    run_tasks()
