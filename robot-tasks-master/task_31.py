#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        if wall_is_beneath() == True:
            if wall_is_on_the_left() == True:
                break
            move_left()
        else:
            move_down()
            while  wall_is_beneath() == False:
                move_down()
            while True:
                if wall_is_on_the_right() == False:
                    move_right()
                    while wall_is_beneath() == False:
                        move_down()
                else:
                    break



if __name__ == '__main__':
    run_tasks()


# while True:
#         if wall_is_beneath() == True:
#             if wall_is_on_the_left() == True:
#                 break
#             else:
#                 move_left()
#         else:
#             move_down()
#
#             while wall_is_beneath() == False:
#                 move_down()
#
#             while True:
#                 if wall_is_on_the_right() == False:
#
#                     while wall_is_beneath() == False:
#                         move_down()
#
#                     move_right()

                else:
                    break