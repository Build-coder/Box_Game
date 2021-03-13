import pygame, random
from pygame.locals import *

# define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create boxes
class Box(pygame.sprite.Sprite):
    def __init__(self, clicked, dragging):
        # inherit all properties of Sprite class
        super(Box, self).__init__()

        # create new dimensions for new box
        self.width = random.randint(25, 100)
        self.height = random.randint(25, 100)

        self.clicked = clicked
        self.dragging = dragging

        # create visual object
        self.surf = pygame.Surface((self.width, self.height))
        # make object white
        self.surf.set_colorkey((WHITE),RLEACCEL)
        # init rect (area under "surf" used for logic. 
        # surf is purely the visual)
        self.rect = self.surf.get_rect(
            center=(
                (SCREEN_WIDTH-self.surf.get_width())/2,
                (SCREEN_HEIGHT-self.surf.get_height())
            )
        )
        
    def move(self):
        # if box is not selected...
        if not self.dragging:
            self.rect.move_ip(0,-5)

            # if box reaches top...
            if self.rect.top <= 0:
                # set box to bottom again
                self.rect.top = 1000

            
            
            
  