import pygame
from pygame.locals import *


class Game:
    def __init__(self, background, title, width, height):
        self.SCREEN_BACKGROUND = background
        self.SCREEN_TITLE = title
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        # set title
        pygame.display.set_caption(self.SCREEN_TITLE)
        
        # load background image 
        # adjust to screen size
        self.BACKGROUND = pygame.image.load(background)
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


    def update(self):
        """ 
        implement game logic updates 
        """
        pass


    def render(self):
        """ 
        implement rendering of game elements
        """

        # draw background image onto screen
        self.SCREEN.blit(self.BACKGROUND, (0, 0))
        
        # update screen
        pygame.display.flip()


class GameObject:
    def __init__(self, destination, x, y, width, height):
        self.IMAGE = pygame.image.load(destination)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (width, height))
        self.RECT = self.IMAGE.get_rect()
        self.RECT.x = x
        self.RECT.y = y

    def update(self):
        # 
        pass

    def render(self, screen):
        # draw object on screen
        screen.blit(self.IMAGE, self.RECT)


    pass
