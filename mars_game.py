import pygame
from pygame.locals import *
from game import Game

def main():
    pygame.init()
    
    """ initialise Game object """

    game = Game('')

    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Mars rover game')
    
    """ fill background """

    background = pygame.Surface(screen.get_size()) 
    background = background.convert() 
    # fill background with white
    background.fill((255, 255, 255))

    """ display text """

    font = pygame.font.Font(None, 36)
    # create text object
    # (rendered text, anti-aliased Y/N, text colour)
    text = font.render("Hello", 1, (10, 10, 10))
    # gets rectangle for text
    textpos = text.get_rect()

    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    """ blit everything to screen """
    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    """ event loop """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()