#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
        while True:
            if wall_is_on_the_left() == False:
                if wall_is_above() == True:
                    move_left()
                else:
                    break
            else:
                break

        while True:
            if wall_is_above() == False:

                while True:
                    if wall_is_above() == False:
                        move_up()
                    else:
                        while True:
                            if wall_is_on_the_left() == False:
                                move_left()
                            else:
                                break
                        break
                break
            else:
                if wall_is_on_the_right() == False:
                    move_right()
                else:
                    break


if __name__ == '__main__':
    run_tasks()
