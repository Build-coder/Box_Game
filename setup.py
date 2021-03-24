import pygame
from box_class import Box
# from linked_list import LinkedList
from display_class import Display 
from pygame.locals import *

# init game
pygame.init()

# create display 
display = Display()

# create screen
screen = pygame.display.set_mode((display.width, display.height)) 

# create a custom event for adding a new box
ADD_BOX = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_BOX, 5000)

# setup the clock for a decent framerate
clock = pygame.time.Clock()

# instantiate box
box = Box(display)

# create groups to hold box sprites
boxes = pygame.sprite.Group()

# add box to sprite groups 
boxes.add(box)






