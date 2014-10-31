import sys
import pygame
from pygame.locals import *

pygame.init()
width = 300
height = 300
setDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Epic Game')

img = pygame.image.load('good_guy.png')
imgx = 10
imgy = 10

movement = 'null'
pixMove = 5
fps = 30

fpsTime = pygame.time.Clock()

yellow = (255,255,0)
red = (255,0,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (255,0,255)
green = (0,255,0)
black = (0,0,0)
def playerMove(direction):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = 'left'
            elif event.key == K_DOWN:
                direction = 'down'
            elif event.key == K_RIGHT:
                direction = 'right'
            elif event.key == K_UP:
                direction = 'up'
        elif event.type == KEYUP:
            direction = 'null'
    return direction
while True:
    setDisplay.fill(black)
    movement = playerMove(movement)
    if movement == 'down':
        imgy += pixMove
        if imgy > height - 100:
            img = pygame.transform.rotate(img, 90)
            #movement = 'right'
    elif movement == 'right':
        imgx += pixMove
        if imgx > width - 100:
            img = pygame.transform.rotate(img, 90)
            #movement = 'up'
    elif movement == 'up':
        imgy -= pixMove
        if imgy < 30:
            img = pygame.transform.rotate(img, 90)
            #movement = 'left'
    elif movement == 'left':
        imgx -= pixMove
        if imgx < 30:
            img = pygame.transform.rotate(img, 90)
            #movement = 'down'
        

    
    setDisplay.blit(img, (imgx,imgy))
    for event in pygame.event.get():
        #print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(fps)
