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
ButtonLength = 150
ButtonWidth = 50

def loadImage(image):
    return pygame.image.load(os.path.join('Material','Image', image)).convert()

backgroundIMG=loadImage("background.png")
backgroundIMG=pygame.transform.scale(backgroundIMG,(w,h))
playerIMG=loadImage("spaceship.png")
enemy_covidIMG=loadImage("enemy_covid.jpg")
enemy_ufoIMG=loadImage("enemy_ufo.png")
enemy_cthulhuIMG=loadImage("enemy_cthulhu.png")
heartIMG=loadImage("heart_present.png")
heartIMG=pygame.transform.scale(heartIMG,(50,50)) #change the original picture's resolution to w,h(50,50)
heartIMG.set_colorkey(WHITE) #remove all white pixels and make them transparent

heart_goneIMG=loadImage("heart_gone.png")
heart_goneIMG=pygame.transform.scale(heart_goneIMG,(50,50)) #change the original picture's resolution to w,h(50,50)
heart_goneIMG.set_colorkey(WHITE) #remove all white pixels and make them transparent

bulletIMG=loadImage("bullet.png")
enemy_bulletIMG=loadImage("enemy_bullet.png")
bonus_double_bulletIMG=loadImage("bonus_double_bullet.jpg")

bonus_double_bulletIMG=loadImage("bonus_double_bullet.jpg")
laserIMG=loadImage("laser.png")
laserIMG.set_colorkey(WHITE)

bonus_laserIMG=loadImage("explosion_0.png")
pauseIMG=loadImage("pause.png")
pauseIMG.set_colorkey(BLACK)


    



#font style and font display section
font_name=pygame.font.match_font('arial')
fontSize=24
def display_text(screen, text,color,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    screen.blit(text_surface,text_rect)




score=0

#define maximum enemy total
enemyTotal=6      
level=1
game_level=1
volume=1



#all lists
playerGroup=pygame.sprite.Group()
spriteGroup=pygame.sprite.Group()
enemyGroup=pygame.sprite.Group()
bulletGroup=pygame.sprite.Group() #from player
ebulletGroup=pygame.sprite.Group() #from enemy
bonusGroup=pygame.sprite.Group()

#default enemy object, covid image and have 10 heart
class Character(pygame.sprite.Sprite):
    def __init__(self, curr_health, max_health, image, xScale, yScale):
        self.current_health = curr_health
        self.max_health = max_health
        self.image = image
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (xScale,yScale))
        self.rect = self.image.get_rect()

#default enemy object, covid image and have 10 heart
class Enemy(Character):
    def __init__(self,image):
        global score

        pygame.sprite.Sprite.__init__(self)
        super().__init__(10, 10, image, 50, 50)
        self.rect.x=random.randint(50,w-50) #enemy object position width
        self.rect.y=30
        #r=random.randint(0,1)
        
        self.speed_y=7
        
    #define covid enemy's movement, moves as a horizontal line and static downward    
    def update(self, toRange=950): 
        self.rect.y+=self.speed_y
        if self.rect.top > h:
            self.rect.x=random.randint(50,toRange) #enemy object position width
            self.rect.y=30
            #self.speed=random.randint(1,5)
    #decrease covid enemy object health 
    def minus_health(self,amount):
        if self.current_health>0:
            self.current_health-=amount
           
           
        if self.current_health<=0:
            self.current_health=0
#second type of enemy, shaped like a UFO, 20 health, random movement vertically 
class Enemy_UFO(Enemy):
    def __init__(self,image):
        global score
        pygame.sprite.Sprite.__init__(self)
        Character.__init__(self, 20,20, image, 100, 100)
        #self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.x=random.randint(100,w-100) #enemy object position width
        self.rect.y=30
        self.bullet_gap=0
        self.bullet_num=1
        r=random.randint(0,1)
        self.speed_x=3
        if (r==0):
            self.speed_x=-self.speed_x
        self.speed_y=2

        #play spawn sound
        soundRand = random.randint(0, 0)
        if (soundRand == 1):
            ufoSpawn = pygame.mixer.Sound(os.path.join('Material','Audio',"enemy_ufo_spawn1.mp3"))
        else:
            ufoSpawn = pygame.mixer.Sound(os.path.join('Material','Audio',"enemy_ufo_spawn2.mp3"))

        ufoSpawn.play()
        ufoSpawn.set_volume(volume)
    def shoot(self):
        
            if self.bullet_gap>=40:
                self.bullet_gap=0
            elif self.bullet_gap>0:
                self.bullet_gap+=1
            if self.bullet_gap==0:
                if self.bullet_num==1:
                    bullet=Bullet(enemy_bulletIMG,30,30,self.rect.centerx,self.rect.bottom,-1,-3)
                    spriteGroup.add(bullet)
                    ebulletGroup.add(bullet)
                    self.bullet_gap=1
                    #play shoot sound (single shoot sound for now)
                    ufoShoot = pygame.mixer.Sound(os.path.join('Material','Audio',"ship_shoot_single.mp3"))
                    ufoShoot.play()
                    ufoShoot.set_volume(volume)
                  
    #defines movement of ufo enemy, random vertical movement
    def update(self):
        self.shoot()
        self.rect.x=self.rect.x
        super().update()
        if self.rect.left>w or self.rect.right<0:
            self.speed_x=-self.speed_x


