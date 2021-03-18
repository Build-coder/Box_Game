from setup import *

# when mouse is clicked      
def mouse_click():
    if event.type == MOUSEBUTTONDOWN and event.button ==1:

        for box in boxes:

            # when cursor is ontop of box
            if box.rect.collidepoint(event.pos):

                box.clicked = True

                # coordinates when clicked
                mouse_x, mouse_y = event.pos

                """
                upper left corner of box are it's coordinates
                mouse coordinates are pointer tip
                difference is saved to later align box 
                to position user intended
                """
                box.offset_x = box.rect.x - mouse_x
                box.offset_y = box.rect.y - mouse_y



def mouse_drag():

    for box in boxes:

        # when mouse is clicked and moving
        if box.clicked and event.type == pygame.MOUSEMOTION:

            # coordinates while moving
            mouse_x, mouse_y = event.pos

            # align box to where user intended
            box.rect.x = mouse_x + box.offset_x
            box.rect.y = mouse_y + box.offset_y

            box.dragged = True


def mouse_unclicked():

    for box in boxes:

        if event.type == MOUSEBUTTONUP and event.button == 1:
            box.clicked = False

            check_overlap()


def add_box():
    # add a new box ?
    if event.type == ADD_BOX:

        # create new box 
        box = Box(display)

        # add it to sprite groups
        boxes.add(box)

def check_overlap():
    for box in boxes:
        if box.clicked and box.dragged:
            
            print('left corner x: ', box.left_corner_x)
            print('left corner y: ', box.left_corner_y)
            print('right corner x: ', box.right_corner_x)
            print('right corner y: ', box.right_corner_y)


def clear():
    if event.type == KEYDOWN:
        if event.key == K_r:

            boxes.empty()


# ways for user to quit game
def quit(running):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE or event.key == K_q:
            running = False
    elif event.type == QUIT:
        running = False

    return running

running = True

while running:

    # check if any events from queue are triggered
    for event in pygame.event.get():

        mouse_click()
        mouse_drag()
        mouse_unclicked()
        add_box()
        clear()
        running = quit(running)     

    screen.fill(display.white)                
    
    # only move touched boxes (others haven't been removed from belt)
    for box in boxes:
        if not box.clicked and not box.dragged:
            box.move()
        
        screen.blit(box.surf, box.rect)

    # display updated image
    pygame.display.flip()

    # ensure program maintains a rate of 30 frames per second
    clock.tick(30)





