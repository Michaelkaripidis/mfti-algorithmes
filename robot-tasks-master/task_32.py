#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    n = 0
    while True:
        if wall_is_on_the_right() == False:

            if wall_is_above() == False:
                while True:
                    if wall_is_above() == False:
                        move_up()

                        if cell_is_filled() == True:
                            n += 1

                        fill_cell()
                    else:
                        while True:
                            if wall_is_beneath() == False:
                                move_down()
                            else:
                                break
                        break

            if wall_is_above() == True:

                if cell_is_filled() == True:
                    n += 1

                fill_cell()

            move_right()

        else:
            mov('ax', n)
            break

if __name__ == '__main__':
    run_tasks()

    # while True:
    #     if wall_is_on_the_right() == False:
    #
    #         move_right()
    #     else:
    #         break