class Enemy_cthulhu(Enemy):
    def __init__(self,image):
        global score
        pygame.sprite.Sprite.__init__(self)
        Character.__init__(self, 30,30, image, 150, 150)
        self.original_image = self.image.copy()
        #self.rect=self.image.get_rect() #gets the surface area of the image
        self.rect.x=random.randint(150,w-150) #enemy object position width
        self.rect.y=30
        self.rotation_degree=4
        self.total_degree=0
        r=random.randint(0,1)
        self.speed_x=3
        self.bullet_num=1
        self.bullet_gap=1
        if (r==0):
            self.speed_x=-self.speed_x
        
        self.speed_y=3

        #play spawn sound
        soundRand = random.randint(0, 1)
        if (soundRand == 0):
            cthulhuSpawn = pygame.mixer.Sound(os.path.join('Material','Audio',"enemy_cthulhu_spawn1.mp3"))
        else:
            cthulhuSpawn = pygame.mixer.Sound(os.path.join('Material','Audio',"enemy_cthulhu_spawn2.mp3"))

        cthulhuSpawn.play()
        cthulhuSpawn.set_volume(volume)
    def shoot(self):
        
            if self.bullet_gap>=30:
                self.bullet_gap=0
            elif self.bullet_gap>0:
                self.bullet_gap+=1
            if self.bullet_gap==0:
                #bullet moves up or down (1=down,-1=up)
                direction=1
                #decides which direction in the x axis the bullet moves (+right,-left )
                speedx=3
                for i in range (1,5):
                   
                        
                    if i==2:
                        speedx=-3
                    elif i==3:
                        direction=-1
                        speedx=3
                    elif i==4:
                        
                        speedx=-3
                    bullet=Bullet_Spread(enemy_bulletIMG,self.rect.centerx,self.rect.centery,direction,speedx,5)
                    spriteGroup.add(bullet)
                    ebulletGroup.add(bullet)
               
                self.bullet_gap=1
                #play shoot sound (double shoot sound for now)
                cthulhuShoot = pygame.mixer.Sound(os.path.join('Material','Audio',"ship_shoot_double.mp3"))
                cthulhuShoot.play()
                cthulhuShoot.set_volume(volume)
    
               
    #defines movement of cthulhu enemy, random vertical movement
    def update(self):
        
        self.rotate()
        self.shoot()
        self.rect.x=self.rect.x-self.speed_x
        super().update(1680)
        if self.rect.left>w or self.rect.right<0:
            self.speed_x=-self.speed_x
    
    def rotate(self):
        self.total_degree+=self.rotation_degree
        #make sure rotation degree doesn't exceed 360
        self.total_degree=self.total_degree%360
        self.image=pygame.transform.rotate(self.original_image,self.total_degree)
        #stores the original image's center
        center=self.rect.center
        self.rect=self.image.get_rect()
        #reset new image to original center
        self.rect.center=center

