#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    while True:
        if wall_is_above() == True and wall_is_beneath() == True:
            fill_cell()
        if wall_is_on_the_right() == False:
            move_right()
        else:
            break

if __name__ == '__main__':
    run_tasks()

# while True:
#         if True == wall_is_above() == wall_is_beneath():
#             fill_cell()
#         if False == wall_is_on_the_right():
#             move_right()
#         else:
#             break