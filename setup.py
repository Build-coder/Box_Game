import pygame
from classes import *

# init game
pygame.init()

# create a custom event for adding a new box
ADD_BOX = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_BOX, 5000)

# create screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setup the clock for a decent framerate
clock = pygame.time.Clock()

# instantiate box
box = Box(clicked=False, dragging=False)

# create groups to hold box sprites
boxes = pygame.sprite.Group()