class Player(Character):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(100, 100, playerIMG, 70, 100)
        self.rect.centerx=w/2 #player object position width
        self.rect.bottom=h-10
        self.speed=10
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

            #play spawn sound
            playerSpawn = pygame.mixer.Sound(os.path.join('Material','Audio',"ship_spawn.mp3"))
            playerSpawn.play()
            playerSpawn.set_volume(volume)
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

                    #play shoot sound
                    playerShootSingle = pygame.mixer.Sound(os.path.join('Material','Audio',"ship_shoot_single.mp3"))
                    playerShootSingle.play()
                    playerShootSingle.set_volume(volume)
                elif self.bullet_num==2:
                    bullet1=Bullet(bulletIMG,30,30,self.rect.left,self.rect.top,1,-10)
                    bullet2=Bullet(bulletIMG,30,30,self.rect.right,self.rect.top,1,-10)
                    spriteGroup.add(bullet1)
                    bulletGroup.add(bullet1)
                    spriteGroup.add(bullet2)
                    bulletGroup.add(bullet2)
                    self.bullet_gap=1

                    #play shoot sound
                    playerShootDouble = pygame.mixer.Sound(os.path.join('Material','Audio',"ship_shoot_double.mp3"))
                    playerShootDouble.play()
                    playerShootDouble.set_volume(volume)
                else:
                    bullet=Bullet(laserIMG,50,1368,self.rect.centerx,self.rect.top+25,-1,1000)
                    spriteGroup.add(bullet)
                    bulletGroup.add(bullet)
                    self.bullet_gap=100
  
    #detect collision between player and the enemy, if player is hit, decrease health and reset enemy object
    def hit_player(self):
        hit_group=pygame.sprite.spritecollide(self,enemyGroup,True)
        for  enemy in hit_group:
            self.minus_health(enemy.max_health)
            if level==1:
              e=Enemy(enemy_covidIMG)
              spriteGroup.add(e)
              enemyGroup.add(e)
            elif level==2:
               e=Enemy_UFO(enemy_ufoIMG)
               spriteGroup.add(e)
               enemyGroup.add(e)
            elif level==3:
               e=Enemy_cthulhu(enemy_cthulhuIMG)
               spriteGroup.add(e)
               enemyGroup.add(e)
            else:
                random_int=random.randint(1,3)
                if random_int==1:
                    e=Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
                elif random_int==2:
                    e=Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
                elif random_int==3:
                    e=Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
        bullet_hit_group=pygame.sprite.spritecollide(self,ebulletGroup,True)
        for ebullet in bullet_hit_group:
            self.minus_health(10)

    def hit_bonus(self):
        hit_group=pygame.sprite.spritecollide(self,bonusGroup,True)
        
        for bonus in hit_group:
            r=random.randint(0,2)
            #for testing a specific bonus only r=2
            if (bonus.type=="health"):
                self.add_health(50)
            elif bonus.type=="bullet":
                self.bonus_time=pygame.time.get_ticks()
                self.bullet_num=2
            elif bonus.type=="laser":
                self.bonus_time=pygame.time.get_ticks()
                #indicates constantly shooting laser instead of bullet
                self.bullet_num=999
            #regenerate a random bonus after player get a bonus
            if (r==0):
                bonus=Bonus(heartIMG,"health")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif(r==1):
                bonus=Bonus(bonus_double_bulletIMG,"bullet")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif(r==2):
                bonus=Bonus(bonus_laserIMG,"laser")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
    
    
    def healthbar(self):
        pygame.draw.rect(screen,RED,(100,100,self.current_health/self.health_ratio,25))#1st=pygame screen;2nd=RGB color;3rd,4th=icon location in screen;5th,6th=icon width, height
        pygame.draw.rect(screen,WHITE,(100,100,self.health_bar_length,25),1)#last input is to click a border around the rectangle
        display_text(screen,"Health: "+str(self.current_health),WHITE,18,50,100)#Write "Health" in the screen position (50,100)
    
    #function to decrease health
    def minus_health(self,amount):
        if self.current_health>0:
            self.current_health-=amount
           
        #lose 1 heart when health run out and reset health to maximum value   
        if self.current_health<=0:
            self.current_health=0
            if (self.lives>=0):
                self.lives-=1
            
            self.add_health(100)
            #hide player for 2 seconds
            expl = Explosion(self.rect.center,70)
                
            spriteGroup.add(expl)
            self.wait_respawn()

        
    def add_health(self,amount):
        if self.current_health<self.max_health:
            self.current_health+=amount
            
        if self.current_health>=self.max_health:
            self.current_health=self.max_health
    
    def heart(self,x,y):
        
        for i in range(self.max_lives):
            heart_x=x+70*i
            heart_y=y
            #display full heart that is equal to current heart count
            if i<self.lives:
                screen.blit(heartIMG,(heart_x,heart_y))
            #display dark heart that is equal to amount of heart lost
            else:
                screen.blit(heart_goneIMG,(heart_x,heart_y))
        

    #hide player image for 2 seconds
    
    def wait_respawn(self):
        self.respawn=True
        self.respawn_time=pygame.time.get_ticks()
        self.rect.center=(w/2,h+1000)

