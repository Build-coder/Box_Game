from setup import *

running = True

while running:
    
    # get events from queue
    for event in pygame.event.get():

        # ways for user to quit game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                running = False
        elif event.type == QUIT:
            running = False
        
        # when mouse is clicked
        elif event.type == MOUSEBUTTONDOWN:
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
                    offset_x = box.rect.x - mouse_x
                    offset_y = box.rect.y - mouse_y

        # when mouse is unclicked
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                box.dragging = False

        # when mouse is clicked and moving
        elif event.type == pygame.MOUSEMOTION:
            if box.dragging:

                # coordinates while moving
                mouse_x, mouse_y = event.pos

                # align box to where user intended
                box.rect.x = mouse_x + offset_x
                box.rect.y = mouse_y + offset_y
            
        # add a new box ?
        elif event.type == ADD_BOX:
            # create new box and add it to sprite groups
            box = Box(clicked=False, dragging=False)
            boxes.add(box)

    # moves box if it hasn't been clicked
    if box.clicked == False or box.dragging == True:
        box.move()

    boxes.update()
    screen.fill(WHITE)

    # draw all sprites
    for entity in boxes:
        screen.blit(entity.surf, entity.rect)

    # display updated image
    pygame.display.flip()

    # ensure program maintains a rate of 30 frames per second
    clock.tick(30)

