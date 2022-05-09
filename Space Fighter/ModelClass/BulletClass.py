import os
import random
import pygame
import math

#RGB color values section
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

w,h=1380,720
#a general bullet class that moves upward by default according to player position
class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,bullet_width,bullet_height,playerX,playerY,direction,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image.set_colorkey(WHITE) #remove all white pixels and make them transparent
        self.image=pygame.transform.scale(self.image,(bullet_width,bullet_height))
        
        self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.centerx=playerX #bullet object position width
        self.rect.bottom=playerY
        self.speed=speed
        self.direction=direction
    def update(self):
        self.rect.y=self.rect.y+self.speed*self.direction
        if (self.rect.right > w or self.rect.left < 0
                or self.rect.bottom > h or self.rect.top < 0):
                self.kill()
#involves a different movement logic in update() function (a linear function)
class Bullet_Spread(pygame.sprite.Sprite):
    def __init__(self,image,playerX,playerY,direction,speedx,speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image.set_colorkey(WHITE) #remove all white pixels and make them transparent
        self.image=pygame.transform.scale(self.image,(50,50))
        
        self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.centerx=playerX #bullet object position width
        self.rect.y=playerY
        self.speedx=speedx
        self.speedy=speedy
        self.direction=direction
    def update(self):
        self.rect.x=self.rect.x+self.speedx
        self.rect.y=self.rect.y+self.speedy*self.direction
        if (self.rect.right > w or self.rect.left < 0
                or self.rect.bottom > h or self.rect.top < 0):
                self.kill()
        
            
