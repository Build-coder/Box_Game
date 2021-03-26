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

def print_group(event):

    if event.type == KEYDOWN:
        if event.key == K_p:

            # count = 0

            for obj in boxes:
                print('obj ', obj.id, ': x: ', obj.rect.x, ': y: ', obj.rect.y, '\
                    : width: ', obj.width, ': height:', obj.height)
                    
                # count += 1

def check_corners(click_box, box):

    click_box_x_limit = click_box.rect.x + click_box.width
    click_box_y_limit = click_box.rect.y + click_box.height

    box_x_limit = box.rect.x + box.width
    box_y_limit = box.rect.y + box.height

    '''
    upper left corner
    upper right corner
    bottom left corner
    bottom right corner
    '''

    if click_box.rect.x in range(box.rect.x, box_x_limit) \
        and click_box.rect.y in range(box.rect.y, box_y_limit) \
        or click_box_x_limit in range(box.rect.x, box_x_limit) \
        and click_box.rect.y in range(box.rect.y, box_y_limit) \
        or click_box.rect.x in range(box.rect.x, box_y_limit) \
        and click_box_y_limit in range(box.rect.y, box_y_limit) \
        or click_box_x_limit in range(box.rect.x, box_x_limit) \
        and click_box_y_limit in range(box.rect.y, box_y_limit):
            return True
    else:
        return False

def check_overlap(event):

    '''
    only trigger overlap when box is ontop of first obj
    or vice versa. for some reason, my loop isn't iterating
    through each obj
    '''

    if event.type == KEYDOWN:
        if event.key == K_c:

            click_box = selected(event)

            box_x_list = range(click_box.rect.x, click_box.rect.x + click_box.width)
            box_y_list = range(click_box.rect.y, click_box.rect.y + click_box.width)

            for box in boxes:

                '''
                need a catch if user selected box is also
                current box in iteration

                i only want to compare different boxes, not
                the same box. obviously the same box will have
                the same coordinates
                '''
                if box is click_box:
                    continue

                else:

                    x_match = False
                    y_match = False

                    obj_x_list = range(box.rect.x, box.rect.x + box.width)
                    obj_y_list = range(box.rect.y, box.rect.y + box.height)

                    for box_x in box_x_list:
                        for obj_x in obj_x_list:
                            if box_x == obj_x:
                                x_match = True

                    for box_y in box_y_list:
                        for obj_y in obj_y_list:
                            if box_y == obj_y:
                                y_match = True

                    corners = check_corners(click_box, box)

                    if (x_match and y_match) or corners:
                        print('overlap')
                        return True

            return False


def selected(event):

    # if event.type == KEYDOWN:
    #     if event.key == K_s:
    for box in boxes:
        if box.clicked:
            # for testing
            if event.type == KEYDOWN:
                if event.key == K_s:
                    print('box ', box.id, ': x: ', box.rect.x, ': y: ', box.rect.y, '\
                    : width: ', box.width, ': height:', box.height)
            return box



