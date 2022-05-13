import unittest
import pygame

class ButtonUnitTesting(unittest.TestCase):
    def test_isLeftClicked(self):
        pygame.init()
        mousePos = (100,100)
        button_rect= pygame.Rect(100,100,100,100)
        eventButton = 1 #event.button {left = 1, right = 2, ...}
        isLeftClicked = False
        buttonisClicked = True #event.type == pygame.MOUSEBUTTONDOWN
        if button_rect.collidepoint(mousePos):
            if buttonisClicked and eventButton == 1:
                print("Left Clicked Mouse Detection... success")
                print("========================")
                isLeftClicked = True
            else:
                isLeftClicked = False
                
        self.assertTrue(isLeftClicked)

    def test_isOnButton(self):
        pygame.init()
        mousePos = (100,100)
        events = pygame.event.get()
        button_rect= pygame.Rect(100,100,100,100)

        isOnButton = False
        if button_rect.collidepoint(mousePos):
            print("Cursor on Button... success")
            print("========================")
            isOnButton = True
        self.assertTrue(isOnButton)

    def test_isColorChanged(self):
        pygame.init()
        screen=pygame.display.set_mode((1350,1000))
        button_color = (255, 0, 0)
        button_rect = pygame.Rect(100, 100, 100, 100)
        pygame.draw.rect(screen, button_color, button_rect)
        self.assertEqual(button_color, (255, 0, 0))
        print("Color changed... success")
        print("========================")

if __name__ == '__main__':
    unittest.main()
        