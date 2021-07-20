#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        fill_cell()
        if wall_is_on_the_right() == False:
            move_right()
        else:
            while True:
                if wall_is_on_the_left() == False:
                    move_left()
                else:
                    break
            if wall_is_beneath() == False:
                move_down()
            else:
                break

if __name__ == '__main__':
    run_tasks()