#detects collision between enemy and player bullet
def hit_enemy(attackGroup,victumGroup):
    global level,game_level,score,enemyTotal
    
    enemyTotal=int(8/game_level)
    hitGroup=pygame.sprite.groupcollide(attackGroup,victumGroup,True,False) #stores the collision objects in a list
    for bullet in hitGroup:
        #access the enemy that hit bullet
        for enemy in hitGroup[bullet]:
            #increase score by the enemy's maximum health, varies among types of enemies
            
            #each bullet decrease 10 enemy health
            enemy.minus_health(10)
            #when enemy health run out, destroy the enemy object and spawn a new one according to score
            if (enemy.current_health<=0):
                score=score+enemy.max_health
                print(enemy.rect.height)
                expl = Explosion(enemy.rect.center,enemy.max_health*3)
                
                spriteGroup.add(expl)
                spriteGroup.remove(enemy)
                enemyGroup.remove(enemy)
                enemy.kill()
                if game_level==1:
                    if(len(enemyGroup)<enemyTotal):
                        print("LEVEL1:"+str(enemyTotal))
                        e=Enemy(enemy_covidIMG)
                        spriteGroup.add(e)
                        enemyGroup.add(e)
                elif game_level==2:
                    if(len(enemyGroup)<enemyTotal):
                        print("LEVEL2:"+str(enemyTotal))
                        e=Enemy_UFO(enemy_ufoIMG)
                        spriteGroup.add(e)
                        enemyGroup.add(e)
                elif game_level==3:
                   
                    if(len(enemyGroup)<enemyTotal):
                        print("LEVEL3:"+str(enemyTotal))
                        e=Enemy_cthulhu(enemy_cthulhuIMG)
                        spriteGroup.add(e)
                        enemyGroup.add(e)

                else:
                    if(len(enemyGroup)<enemyTotal):
                        print("LEVEL4:"+str(enemyTotal))
                        random_int=random.randint(1,3)
                        if random_int==1:
                            e=Enemy(enemy_covidIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e) 
                        elif random_int==2:
                            e=Enemy_UFO(enemy_ufoIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e) 
                        elif random_int==3:
                            e=Enemy_cthulhu(enemy_cthulhuIMG)
                            spriteGroup.add(e)
                            enemyGroup.add(e) 


#image resource reference:<a href="https://www.freepik.com/vectors/animation-frames">Animation frames vector created by freepik - www.freepik.com</a> 
#code reference: https://kidscancode.org/blog/2016/09/pygame_shmup_part_10/
explosion_anim = {}
BLACK=(0,0,0)
explosion_anim= []
for i in range(5):
    filename = 'explosion_{}.png'.format(i)
    
    img = loadImage(filename)
    img.set_colorkey(BLACK)
    img=pygame.transform.scale(img, (50, 50))
    explosion_anim.append(img)
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60

        #play explosion sound
        explosionSound = pygame.mixer.Sound(os.path.join('Material','Audio',"explosion.mp3"))
        explosionSound.play()
        explosionSound.set_volume(volume)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = pygame.transform.scale(explosion_anim[self.frame],(self.size,self.size))
                self.rect = self.image.get_rect()
                self.rect.center = center
clock=pygame.time.Clock()
#referenced: https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
def name():
    global score, user
    box_width=300
    box_height=50
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    
    input_box = pygame.Rect(w/2-box_width/2, h/2,box_width, box_height )
    
    color_inactive = WHITE
    color_active = GREEN
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                user="ANONYMOUS"
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text is None or text=='':
                            user="ANONYMOUS"
                        else:
                            user=text
                        return PAGE_GAMEOVER
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text)<20:

                            text += event.unicode.upper()
        
        
             


        screen.fill(BLACK)
        screen.blit(backgroundIMG,(0,0))
        display_text(screen,"Your Score:",WHITE,48,w/2,100)
        display_text(screen,str(score),WHITE,128,w/2,150)
        display_text(screen,"Enter Your Name:",WHITE,48,w/2,300)
        # Render the current text.
        txt_surface = font.render(text, True, WHITE)
        # Resize the box if the text is too long.
        #width = max(200, txt_surface.get_width()+10)
      
        
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+12.5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        save=Button("SAVE", pygame.font.match_font('arial'), 18, BLACK, w/2+250, h/2,WHITE, ButtonLength, ButtonWidth)
        
        if save.click(screen,events):
            if text is None or text=='':
                user="ANONYMOUS"
            else:
                user=text
            return PAGE_GAMEOVER
          
        pygame.display.flip()
        clock.tick(30)
