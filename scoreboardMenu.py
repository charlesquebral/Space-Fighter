import pygame

def scoreboardMenu():
      while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                pygame.quit()
                sys.exit()   
       
        if __backButton(screen):
            
            return PAGE_MAIN              
        pygame.display.set_caption("Scoreboard")

        font = pygame.font.Font(None, 90)
        text_name = font.render("Name", True, WHITE)
        screen.blit(text_name, (300, 50))
        text_score = font.render("Score", True, WHITE)
        screen.blit(text_score, (w/2, 50))
        
        with open('scoreboard.txt', 'r') as f:
          font = pygame.font.Font(None, 50)
          f_contents = f.readlines()
          scoresList = []
          for i in range(0, int(len(f_contents)/2)):
            
            scoresList.append(ScoreObject(f_contents[i*2].splitlines()[0],int(f_contents[i*2+1].splitlines()[0])))
            

          scoresList.sort(key=lambda s:s.score,reverse=True)
          j = 0
          for i in range(len(scoresList)):
            
          
          
            strToRender = str(j+1) + ') ' + scoresList[i].user
            text = font.render(strToRender, True, WHITE)
          
            screen.blit(text, (300, 100 + ((j+1)*50)))
            strToRender=str(scoresList[i].score)
            text=font.render(strToRender,True,WHITE)
            screen.blit(text,(w/2,100+(j+1)*50))

            j += 1

 

          pygame.display.update()