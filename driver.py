from setup import *
from controller import *

# when mouse is clicked      
def mouse_click(event):
    if event.type == MOUSEBUTTONDOWN and event.button ==1:

        for box in boxes:

            # when cursor is ontop of box
            if box.rect.collidepoint(event.pos):

                box.clicked = True
                box.touched = True

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


def mouse_drag(event):

    for box in boxes:
        # when mouse is clicked and moving
        if box.clicked and event.type == pygame.MOUSEMOTION:

            # coordinates while moving
            mouse_x, mouse_y = event.pos
       
            # align box to where user intended
            box.rect.x = mouse_x + box.offset_x
            box.rect.y = mouse_y + box.offset_y


def mouse_unclicked(event):

    for box in boxes:

        if event.type == MOUSEBUTTONUP and event.button == 1:
            box.clicked = False

# automatically generates new box
# def add_box(event):

#     if event.type == ADD_BOX:

#         # create new box 
#         box = Box(display)

#         # add it to sprite groups
#         boxes.add(box)

# give each box in play an id
def set_id(event):
    count = 0
    
    for box in boxes:
        box.id = count
        count += 1

# ways for user to quit game
def quit(event, running):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE or event.key == K_q:
            running = False
    elif event.type == QUIT:
        running = False

    return running


def main(box):

    running = True

    while running:

        # check if any events from queue are triggered
        for event in pygame.event.get():

            set_id(event)
            mouse_click(event)
            mouse_drag(event)
            mouse_unclicked(event)
            check_overlap(event)
            print_group(event)
            add_box(event)
            selected(event)
            remove_all(event)
            clear = clear_console(event)
            running = quit(event, running)     

        screen.fill(display.white)                
        
        # only move touched boxes (others haven't been removed from belt)
        for box in boxes:
            if not box.touched:
                box.move(boxes)
            
            screen.blit(box.surf, box.rect)

        # display updated image
        pygame.display.flip()

        # ensure program maintains a rate of 30 frames per second
        clock.tick(30)


if __name__ == "__main__":

    from setup import *
    from controller import *

    main(box)

