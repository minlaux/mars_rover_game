import pygame
from pygame.locals import *


class Game:
    def __init__(self, background, title, width, height):
        self.SCREEN_BACKGROUND = background
        self.SCREEN_TITLE = title
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        pygame.display.set_caption(self.SCREEN_TITLE)

        self.background = pygame.image.load('/Users/polinapetrova/Coding/scratchrover_backgrounds_mars/Hebrus Valles.jpg')


    def update(self):
        """ 
        implement game logic updates 
        """
        pass

    def render(self):
        """ 
        implement rendering of game elements
        """
        pass


    pass
