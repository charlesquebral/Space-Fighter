import os
import random
import pygame


w,h=1380,720

#RGB color values section
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

#a general bonus material class that gives positive feedback to player, increase 10 health by default
class Bonus(pygame.sprite.Sprite):
    def __init__(self,image,type):
        pygame.sprite.Sprite.__init__(self)
        self.type=type
        self.image=image
        self.image.set_colorkey(WHITE) #remove all white pixels and make them transparent
        self.image=pygame.transform.scale(self.image,(50,50))
        
        self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.x=random.randint(50,w-50) #enemy object position width
        self.rect.y=random.randint(50,250)
        r=random.randint(0,1)
        self.speed_x=random.randint(1,5)
        if(r==0):
            self.speed_x=-self.speed_x
        self.speed_y=random.randint(1,5)
    #defines movement of bonus    
    def update(self):
        self.rect.x=self.rect.x
        self.rect.y=self.rect.y+self.speed_y
        if self.rect.top > h or self.rect.left>w or self.rect.right<0:
            self.rect.x=random.randint(50,950) #enemy object position width
            self.rect.y=random.randint(50,250)
            self.speed=random.randint(1,5)
        if self.rect.top<0:
            self.kill()

