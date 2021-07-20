#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_left() == True:
        while True:
            if wall_is_on_the_right() == True:
                break
            move_right()
    else:
        while True:
            if wall_is_on_the_left() == True:
                break
            move_left()

    if wall_is_above() == True:
        while True:
            if wall_is_beneath() == True:
                break
            move_down()
    else:
        while True:
            if wall_is_above() == True:
                break
            move_up()



if __name__ == '__main__':
    run_tasks()
