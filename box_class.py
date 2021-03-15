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
        self.dragging = False

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

        self.next = None

        self.offset_x = 0
        self.offset_y = 0
        
    def move(self):
        # if box is not selected...
        if not self.dragging:
            self.rect.move_ip(0,-5)

            # if box reaches top...
            if self.rect.top <= 0:
                # set box to bottom again
                self.kill()

            
            
            
  