def store_score():
    global user
    
    scoresList = []

    with open('scoreboard.txt', 'r') as f:
        font = pygame.font.Font(None, 50)
        f_contents = f.readlines()
        
        for i in range(0, int(len(f_contents)/2)):
            scoresList.append(ScoreObject(f_contents[i*2].splitlines()[0],int(f_contents[i*2+1].splitlines()[0])))
            
        f.close()
    print(len(scoresList))
    if len(scoresList)<10:
        name()
        scoresList.append(ScoreObject(user,str(score)))
        with open('scoreboard.txt','w') as f:
            for i in range (0,len(scoresList)):
                f.write(scoresList[i].user+'\n')
                f.write(str(scoresList[i].score)+'\n')
            f.close()
      
        f.close()
    elif len(scoresList)>=10:
        
        #sort score list in decending score order
        scoresList.sort(key=lambda s:s.score,reverse=True)
        #if current score>the 10th record (lowest score) in arraylist, replace the 10th record with current score
        if scoresList[len(scoresList)-1].score<score:
            name()
            scoresList[len(scoresList)-1].user=user
            scoresList[len(scoresList)-1].score=score
            with open('scoreboard.txt','w') as f:
                for i in range (0,len(scoresList)):
                    f.write(scoresList[i].user+'\n')
                    f.write(str(scoresList[i].score)+'\n')
                f.close()

                
                

    #call collision functions
        hit_enemy(bulletGroup,enemyGroup)
        
    #put everything in spriteGroup list to the screen
   
        spriteGroup.draw(screen)
    #move all elements within the spriteGroup list
        spriteGroup.update()
    #update the screen elements 60 frames a second
        pygame.display.update() #update the black screen to background image


def __backButton(surface):
    action = False
    clicked = False
    mousePos = pygame.mouse.get_pos()
    #BACK = pygame.image.load(os.path.join('Material','Image',"bullet.png")).convert()
    BACK = loadImage("back.png")
    BACK = pygame.transform.scale(BACK, (50, 50))
    BACK.set_colorkey(BLACK)
    surface.blit(BACK, (15, 10))
    if BACK.get_rect().collidepoint(mousePos):
      if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        clicked = True
        action = True

    if pygame.mouse.get_pressed()[0] == 0:
      clicked = False

   

    return action

def main_menu():
      play = Button("PLAY", None, fontSize,BLACK,w / 2, 350,WHITE, ButtonLength, ButtonWidth)
      scoreboard = Button("SCOREBOARD", None, fontSize, BLACK, w / 2, 450,WHITE, ButtonLength, ButtonWidth)
      options = Button("OPTIONS", None, fontSize, BLACK,w / 2, 550,WHITE, ButtonLength, ButtonWidth)
      quit = Button("QUIT", None, fontSize, BLACK, w / 2, 650,WHITE, ButtonLength, ButtonWidth)
      SPACESHIP = loadImage("spaceship.png")
      #SPACESHIP = pygame.image.load(os.path.join('Material','Image',"spaceship.png")).convert()
      SPACESHIP = pygame.transform.scale(SPACESHIP, (200, 200))
      SPACESHIP.set_colorkey(WHITE)
      
      running = True
      while running:
        clock.tick(FPS)
       
           
        events=pygame.event.get()
        for event in events:
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                pygame.quit()
                sys.exit()
            #return PAGE_QUIT
         
        
        pygame.display.set_caption("Main Menu")
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))
        screen.blit(SPACESHIP, (w/2-100,100))
        display_text(screen,"SPACE FIGHTER",WHITE,30,w/2,50)
        if play.click(screen,events):
          
          return PAGE_GAME
          
        if scoreboard.click(screen,events):
          
          return PAGE_SCOREBOARD
        if options.click(screen,events):
          
          return PAGE_OPTION
        if quit.click(screen,events):
           if quitButton():
                pygame.quit()
                sys.exit()
           else:
                return PAGE_MAIN
        pygame.display.update()

