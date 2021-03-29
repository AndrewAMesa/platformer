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

    def parseText(self):
        self.count = 0
        file = open(self.level)
        line = file.readline()
        tempX = 0
        for x in range(0, len(line)):
            if line[x] == "i":
                self.startingSpotX = tempX
                self.startingSpotY = self.count
                self.BOARDWIDTH += 1
                tempX += 1
                self.lineList.append(line[x])
            elif line[x] != ',' and line[x] != '\n':
                self.BOARDWIDTH += 1
                tempX += 1
                self.lineList.append(line[x])
        self.count += 1
        while line:
            line = file.readline()
            tempX = 0
            for x in range(0, len(line)):
                if line[x] == "i":
                    self.startingSpotX = tempX
                    self.startingSpotY = self.count
                    tempX += 1
                    self.lineList.append(line[x])
                elif line[x] != "," and line[x] != "\n":
                    tempX += 1
                    self.lineList.append(line[x])
            self.count += 1
        self.count -= 1

MainObject = main()
MainObject.main()