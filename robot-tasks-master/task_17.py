#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    # while True:
    #     if wall_is_above() == False:
    #         move_up()
    #         if cell_is_filled() == True:
    #             move_left()
    #             if cell_is_filled() == False:
    #                 move_right(2)
    #             break
    #     else:
    #         break
    while True:
        if wall_is_above() == False:
            move_up()
            if cell_is_filled() == True:
                if wall_is_on_the_left() == False:
                    move_left()
                    if cell_is_filled() == False:
                        move_right(2)
                else:
                    move_right()
                break
        else:
            break




if __name__ == '__main__':
    run_tasks()


while True:
       if wall_is_above() == False:
           move_up()
           if cell_is_filled() == True:
               if wall_is_on_the_left() == False:
                   move_left()
                   if cell_is_filled() == False:
                       move_right(2)
               else:
                   move_right()
               break
       else:
           break