def quitButton():
    fontSize = 20
    while True:
        lenButton = 500
        widButton = 150
        xPos = w/2-200
        yPos = 300
        clock.tick(FPS)
        #screen.fill(BLACK)
        #BACKGROUND = pygame.transform.scale(backgroundIMG, (500, 150))
        
        border_width=5
        
        pygame.draw.rect(screen, BROWN, pygame.Rect(xPos,yPos,lenButton,widButton))
        pygame.draw.rect(screen, WHITE, pygame.Rect(xPos,yPos,lenButton,widButton), width=border_width)
        
        #screen.blit(BACKGROUND, (470,300))
        events = pygame.event.get()
        font = pygame.font.Font(None, fontSize+20)
        text = font.render("Do you want to exit the game?", True, WHITE)
        screen.blit(text, (530, 330))
        lenButton = 150
        widButton = 30
        yPos += 80
        buttonFontSize=36
        yes = Button('YES', None, buttonFontSize, BLACK,  650, yPos, WHITE, lenButton, widButton)
        if yes.click(screen, events):
            return True 

        no = Button('NO', None, buttonFontSize, BLACK,  810, yPos, WHITE, lenButton, widButton)
        if no.click(screen, events):
            return False
        pygame.display.update()

    """ while True:
        clock.tick(FPS)
        #screen.fill(BLACK)
        BACKGROUND = pygame.transform.scale(backgroundIMG, (500, 150))
        
        border_width=5
        
        pygame.draw.rect(screen, BROWN, pygame.Rect(w/2-200,300,500,150))
        pygame.draw.rect(screen, WHITE, pygame.Rect(w/2-200,300,500,150),width=border_width)
        
        
        #screen.blit(BACKGROUND, (470,300))
        events = pygame.event.get()
        exitButton = ButtonText('X', None, 25, WHITE, 950, 310)
        if exitButton.click(screen, events):
           
            return False
        font = pygame.font.Font(None, 40)
        text = font.render("Do you want to exit the game?", True, WHITE)
        screen.blit(text, (510, 330))
        yes = Button('YES', None, 40,BLACK,  600, 380,WHITE)
        if yes.click(screen, events):
            return True 

        no = Button('NO', None, 40,BLACK,  810, 380,WHITE)
        if no.click(screen, events):
            return False
        pygame.display.update() """
def Main_Prompt():
    while True:
        clock.tick(FPS)
        pygame.draw.rect(screen, BROWN, pygame.Rect(w/2-200,300,450,150))
        pygame.draw.rect(screen, WHITE, pygame.Rect(w/2-200,300,450,150),width=5)
        events = pygame.event.get()
        
        font = pygame.font.Font(None, 40)
        text = font.render("Return to Main Menu?", True, WHITE)
        screen.blit(text, (510, 330))
        yes = Button('YES', None, 40,BLACK,  600, 380,WHITE, ButtonLength, ButtonWidth)
        if yes.click(screen, events):
            return True 

        no = Button('NO', None, 40,BLACK,  810, 380,WHITE, ButtonLength, ButtonWidth)
        if no.click(screen, events):
            return False
        pygame.display.update()
def pause_game(events):
    global IS_PAUSE
    border_width=5
    pygame.draw.rect(screen, BROWN, pygame.Rect(w/2-150,180,300,350))
    pygame.draw.rect(screen, WHITE, pygame.Rect(w/2-150,180,300,350),width=border_width)
    display_text(screen,"Pause",WHITE,48,w/2,200)
    resume = Button("RESUME", None, fontSize, BLACK,w / 2, 300,WHITE, ButtonLength, ButtonWidth)
    main = Button("MAIN MENU", None, fontSize, BLACK, w / 2, 380,WHITE, ButtonLength, ButtonWidth)
    quit = Button("QUIT", None, fontSize, BLACK, w / 2, 460,WHITE, ButtonLength, ButtonWidth)
     
        

    pygame.display.set_caption("Pause Menu")
    #screen.fill(BLACK)
    #screen.blit(backgroundIMG, (0,0))
    #events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            
                IS_PAUSE=False 
        
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                
                IS_PAUSE=False
                
            
    
    if resume.click(screen,events):
        IS_PAUSE=False
        
        
  
  
    if main.click(screen,events):
        if Main_Prompt():
            return PAGE_MAIN
        else:
            return
    if quit.click(screen,events):
        if quit.click(screen,events):
           if quitButton():
                pygame.quit()
                sys.exit()
          
    pygame.display.update()
         
