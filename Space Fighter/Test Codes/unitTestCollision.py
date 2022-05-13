import unittest
import pygame

class test_hit(unittest.TestCase):
  def test_hit_player(self):
    player = pygame.Rect(200,200,200,200)
    enemy = pygame.Rect(300,300,300,300)
    playerHP = 100
    testBool = False
    print ("Player HP is: " + str(playerHP))
    print ("\nNow Testing for collision with enemy...\n")
    if enemy.colliderect(player):
      playerHP = 50
      print ("Collision Works! Player HP now equals: " + str(playerHP))
      testBool = True
    self.assertTrue(testBool)

if __name__ == '__main__':
  unittest.main()

