import pygame

music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)


def optionsMenu():
    level = 1
    sound = 1.0

    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))
        events = pygame.event.get()

        for event in pygame.event.get():
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            pygame.quit()
            sys.exit()  

        if __backButton(screen):
          #break
          return PAGE_MAIN

        pygame.display.set_caption("Options")

        font = pygame.font.Font(None, 100)
        text = font.render("OPTIONS", True, WHITE)
        screen.blit(text, (w/2.5, 30))
        levelName = font.render("LEVEL", True, WHITE)
        screen.blit(levelName, (150, 150) )
        leftButton = ButtonClass.Button("<", None, 100, BLACK, 500, 160, WHITE)
        rightButton = ButtonClass.Button(">", None, 100, BLACK, 1000, 160, WHITE)

        if leftButton.click(screen, events) and level > 1:
            level = level - 1
        elif rightButton.click(screen, events) and level < 4:
            level = level + 1
        
        if level == 4:
            levelOnScreen = font.render("INFINITE", True, WHITE)
            screen.blit(levelOnScreen, (650, 150))
        else:
            left = font.render(str(level), True, WHITE)
            screen.blit(left, (775, 150))

        soundLevel = font.render("Sound", True, WHITE)
        screen.blit(soundLevel, (150, 300))  
        
        leftButton = ButtonClass.Button("<", None, 100, BLACK, 500, 310, WHITE)
        rightButton = ButtonClass.Button(">", None, 100, BLACK, 1000, 310, WHITE)
        if leftButton.click(screen, events) and sound > 0.0:
            sound = round(sound - 0.1, 1)
        elif rightButton.click(screen, events) and sound < 1.0:
            sound = round(sound + 0.1, 1)
      
        pygame.mixer.music.set_volume(sound)
        soundOnScreen = font.render(str(sound), True, WHITE)
        screen.blit(soundOnScreen, (775, 310))

        pygame.display.update()