def gameover_menu():
      global game_level,score
      
      replay = Button("REPLAY", None, fontSize,BLACK,w / 2, 350,WHITE, ButtonLength, ButtonWidth)
      scoreboard = Button("SCOREBOARD", None, fontSize,BLACK,w / 2, 450,WHITE, ButtonLength, ButtonWidth)
      main = Button("MAIN MENU", None, fontSize, BLACK, w / 2, 550,WHITE, ButtonLength, ButtonWidth)
      quit = Button("QUIT", None, fontSize, BLACK, w / 2, 650,WHITE, ButtonLength, ButtonWidth)
      #SPACESHIP = pygame.image.load(os.path.join('Material','Image',"spaceship.png")).convert()
      #SPACESHIP = pygame.transform.scale(SPACESHIP, (200, 200))
      #SPACESHIP.set_colorkey(WHITE)
      
      running = True
      while running:
        clock.tick(FPS)
       
           
        events=pygame.event.get()
        for event in events:
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                pygame.quit()
                sys.exit()
            
         
        
        pygame.display.set_caption("Game Over")
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))
        
        display_text(screen,"Game Over",WHITE,50,w/2,50)
        display_text(screen,"Your Score: "+str(score),WHITE,50,w/2,150)
        if game_level==4:
            display_text(screen,"You Reached Level: Infinite",WHITE,50,w/2,200)
        else:
            display_text(screen,"You Reached Level: "+str(game_level),WHITE,50,w/2,250)
        #screen.blit(SPACESHIP, (w/2-100,100))
        
        if replay.click(screen,events):
          
          return PAGE_GAME
        if scoreboard.click(screen,events):
          return PAGE_SCOREBOARD
          
        if main.click(screen,events):
          return PAGE_MAIN
        if quit.click(screen,events):
          
          if quitButton():
                pygame.quit()
                sys.exit()
          else:
                return PAGE_GAMEOVER
        
        pygame.display.update()        

def game_play():
    global level,game_level,score,enemyTotal,IS_PAUSE
    IS_PAUSE=False
    #create a player object and add it to lists
    game_level=level
    #pause_button = ButtonText("PAUSE", None, 50, WHITE, w-200, 20)
    pause_button = ButtonImage(pauseIMG, 50, 50, w-200, 20)
    
    score=0
    playerGroup.empty()
    bonusGroup.empty()
    enemyGroup.empty()
    spriteGroup.empty()
    bulletGroup.empty()
    ebulletGroup.empty()
   
    player=Player()
    
    playerGroup.add(player)
    spriteGroup.add(player) 

