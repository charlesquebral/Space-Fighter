import os
import random

import sys

import pygame

from ModelClass.ButtonClass import *
from ModelClass.ScoreClass import ScoreObject
from ModelClass.BonusClass import *
from ModelClass.BulletClass import Bullet, Bullet_Spread



pygame.init() #initialize pygame
FPS=60
w,h=1380,720
screen=pygame.display.set_mode((w,h)) #display the pygame window in width and size.
pygame.display.set_caption("Road Fighter") #pygame title


#RGB color values section
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
GREY=(127,138,149)
LIGHTBLUE=(173,216,230)
BROWN=(41,2,26)
YELLOW=(242,255,0)
#Image section
#Image loading, finds the directory "Image" after our code directory, convert() is for faster file read in pygame

PAGE_QUIT=0
PAGE_MAIN=1
PAGE_GAME=2
PAGE_SCOREBOARD=3
PAGE_OPTION=4
PAGE_GAMEOVER=5

IS_PAUSE=False

backgroundIMG=pygame.image.load(os.path.join('Material','Image',"background.png")).convert()
backgroundIMG=pygame.transform.scale(backgroundIMG,(w,h))
playerIMG=pygame.image.load(os.path.join('Material','Image',"spaceship.png")).convert()backgroundIMG=pygame.image.load(os.path.join('Material','Image',"background.png")).convert()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=playerIMG
        self.image.set_colorkey(WHITE) #remove all white pixels and make them transparent
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.centerx=w/2 #player object position width
        self.rect.bottom=h-10
        self.speed=10
        #health bar initialization
        self.current_health=100
        self.max_health=100
        self.health_bar_length=200
        self.health_ratio=self.max_health/self.health_bar_length#maximum health/health bar length=0.5, if current_helath*ratio, the current health will be 1/2 of pixels in length
        #max 3 lives, respawn will hide the player image for 2 seconds
        self.lives=3
        self.max_lives=3
        self.respawn=False
        self.respawn_time=0
        self.bonus_time=0
        self.bullet_gap=0
        self.bullet_num=1
        
       
