import pygame, random
from pygame.locals import *

# create boxes
class Box(pygame.sprite.Sprite):
    def __init__(self, display):
        # inherit all properties of Sprite class
        super(Box, self).__init__()

        # create new dimensions for new box
        self.width = random.randint(25, 100)
        self.height = random.randint(25, 100)

        self.clicked = False
        self.dragged = False

        # create visual object
        self.surf = pygame.Surface((self.width, self.height))

        # make object black (display.white produces black somehow?)
        self.surf.set_colorkey((display.white),RLEACCEL)

        # init rect (area under "surf" used for logic. 
        # surf is purely the visual)
        self.rect = self.surf.get_rect(
            center=(
                (display.width-self.surf.get_width())/2,
                (display.height-self.surf.get_height())
            )
        )

        # used for linked list
        self.next = None

        # coordinates for corners of box
        self.left_corner_x = self.rect.x - self.width
        self.left_corner_y = self.rect.y - self.height

        self.right_corner_x = self.rect.x + self.width
        self.right_corner_y = self.rect.y + self.height

        # vars to correct object drag and drop
        self.offset_x = 0
        self.offset_y = 0

        
    def move(self):
        # box moves up
        self.rect.move_ip(0,-5)

        # if box reaches top...
        if self.rect.top <= 0:
            # box ceases to exist
            self.kill()

            
            
            
  