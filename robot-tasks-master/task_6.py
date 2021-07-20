#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    s = 0
    while True:
        if s == 0:
            if True == wall_is_beneath():
                s = 1

        if True == wall_is_beneath() or s == 0:
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()

# from pyrob.api import *
#
#
# @task
# def task_5_3():
#     # введем флажок s, по которому определяем началась уже стена (s = 1) или еще нет (s = 0)
#     s = 0
#     while True:
#         if s == 0:
#             if True == wall_is_beneath():
#                 # стена началась, переведем флажок в положение "началась"
#                 s = 1
#
#         # проверяем не только не закончилась ли стена wall_is_beneath(), но и началась ли она уже (s = 1)
#         if True == wall_is_beneath() or s == 0:
#             move_right()
#         else:
#             break
#
#
# if _name_ == '_main_':
#     run_tasks()