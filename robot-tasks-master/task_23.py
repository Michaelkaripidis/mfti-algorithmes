#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while True:
        if wall_is_above() == False:
            while True:
                if wall_is_above() == False:
                    move_up()
                    fill_cell()
                else:
                    while True:
                        if wall_is_beneath() == False:
                            move_down()
                        else:
                            break
                    break

        if wall_is_on_the_right() == False:
            move_right()
        else:
            while True:
                if wall_is_on_the_left() == False:
                    if (wall_is_above() == False) and (wall_is_beneath() == False):
                        break
                    else:
                        move_left()
                else:
                    break
            break

if __name__ == '__main__':
    run_tasks()

# Пройдет с лева направо и вернется обратно
# while True:
#     if wall_is_on_the_right() == False:
#         move_right()

# while True:
#         if wall_is_on_the_right() == False:
#             if wall_is_above() == False:
#                 while True:
#                     if wall_is_above() == False:
#                         fill_cell()
#                         move_up()
#                     else:
#                         while True:
#                             if wall_is_beneath():
#                                 move_down()
#                             else:
#                                 break
#             move_right()
#         else:
#             while True:
#                 if wall_is_on_the_left() == False:
#                     if (wall_is_above() == False) and (wall_is_beneath() == False):
#                        break
#                     else:
#                         move_left()
#                 else:
#                     break
#             break