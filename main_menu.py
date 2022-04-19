import pygame

def main_menu():
      play = ButtonClass.Button("Play", None, fontSize,BLACK,w / 2, 350, WHITE)
      scoreboard = ButtonClass.Button("Scoreboard", None, fontSize, BLACK, w / 2, 450, WHITE)
      options = ButtonClass.Button("Options", None, fontSize, BLACK,w / 2, 550, WHITE)
      quit = ButtonClass.Button("Quit", None, fontSize, BLACK, w / 2, 650, WHITE)
      SPACESHIP = pygame.image.load(os.path.join('Material','Image',"spaceship.png")).convert()
      SPACESHIP = pygame.transform.scale(SPACESHIP, (200, 200))
      SPACESHIP.set_colorkey(WHITE)
      running = True
      while running:
        clock.tick(FPS)
        events = pygame.event.get()

           

        for event in events:
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                pygame.quit()
                sys.exit()
         
        
        pygame.display.set_caption("Main Menu")
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))
        screen.blit(SPACESHIP, (w/2,100))

        if play.click(screen, events):
          
          return PAGE_GAME
          
        if scoreboard.click(screen, events):
          return PAGE_SCOREBOARD
        if options.click(screen, events):
          
          return PAGE_OPTION
        if quit.click(screen, events):
            if quitButton():
                pygame.quit()
                sys.exit()
            else:
                return PAGE_MAIN
        pygame.display.update()