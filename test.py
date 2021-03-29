# os is code to clear console
import os, pygame
from pygame.locals import *
from setup import *

def clear_console(event):
    if event.type == KEYDOWN:
        if event.key == K_l:
            clear = lambda: os.system('clear')
            clear()

def remove_all(event):
    if event.type == KEYDOWN:
        if event.key == K_r:

            boxes.empty()

def add_box(event):

    if event.type == KEYDOWN:
        if event.key == K_a:

            box = Box(display)
            boxes.add(box)

def check_coordinates(event):

    if event.type == KEYDOWN:
        if event.key == K_f:
            print('x:', box.rect.x, ', y:', box.rect.y)

def print_group(event, box):

    if event.type == KEYDOWN:
        if event.key == K_p:

            count = 0

            for obj in boxes:
                print('obj ', count, ': x: ', obj.rect.x, ': y: ', obj.rect.y, '\
                    : width: ', obj.width, ': height:', obj.height)
                    
                count += 1

def check_overlap(event, box, obj):

    # if event.type == KEYDOWN:
    #     if event.key == K_c:


    if obj is box:
        return False

    else:

        x_match = False
        y_match = False

        box_x_list = range(box.rect.x, box.rect.x + box.width)
        box_y_list = range(box.rect.y, box.rect.y + box.width)

        obj_x_list = range(obj.rect.x, obj.rect.x + obj.width)
        obj_y_list = range(obj.rect.y, obj.rect.y + obj.height)
        

        for box_x in box_x_list:
            for obj_x in obj_x_list:
                if box_x == obj_x:
                    x_match = True

        for box_y in box_y_list:
            for obj_y in obj_y_list:
                if box_y == obj_y:
                    y_match = True

        if x_match and y_match:

            # print('overlap')
            return True

        else:
            # print('no-overlap')
            return False


                # box_y_list = range(box.rect.y, box.rect.y + box.height)

                # obj_x_list = range(obj.rect.x, obj.rect.x + obj.width)
                # obj_y_list = range(obj.rect.y, obj.rect.y + obj.height)

                # for obj in obj_x_list:
                #     for box in box_x_list:
                #         if obj == box:
                #             print('obj is in box x-axis')

                # for obj in obj_y_list:
                #     for box in box_y_list:
                #         if obj == box:
                #             print('obj is in box y-axis')


                # if box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                # and box.rect.y in range(obj.rect.y, obj.rect.y + obj.height) \
                # or (box.rect.x + box.width) in range(obj.rect.x, obj.rect.x + obj.width) \
                # and box.rect.y in range(obj.rect.y, obj.rect.y + obj.height) \
                # or box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                # and (box.rect.y + box.height) in range(obj.rect.y, obj.rect.y + obj.height) \
                # or (box.rect.x + box.width) in range(obj.rect.x, obj.rect.x + obj.width) \
                # and (box.rect.y + box.height) in range(obj.rect.y, obj.rect.y + obj.height) \
                # or box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                # and (box.rect.y + (box.height/2)) in range(obj.rect.y, obj.rect.y + obj.height):
                
                    # print('overlap')
                    




