from setup import *
from test import *

# # code to clear console
# import os

# def clear_console():
#     if event.type == KEYDOWN:
#         if event.key == K_c:
#             clear = lambda: os.system('clear')
#             clear()


# when mouse is clicked      
def mouse_click(event):
    if event.type == MOUSEBUTTONDOWN and event.button ==1:

        for box in boxes:

            # when cursor is ontop of box
            if box.rect.collidepoint(event.pos):

                box.clicked = True
                print('box clicked')

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

                print('reached end of mouse_click()')



def mouse_drag(event):

    for box in boxes:
        # when mouse is clicked and moving
        if box.clicked and event.type == pygame.MOUSEMOTION:

            box.dragged = True
            print('box dragged')

            # coordinates while moving
            mouse_x, mouse_y = event.pos

            '''
            check if boxes overlap
            if they do, don't allow user to place box
            '''
            # overlap = check_overlap(box)

            # align box to where user intended
            box.rect.x = mouse_x + box.offset_x
            box.rect.y = mouse_y + box.offset_y
                
            print('In mouse_drag()')
            print('x: ', box.rect.x, ', ', box.rect.y)
            print()

def mouse_unclicked(event):

    for box in boxes:

        if event.type == MOUSEBUTTONUP and event.button == 1:
            print('In mouse_unclicked()')
            print('x: ', box.rect.x, ', ', box.rect.y)
            print()
            box.clicked = False


# def check_coordinates(box):
    
#     # temp code for testing
#     if event.type == KEYDOWN:
#         if event.key == K_c:
#             pass

# def add_box():

#     # temp code for testing
#     if event.type == KEYDOWN:
#         if event.key == K_a:

#             box = Box(display)
#             boxes.add(box)

    # # add a new box ?
    # if event.type == ADD_BOX:

    #     # create new box 
    #     box = Box(display)

    #     # add it to sprite groups
    #     boxes.add(box)

def check_overlap(box):

    '''
    comparing each box in group (obj) to the box
    that is selected by the user
    '''
    for obj in boxes:    

        pass


# def clear_all():
#     if event.type == KEYDOWN:
#         if event.key == K_r:

#             boxes.empty()


# ways for user to quit game
def quit(event, running):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE or event.key == K_q:
            running = False
    elif event.type == QUIT:
        running = False

    return running

def main_prog():

    running = True

    while running:

        # check if any events from queue are triggered
        for event in pygame.event.get():

            mouse_click(event)
            mouse_drag(event)
            mouse_unclicked(event)
            # check_coordinates(box)
            add_box(event)
            clear_all(event)
            clear = clear_console(event)
            running = quit(event, running)     

        screen.fill(display.white)                
        
        # only move touched boxes (others haven't been removed from belt)
        for box in boxes:
            if not box.dragged:
                box.move(boxes)
            
            screen.blit(box.surf, box.rect)

        # display updated image
        pygame.display.flip()

        # ensure program maintains a rate of 30 frames per second
        clock.tick(30)


if __name__ == "__main__":

    from setup import *
    from test import *

    main_prog()

