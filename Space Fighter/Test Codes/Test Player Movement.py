import os
import random
import pygame
from pygame.locals import * # Constants
import math
import sys


screen = pygame.display.set_mode((1000,1000))

clock = pygame.time.Clock()
RED=(255,0,0)
class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, RED, (100,100,500,500))
        self.distance = 10

    def update(self):
        for e in pygame.event.get():
            key_pressed=pygame.key.get_pressed()

            if e.type == QUIT:
                pygame.quit(); exit()
            elif e.type == KEYDOWN:
                key = e.key
                if key_pressed[pygame.K_LEFT]:
                    self.draw_rect(-1, 0)
                if key_pressed[pygame.K_RIGHT]:
                    self.draw_rect(1, 0)
                if key_pressed[pygame.K_UP]:
                    self.draw_rect(0, -1)
                if key_pressed[pygame.K_DOWN]:
                    self.draw_rect(0, 1)
                elif key == K_ESCAPE:
                    pygame.quit(); exit()
                

    def draw_rect(self,x,y):
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.distance, y*self.distance); pygame.draw.rect(screen, RED, self.rect)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, RED, (100,100,500,500))

pygame.init()

player = Player()
#clock = pygame.time.Clock()
screen.fill((255, 255, 255))
player.draw(screen)
pygame.display.update()

while True:
  player.update()