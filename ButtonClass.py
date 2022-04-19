import pygame

class Button():
  def __init__(self, text, font, fontSize, text_color,x, y, button_color):
    self.fontsize=fontSize
    self.font = pygame.font.Font(font, fontSize)
    self.textstring=text
    self.text = self.font.render(text, True, text_color)
    self.text_color=text_color
    self.button_color=button_color

    self.button_rect= pygame.Rect(x,y,150,50)
    self.button_rect.centerx=x
    self.textrect = self.text.get_rect()
    self.textrect.centerx=self.button_rect.centerx
    self.textrect.centery=self.button_rect.centery

 
    self.clicked = False



 
  def click(self, surface,events):

    #get mouse position
    mousePos = pygame.mouse.get_pos()
     #draw button on screen



    #check mouseover and clicked conditions

    if self.button_rect.collidepoint(mousePos):
      pygame.draw.rect(surface, (94,97,100), self.button_rect)
      text = self.font.render(self.textstring, True, (0,0,0))
      surface.blit(text, (self.textrect.x, self.textrect.y))
      for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
              pygame.draw.rect(surface, self.button_color, self.button_rect)
              surface.blit(self.text, (self.textrect.x, self.textrect.y))
              self.clicked = True
        else:
          self.clicked = False
    else:
      pygame.draw.rect(surface, self.button_color, self.button_rect)
      surface.blit(self.text, (self.textrect.x, self.textrect.y))
    return self.clicked
  

class ButtonText():
  def __init__(self, text, font, fontSize, color, x, y):
    self.font = pygame.font.Font(font, fontSize)
    self.text = self.font.render(text, True, color)
    self.textrect = self.text.get_rect()
    self.textrect.centerx = x
    self.textrect.y = y  
    self.clicked = False

  def click(self, surface,events):
    action = False
    #get mouse position
    mousePos = pygame.mouse.get_pos()

    #draw button on screen
    surface.blit(self.text, (self.textrect.x, self.textrect.y))
    if self.textrect.collidepoint(mousePos):
      for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
          self.clicked = True
        else:
          self.clicked = False
  
    return self.clicked
class ButtonImage():
  def __init__(self, image, image_width, image_height, x, y):
    self.image=image
    self.image=pygame.transform.scale(self.image,(image_width,image_height)) #scale image
    #self.rect=self.image.get_rect()
    self.rect = pygame.Rect(x, y, image_width, image_height)
    self.x=x
    self.y=y

    self.clicked = False

  def click(self, surface,events):
   
    #get mouse position
    mousePos = pygame.mouse.get_pos()
     #draw button on screen
    #pygame.draw.rect(surface, self.button_color, self.button_rect)
    surface.blit(self.image, (self.x,self.y))
    #check mouseover and clicked conditions
   
    if self.rect.collidepoint(mousePos):
    
      for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
          self.clicked = True
        else:
          self.clicked = False
  
    return self.clicked