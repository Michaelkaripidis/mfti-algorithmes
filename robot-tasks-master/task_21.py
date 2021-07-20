#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n = 0

    for i in range(7):

        for j in range(14):

            if (j > 0) and (j <= n):
                fill_cell()

            move_right()

        if wall_is_beneath() == False:
            move_down()
            n = n + 1
        else:
            break

        for j in range(14):
            if (j > 0) and (j >= 14 - n):
                fill_cell()
            move_left()

        if wall_is_beneath() == False:
            move_down()
            n = n + 1
        else:
            break
    move_right()


if __name__ == '__main__':
    run_tasks()
