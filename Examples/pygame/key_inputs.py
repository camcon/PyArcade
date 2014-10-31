import pygame
import sys
from pygame.locals import *
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (175,0,0)
bg = black

fps = 30
width = 800
height = 600
cellSize = 10

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

deadZones = []
def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs (text, font, tcolor):
    textSurface = font.render(text, True, tcolor)
    return textSurface, textSurface.get_rect()

def msgSurface(text, textColor):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
    titleTextRect.center = (int(width/2), int(height/2))
    setDisplay.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press key to continure', smallText, white)
    typTextRect.center = (int(width/2),int(height/2)+120)
    setDisplay.blit(typTextSurf, typTextRect)
    pygame.display.update()
    fpsTime.tick()

    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            fpsTime.tick()

    runGame()
def evilMove(evilGuy):
    evilCoords = []
    # Returns either -1, 0, or a 1
    randomMovex = random.randrange(-1,2)
    randomMovey = random.randrange(-1,2)
    newCell = {'x':evilGuy[0]['x']+randomMovex, 'y':evilGuy[0]['y'] + randomMovey}

    if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > width/cellSize or newCell['y'] > height/cellSize):
        newCell = {'x': width/(2*cellSize), 'y': height/(2*cellSize)}
    
    del evilGuy[-1]

    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])
    deadZones.append(evilCoords)
    evilGuy.insert(0,newCell)
    
    
def runGame():
    global deadZones
    startx = 5
    starty = 5
    coords = [{'x':startx, 'y':starty}]
    evilCoords1 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords2 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords3 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords4 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords5 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords6 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords7 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords8 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    evilCoords9 = [{'x': width/(2*cellSize), 'y': height/(2*cellSize)}]
    
    direction = RIGHT
    
    isAlive = 'yes'

    while True:

        while isAlive == 'yes':
            deadZones = []
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction = LEFT
                    elif event.key == K_RIGHT:
                        direction = RIGHT
                    elif event.key == K_DOWN:
                        direction = DOWN
                    elif event.key == K_UP:
                        direction = UP

            if direction == UP:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']-1}
            elif direction == DOWN:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']+1}
            elif direction == LEFT:
                newCell = {'x':coords[0]['x']-1, 'y':coords[0]['y']}
            elif direction == RIGHT:
                newCell = {'x':coords[0]['x']+1, 'y':coords[0]['y']}           
            del coords[-1]


            coords.insert(0, newCell)
            setDisplay.fill(bg)

            evilMove(evilCoords1)
            evilMove(evilCoords2)
            evilMove(evilCoords3)
            evilMove(evilCoords4)
            evilMove(evilCoords5)
            evilMove(evilCoords6)
            evilMove(evilCoords7)
            evilMove(evilCoords8)
            evilMove(evilCoords9)
            
            drawCell(coords, white)
            drawCell(evilCoords1, red)
            drawCell(evilCoords2, red)
            drawCell(evilCoords3, red)
            drawCell(evilCoords4, red)
            drawCell(evilCoords5, red)
            drawCell(evilCoords6, red)
            drawCell(evilCoords7, red)
            drawCell(evilCoords8, red)
            drawCell(evilCoords9, red)

            currentPos = [newCell['x'], newCell['y']]

            for eachDeathCoord in deadZones:
                if eachDeathCoord == currentPos:
                    isAlive = 'no'
            
            pygame.display.update()
            fpsTime.tick(fps)


            if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > width/cellSize or newCell['y'] > height/cellSize):
                isAlive = 'no'
                
        msgSurface('You Lose!', red)

def drawCell(coords, ccolor):
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize, cellSize)
        pygame.draw.rect(setDisplay, ccolor, makeCell)

while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((width, height))
    pygame.display.set_caption('controlling')
    runGame()
