import pygame

def __backButton(surface):

    clicked = False
    mousePos = pygame.mouse.get_pos()
    
    BACK = pygame.image.load(os.path.join('Material','Image',"bullet.png")).convert()
    #BACK.set_colorkey(WHITE)
    #BackButton = ButtonClass.ButtonImage(BACK, 50, 50, 15, 10)
    BACK = pygame.transform.scale(BACK, (50, 50))
    surface.blit(BACK, (15, 10))
    if BACK.get_rect().collidepoint(mousePos):
      if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        clicked = True
        action = True

    if pygame.mouse.get_pressed()[0] == 0:
      clicked = False

   
    #events = pygame.event.get()
    return clicked