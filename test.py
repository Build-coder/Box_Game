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

def check_overlap(event, box):

    '''
    comparing each box in group (obj) to the box
    that is selected by the user
    '''


    if event.type == KEYDOWN:
        if event.key == K_c:

            for obj in boxes:  

                l1_x = obj.rect.x
                l1_y = obj.rect.y

                r1_x = obj.rect.x + obj.width
                r1_y = obj.rect.y + obj.height

                l2_x = box.rect.x
                l2_y = box.rect.y

                r2_x = box.rect.x + box.width
                r2_y = box.rect.y + box.height

                if obj is box:
                    break

                '''
                1: upper left corner x
                2: upper left corner y

                3: upper right corner x
                4: upper right corner y

                5: lower left corner x
                6: lower left corner y

                7: lower right corner x
                8: lower right corner y
                '''
                if box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                and box.rect.y in range(obj.rect.y, obj.rect.y + obj.height) \
                or (box.rect.x + box.width) in range(obj.rect.x, obj.rect.x + obj.width) \
                and box.rect.y in range(obj.rect.y, obj.rect.y + obj.height) \
                or box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                and (box.rect.y + box.height) in range(obj.rect.y, obj.rect.y + obj.height) \
                or (box.rect.x + box.width) in range(obj.rect.x, obj.rect.x + obj.width) \
                and (box.rect.y + box.height) in range(obj.rect.y, obj.rect.y + obj.height) \
                or box.rect.x in range(obj.rect.x, obj.rect.x + obj.width) \
                and (box.rect.y + (box.height/2)) in range(obj.rect.y, obj.rect.y + obj.height):

                    print('overlap')
                    