#create a health bonus and add it to lists
    
    bonus=Bonus(heartIMG,"health")
    spriteGroup.add(bonus)
    bonusGroup.add(bonus)
   
         



    


    
    #initialize some covid shaped enemy when score is lower than 10
    if (game_level==1):
        enemyTotal=int(8/game_level)
        for i in range(enemyTotal):
            
            e=Enemy(enemy_covidIMG)
            spriteGroup.add(e)
            enemyGroup.add(e)
    elif game_level==2:
          
          enemyTotal=int(8/game_level)
          for i in range(enemyTotal):
            
            e=Enemy_UFO(enemy_ufoIMG)
            spriteGroup.add(e)
            enemyGroup.add(e)
    elif game_level==3:
          
          enemyTotal=int(8/game_level)
          for i in range(enemyTotal):
            
            e=Enemy_cthulhu(enemy_cthulhuIMG)
            spriteGroup.add(e)
            enemyGroup.add(e)
    else:
       
        for i in range(enemyTotal):
                random_int=random.randint(1,3)
                if random_int==1:
                    e=Enemy(enemy_covidIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
                elif random_int==2:
                    e=Enemy_UFO(enemy_ufoIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
                elif random_int==3:
                    e=Enemy_cthulhu(enemy_cthulhuIMG)
                    spriteGroup.add(e)
                    enemyGroup.add(e) 
    
    active=True
    while active:  
        #set the game to run 60 frames per second
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(backgroundIMG,(0,0)) #set screen to background image
        display_text(screen,"Score: "+str(score),WHITE,18,w/2,10)
        if game_level == 4:
            display_text(screen,"Level: Infinite",WHITE,18,w/2,30)
        else: 
            display_text(screen,"Level: "+str(game_level),WHITE,18,w/2,30)
        
        
        events=pygame.event.get()
    #detects key single key action
        for event in events:
            if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
                if quitButton():
                    pygame.quit()
                    sys.exit() 
            
            #elif event.type == pygame.KEYDOWN:
                #if event.key==pygame.K_SPACE:
                    #player.shoot()
        if(pause_button.click(screen,events)):
            IS_PAUSE=True
           
          
        if(score<=100):
            if game_level<=1:
                game_level=1
            
        elif score>100 and score<=300:
           
            if game_level<=2:
                game_level=2
            
        elif score>300 and score<=600:
            
            if game_level<=3:
                game_level=3
        else:
           
            if game_level<=4:
                game_level=4
        #clear all global variables
        if(player.lives<=0):
           
            store_score()
            return PAGE_GAMEOVER
             
        #put everything in spriteGroup list to the screen

        spriteGroup.draw(screen)
        if IS_PAUSE: 
            result=pause_game(events)
            if(result==PAGE_SCOREBOARD):
                return PAGE_SCOREBOARD
            elif result==PAGE_OPTION:
                return PAGE_OPTION
            elif result==PAGE_MAIN:
                
                return PAGE_MAIN
        else:
        #call collision functions
            hit_enemy(bulletGroup,enemyGroup)
       
        #move all elements within the spriteGroup list
            spriteGroup.update()
        #update the screen elements 60 frames a second
            pygame.display.update() 
            
                 
 
   
    
   
    




def scoreboardMenu():
      global IS_PAUSE
      while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                pygame.quit()
                sys.exit()
            else:
                return PAGE_SCOREBOARD
       
        if __backButton(screen):
            if IS_PAUSE:
                break
            else:
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
  
        



def optionsMenu():
    
    
    global level,volume

    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(backgroundIMG, (0,0))
        events = pygame.event.get()

         
        for event in events:
          if event.type == pygame.QUIT: #if user clicks the x button, exit pygame
            if quitButton():
                    pygame.quit()
                    sys.exit() 
           

        if __backButton(screen):
          pygame.mixer.music.stop()
          return PAGE_MAIN

        pygame.display.set_caption("Options")

        font = pygame.font.Font(None, 100)
        text = font.render("OPTIONS", True, WHITE)
        screen.blit(text, (w/2.5, 30))
        levelName = font.render("LEVEL", True, WHITE)
        screen.blit(levelName, (150, 150) )
        button_level_down = Button("<", None, 100, BLACK, 500, 160, WHITE, ButtonLength, ButtonWidth)
        button_level_up = Button(">", None, 100, BLACK,  1000, 160,WHITE, ButtonLength, ButtonWidth)

        if button_level_down.click(screen, events) and level > 1:
            level = level - 1
        elif button_level_up.click(screen, events) and level < 4:
            level = level + 1
        
        if level == 4:
            levelOnScreen = font.render("INFINITE", True, WHITE)
            screen.blit(levelOnScreen, (600, 150))
        else:
            level_display = font.render(str(level), True, WHITE)
            screen.blit(level_display, (700, 150))

        soundLevel = font.render("SOUND", True, WHITE)
        screen.blit(soundLevel, (150, 300))  
        
        button_volume_down = Button("<", None, 100, BLACK,  500, 310,WHITE, ButtonLength, ButtonWidth)
        button_volume_up = Button(">", None, 100, BLACK,  1000, 310,WHITE, ButtonLength, ButtonWidth)
        if button_volume_down.click(screen, events) and volume > 0.0:
            volume = round(volume - 0.1, 1)
        elif button_volume_up.click(screen, events) and volume < 1.0:
            volume = round(volume + 0.1, 1)
      
        pygame.mixer.music.set_volume(volume)
        soundOnScreen = font.render(str(int(volume*10)), True, WHITE)
        screen.blit(soundOnScreen, (700, 310))

        pygame.display.update()
def Main():
    music = pygame.mixer.music.load(os.path.join('Material','Audio',"Music_menu.mp3"))
    pygame.mixer.music.play(-1) 
    scene = PAGE_MAIN
    while True:
        #clock.tick(FPS)
        if scene is None:
            pygame.mixer.music.load(os.path.join('Material','Audio',"Music_menu.mp3"))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.play(-1)
            scene=main_menu()
        if scene == PAGE_MAIN:
            pygame.mixer.music.load(os.path.join('Material','Audio',"Music_menu.mp3"))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            scene = main_menu()
        if scene == PAGE_GAME:
            #pygame.mixer.music.load(os.path.join('Material','Audio',"Music_game.mp3"))
            pygame.mixer.music.load(os.path.join('Material','Audio',"Music_game_test.mp3"))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1) 
            scene = game_play()
        if scene == PAGE_SCOREBOARD:
            scene = scoreboardMenu()
        if scene == PAGE_OPTION:
            pygame.mixer.music.load(os.path.join('Material','Audio',"Music_menu.mp3"))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)  
            scene = optionsMenu()
        if scene == PAGE_GAMEOVER:
            pygame.mixer.music.load(os.path.join('Material','Audio',"Music_gameover.mp3"))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()
            scene = gameover_menu()
        if scene==PAGE_QUIT:
            pygame.quit()
            sys.exit()

Main()
 
        


