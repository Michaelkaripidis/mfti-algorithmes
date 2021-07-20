#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n = 0
    while True:
        if wall_is_on_the_right() == False:
            move_right()
            if cell_is_filled() == True:
                n = n + 1
            if n >= 5:
                break




if __name__ == '__main__':
    run_tasks()
