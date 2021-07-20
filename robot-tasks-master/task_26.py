#!/usr/bin/python3

from pyrob.api import *


def cross():
    fill_cell()

    move_up()
    fill_cell()
    move_down()

    move_right()
    fill_cell()
    move_left()

    move_down()
    fill_cell()
    move_up()

    move_left()
    fill_cell()
    move_right()

@task(delay=0.02)
def task_2_4():


    for j in range(5):
        move_right()
        move_down()
        for i in range(10):
            cross()
            if i < 9:
                move_right(4)

        while True:
            if wall_is_on_the_left() == False:
                move_left()
            else:
                break
        move_up()

        if j <= 3:
            move_down(4)


if __name__ == '__main__':
    run_tasks()
