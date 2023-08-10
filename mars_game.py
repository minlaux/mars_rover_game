import pygame
from pygame.locals import *
from game import Game, GameObject

def main():
    pygame.init()
    
    # initialise Game object
    game = Game('Hebrus Valles.jpg', 'Mars Rover Game', 150, 50)

    # create destination
    dest = GameObject('Gusev Crate.jpg', 375, 50, 50, 50)

    """ event loop """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        game.update()
        game.render()


if __name__ == '__main__': main()