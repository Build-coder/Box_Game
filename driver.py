from setup import *

running = True

# ways for user to quit game
def quit(running):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE or event.key == K_q:
            running = False
    elif event.type == QUIT:
        running = False
    
    return running

# when mouse is clicked      
def mouse_click(box):
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:

            # when cursor is ontop of box
            if box.rect.collidepoint(event.pos):
                box.dragging = True
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
    
    return box

def mouse_unclicked(box):

    if event.type == MOUSEBUTTONUP:
        if event.button == 1:
            box.dragging = False

    return box

def drag(box):

    # when mouse is clicked and moving
    if event.type == pygame.MOUSEMOTION and box.clicked == True:
        if box.dragging:

            # coordinates while moving
            mouse_x, mouse_y = event.pos

            # align box to where user intended
            box.rect.x = mouse_x + box.offset_x
            box.rect.y = mouse_y + box.offset_y

    return box

def add_box(box):
    # add a new box ?
    if event.type == ADD_BOX:

        # create new box 
        box = Box(display)

        # add it to sprite groups
        boxes.add(box)
            
        # insert node into linked list
        llist.insert_box(box)

    return box


while running:
    
    # get events from queue
    for event in pygame.event.get():

        running = quit(running)

        box = mouse_click(box)
        
        box = mouse_unclicked(box)

        box = drag(box)

        box = add_box(box)
                         
    # first box move if it hasn't been clicked
    if box.clicked == False:
        box.move()

    # prev box move if it hasn't been clicked
    if box.next is not None and box.next.clicked == False:
        box.next.move()

        if box.next.next is not None and box.next.next.clicked == False:
            box.next.next.move()


    boxes.update()
    screen.fill(display.white)

    # draw all sprites
    for entity in boxes:
        screen.blit(entity.surf, entity.rect)

    # display updated image
    pygame.display.flip()

    # ensure program maintains a rate of 30 frames per second
    clock.tick(30)

