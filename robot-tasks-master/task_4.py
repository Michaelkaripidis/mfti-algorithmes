#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if False == wall_is_above():
        move_up()

    elif False == wall_is_on_the_right():
        move_right()

    elif False == wall_is_beneath():
        move_down()

    else:
        move_left()


if __name__ == '__main__':
    run_tasks()
