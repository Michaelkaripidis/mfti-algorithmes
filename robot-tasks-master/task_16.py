#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while True:
        if wall_is_above() == True:
            if wall_is_on_the_left() == True:
                while True:
                    if wall_is_on_the_right() == False:
                        move_right()
                    else:
                        break
            else:
                while True:
                    if wall_is_on_the_left() == False:
                        move_left()
                    else:
                        break
            break
        else:
            move_up()



if __name__ == '__main__':
    run_tasks()


