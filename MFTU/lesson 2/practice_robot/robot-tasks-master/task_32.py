#!/usr/bin/python3

from pyrob.api import *

counter = 0


@task(delay=0.01)
def task_8_18():
    global counter

    def go_to_up():
        global counter
        y = 0
        while True:
            if cell_is_filled():
                counter += 1
                y += 1
            else:
                fill_cell()
                y += 1
            if wall_is_above():
                move_down(y)
                break
            move_up()

    while not wall_is_on_the_right():

        if wall_is_above() and wall_is_beneath():
            fill_cell()
        elif not wall_is_above():
            move_up()
            go_to_up()

        move_right()
    mov('ax', counter)
    counter = 0


if __name__ == '__main__':
    run_tasks()
