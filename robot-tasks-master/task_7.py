#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while True:
        if  True == wall_is_beneath():
            s = 0
            while True:
                if True == wall_is_beneath():
                    move_right()
                    s = s + 1
                else:
                    move_down(1)
                    for i in range(s):
                        move_left()
                    break
            break
        else:
            move_down()



if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


# @task
# def task_5_4():
#     while True:
#         if True == wall_is_beneath():
#             # введем Счетчик шагов вправо, чтобы запомнить сколько нужно будет сделать шагов обратно (влево)
#             s = 0
#             while True:
#                 if True == wall_is_beneath():
#                     move_right()
#                     s = s + 1
#                     # сделели еще шаг вправо, увеличиваем счетчик еще на 1
#                 else:
#                     move_down()
#                     # теперь цикл на строго определенное количесво шагов (s)
#                     for i in range(s):
#                         move_left()
#                     break
#             break
#
#         else:
#             move_down()
#
# if _name_ == '_main_':
#     run_tasks()