import pygame
from pygame.locals import *

def main():
    """ game main function """

    pygame.init()
    
    """ initialise game screen """
    
    # make display screen 
    # (width, height)
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Mars rover game')
    
    """ fill background """

    # create surface object
    background = pygame.Surface(screen.get_size()) 
    # convert surface to single pixel format
    background = background.convert() 
    # fill background with white
    background.fill((255, 255, 255))

    """ display text """

    # create font object
    # (font to use, size of font)
    font = pygame.font.Font(None, 36)
    # create text object
    # (rendered text, anti-aliased Y/N, text colour)
    text = font.render("Hello", 1, (10, 10, 10))
    # gets rectangle for text
    textpos = text.get_rect()
    # set text centre same as background centre
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    """ blit everything to screen """
    
    # blitting: rendering objects (copy object pixels to destination object)
    
    # blit text onto background
    # blit background onto screen
    screen.blit(background, (0, 0))
    # update display
    pygame.display.flip()

    """ event loop """

    # check for pygame events (user input)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()