import pygame, sys
from pygame.locals import *
pygame.init()

class main():
    DISPLAYWIDTH = 15
    DISPLAYHEIGHT = 15
    TILESIZE = 30
    DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH * TILESIZE, DISPLAYHEIGHT * TILESIZE))

    def main(self):


        while True:

            #Event Loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #Update the Screen
            pygame.display.update()

MainObject = main()
MainObject.main()