#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    x = 0
    y = 0
    move_right()
    fill_cell()
    while True:
        if wall_is_on_the_right() == False:
            move_right()

            if x == y:
                fill_cell()
                y = 0
                x = x + 1
            else:
                y = y + 1
        else:
            break


if __name__ == '__main__':
    run_tasks()
