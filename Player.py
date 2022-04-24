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
    def update(self):
        
        self.healthbar()
        self.heart(100,30)
        self.shoot()
        self.hit_player()
        self.hit_bonus()
        #set a timer starting now comparing to the respawn time, after 2 seconds, show player image
        current_time=pygame.time.get_ticks()
        if self.respawn and current_time-self.respawn_time>2000:
            self.respawn=False
        if current_time-self.bonus_time>10000:
            self.bullet_num=1
            self.bonus_time=current_time
        #key action responding
        key_pressed=pygame.key.get_pressed()
        if self.respawn==False:
            if key_pressed[pygame.K_RIGHT]:
             self.rect.x=self.rect.x+self.speed
            if key_pressed[pygame.K_LEFT]:
             self.rect.x=self.rect.x-self.speed
            if key_pressed[pygame.K_UP]:
             self.rect.y=self.rect.y-self.speed
            if key_pressed[pygame.K_DOWN]:
                self.rect.y=self.rect.y+self.speed
            if self.rect.right>w:
                self.rect.right=w
            if self.rect.left<0:
                self.rect.x=0
            if self.rect.bottom>h:
                self.rect.bottom=h
            if self.rect.top<0:
              self.rect.top=0
        
     #create one bullet      
    def shoot(self):
        if self.respawn==False:
            if self.bullet_gap>=20:
                self.bullet_gap=0
            elif self.bullet_gap>0:
                self.bullet_gap+=1
            if self.bullet_gap==0:
                if self.bullet_num==1:
                    bullet=Bullet(bulletIMG,30,30,self.rect.centerx,self.rect.top,1,-10)
                    spriteGroup.add(bullet)
                    bulletGroup.add(bullet)
                    self.bullet_gap=1
                elif self.bullet_num==2:
                    bullet1=Bullet(bulletIMG,30,30,self.rect.left,self.rect.top,1,-10)
                    bullet2=Bullet(bulletIMG,30,30,self.rect.right,self.rect.top,1,-10)
                    spriteGroup.add(bullet1)
                    bulletGroup.add(bullet1)
                    spriteGroup.add(bullet2)
                    bulletGroup.add(bullet2)
                    self.bullet_gap=1
                else:
                    bullet=Bullet(laserIMG,50,1368,self.rect.centerx,self.rect.top+25,-1,1000)
                    spriteGroup.add(bullet)
                    bulletGroup.add(bullet)
                    self.bullet_gap=100


    # detect collision between player and the enemy, if player is hit, decrease health and reset enemy object
    def hit_player(self):
        hit_group = pygame.sprite.spritecollide(self, enemyGroup, True)
        for enemy in hit_group:
            self.minus_health(enemy.max_health)
            if level == 1:
                e = Enemy(enemy_covidIMG)
                spriteGroup.add(e)
                enemyGroup.add(e)
            elif level == 2:
                e = Enemy_UFO(enemy_ufoIMG)
                spriteGroup.add(e)
                enemyGroup.add(e)
            elif level == 3:
                e = Enemy_cthulhu(enemy_cthulhuIMG)
                spriteGroup.add(e)
                enemyGroup.add(e)
            else:
                random_int = random.randint(1, 3)
                if random_int == 1:
                    e = Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e)
                elif random_int == 2:
                    e = Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e)
                elif random_int == 3:
                    e = Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e)
        bullet_hit_group = pygame.sprite.spritecollide(self, ebulletGroup, True)
        for ebullet in bullet_hit_group:
            self.minus_health(10)


    def hit_bonus(self):
        hit_group = pygame.sprite.spritecollide(self, bonusGroup, True)

        for bonus in hit_group:
            r = random.randint(0, 2)
            # for testing a specific bonus only r=2
            if (bonus.type == "health"):
                self.add_health(50)
            elif bonus.type == "bullet":
                self.bonus_time = pygame.time.get_ticks()
                self.bullet_num = 2
            elif bonus.type == "laser":
                self.bonus_time = pygame.time.get_ticks()
                # indicates constantly shooting laser instead of bullet
                self.bullet_num = 999
            # regenerate a random bonus after player get a bonus
            if (r == 0):
                bonus = Bonus(heartIMG, "health")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif (r == 1):
                bonus = Bonus(bonus_double_bulletIMG, "bullet")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif (r == 2):
                bonus = Bonus(bonus_laserIMG, "laser")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)

    # detects collision between enemy and player bullet
    def hit_enemy(attackGroup, victumGroup):
        global level, game_level, score, enemyTotal

        enemyTotal = int(8 / game_level)
        hitGroup = pygame.sprite.groupcollide(attackGroup, victumGroup, True,
                                              False)  # stores the collision objects in a list
        for bullet in hitGroup:
            # access the enemy that hit bullet
            for enemy in hitGroup[bullet]:
                # increase score by the enemy's maximum health, varies among types of enemies
                score = score + enemy.max_health
                # each bullet decrease 10 enemy health
                enemy.minus_health(10)
                # when enemy health run out, destroy the enemy object and spawn a new one according to score
                if (enemy.current_health <= 0):

                    spriteGroup.remove(enemy)
                    enemyGroup.remove(enemy)
                    enemy.kill()
                    if game_level == 1:
                        if (len(enemyGroup) < enemyTotal):
                            print("LEVEL1:" + str(enemyTotal))
                            e = Enemy(enemy_covidIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e)
                    elif game_level == 2:
                        if (len(enemyGroup) < enemyTotal):
                            print("LEVEL2:" + str(enemyTotal))
                            e = Enemy_UFO(enemy_ufoIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e)
                    elif game_level == 3:

                        if (len(enemyGroup) < enemyTotal):
                            print("LEVEL3:" + str(enemyTotal))
                            e = Enemy_cthulhu(enemy_cthulhuIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e)

                    else:
                        if (len(enemyGroup) < enemyTotal):
                            print("LEVEL4:" + str(enemyTotal))
                            random_int = random.randint(1, 3)
                            if random_int == 1:
                                e = Enemy(enemy_covidIMG)
                                spriteGroup.add(e)
                                enemyGroup.add(e)
                            elif random_int == 2:
                                e = Enemy_UFO(enemy_ufoIMG)
                                spriteGroup.add(e)
                                enemyGroup.add(e)
                            elif random_int == 3:
                                e = Enemy_cthulhu(enemy_cthulhuIMG)
                                spriteGroup.add(e)
                                enemyGroup.add(e)

       
