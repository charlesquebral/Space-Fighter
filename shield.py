import os
import random
import pygame

bonus_shieldIMG=pygame.image.load(os.path.join('Material','Image',"bonus_shield.png")).convert()
shieldIMG=pygame.image.load(os.path.join('Material', 'Image', "shieldIMG.png")).convert()

class Shield(pygame.sprite.Sprite):
    def __init__(self, image, center, player):
        super().__init__()
        self.image = pygame.transform.scale(image, (85, 85))
        self.center = center    
        self.rect = self.image.get_rcet(center=(self.center))
        self.player = player

    def update(self):
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery


