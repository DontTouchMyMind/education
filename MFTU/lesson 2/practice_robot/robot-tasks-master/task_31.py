#!/usr/bin/python3

from pyrob.api import *


@task  # (delay=0.01)
def task_8_30():
    x = 0
    counter = 0

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

    while not wall_is_on_the_left():
        x += 1
        move_left()
    move_right(x)
    while counter < 2:
        print(x, counter)
        while wall_is_beneath():
            left()
            right()
        move_down()


if __name__ == '__main__':
    run_tasks()
