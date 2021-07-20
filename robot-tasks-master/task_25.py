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

@task
def task_2_2():
    move_right()
    move_down(2)
    for i in range(5):
        cross()

        if i == 4:
            move_left()
            move_up()
        else:
            move_right(4)

if __name__ == '__main__':
    run_tasks()
