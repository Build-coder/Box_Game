# os is code to clear console
import os, pygame
from pygame.locals import *
from setup import *

def clear_console(event):
    if event.type == KEYDOWN:
        if event.key == K_c:
            clear = lambda: os.system('clear')
            clear()

def clear_all(event):
    if event.type == KEYDOWN:
        if event.key == K_r:

            boxes.empty()

def add_box(event):

    # temp code for testing
    if event.type == KEYDOWN:
        if event.key == K_a:

            box = Box(display)
            boxes.add(box)


