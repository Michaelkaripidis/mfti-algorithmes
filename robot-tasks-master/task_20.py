#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():

    for i in range(6):
        for j in range(27):
            move_right()
            fill_cell()
        move_down()
        for d in range(27):
            fill_cell()
            move_left()
        move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()


# while True:
#         if wall_is_on_the_right() == False:
#             move_right()
#         else:
#             move_down()
#             while True:
#                 if wall_is_on_the_left() == False:
#                     move_left()
#                 else:
#                     move_down()


# while True:
#     if wall_is_on_the_right() == False:
#         if cell_is_filled() == True:
#             fill_cell()
#         move_right()
#     else:
#         move_down()
#         while True:
#             if wall_is_on_the_left() == False:
#                 if cell_is_filled() == True:
#                     fill_cell()
#                 move_left()
#             else:
#                 move_down()
#                 break