import pygame

def quitButton():
    running = True
    while running:
        clock.tick(FPS)
        pygame.display.update()
        #screen.fill(BLACK)
        BACKGROUND = pygame.transform.scale(backgroundIMG, (500, 150))
        screen.blit(BACKGROUND, (470,300))
        events = pygame.event.get()
        font = pygame.font.Font(None, 40)
        text = font.render("Do you want to exit the game?", True, WHITE)
        screen.blit(text, (510, 330))
        yes = ButtonClass.ButtonText('Yes', None, 40, WHITE, 600, 380)
        if yes.click(screen, events):
            return True
   
        no = ButtonClass.ButtonText('No', None, 40, WHITE, 810, 380)
        if no.click(screen, events):
            return False