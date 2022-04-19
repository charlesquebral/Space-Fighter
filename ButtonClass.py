import pygame

class ButtonText():
  def __init__(self, text, font, fontSize, text_color, x, y):
    self.font = pygame.font.Font(font, fontSize)
    self.text = self.font.render(text, True, text_color)
    self.rect = self.text.get_rect()
    self.rect.centerx = x
    self.rect.y = y  
    self.clicked = False

  def click(self, surface,events):
    action = False
    #get mouse position
    mousePos = pygame.mouse.get_pos()

    #draw button on screen
    surface.blit(self.text, (self.rect.x, self.rect.y))
    if self.rect.collidepoint(mousePos):
      for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
          self.clicked = True
        else:
          self.clicked = False
  
    return self.clicked

class Button(ButtonText):
  def __init__(self, text, font, fontSize, text_color, x, y, button_color):
    super().__init__(text, font, fontSize, text_color, x, y)
    
    self.button_color=button_color
    #self.textstring=text
    self.rect= pygame.Rect(x,y,150,50) #this self.rect is different rect from the super class's self.rect
    self.rect.centerx=x
    self.textrect = self.text.get_rect()
    self.textrect.centerx=self.rect.centerx
    self.textrect.centery=self.rect.centery

  def click(self, surface,events): 
    self.clicked = super().click(surface, events)
    mousePos = pygame.mouse.get_pos()
    if self.rect.collidepoint(mousePos):
      pygame.draw.rect(surface, (94,97,100), self.rect)
      
    else:
      pygame.draw.rect(surface, self.button_color, self.rect)
    
    surface.blit(self.text, (self.textrect.x, self.textrect.y))

    return self.clicked
  

class ButtonImage(ButtonText):
  def __init__(self,image, image_width, image_height, x, y, text ='', font=None, fontSize=0, text_color=(255,255,255)):
    super().__init__(text, font, fontSize, text_color, x, y )
    self.text=pygame.transform.scale(image, (image_width,image_height)) #scale image
    #self.rect=self.image.get_rect()
    self.rect = self.text.get_rect()
    self.rect.topleft = (x,y)