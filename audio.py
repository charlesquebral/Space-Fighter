import pygame

from pygame import mixer
from ModelClass.Main import scene

pygame.init()
mixer.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Audio Test Output')
font = pygame.font.Font('freesansbold.ttf', 32)

def Music()

	while True:
	if scene == 1
		mixer.music.load("menu.mp3")
		mixer.music.play(-1)	

		#text = font.render('menu music played infinitely', True, black, white)
    		#display_surface.blit(text, textRect)


	if scene == 2
		mixer.music.load("gameplay.mp3")
		mixer.music.play(-1)

		#text = font.render('gameplay music played infinitely', True, black, white)
    		#display_surface.blit(text, textRect)


	if scene == 5
		mixer.music.load("gameover.mp3")
		mixer.music.play()
		
		#text = font.render('gameover music played once', True, black, white)
    		#display_surface.blit(text, textRect)