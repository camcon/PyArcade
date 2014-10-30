import sys
import pygame
from pygame.locals import *
import random

pygame.init()
width = 300
height = 300
setDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Epic Game')

img = pygame.image.load('good_guy.png')
bguy = pygame.image.load('bad_guy.png')
imgx = width / 2
imgy = height - 40 

bGuyY = 0
bGuyX = (width/2) - 16

movement = 'null'
pixMove = 5
fps = 30

fpsTime = pygame.time.Clock()

black = (0,0,0)
def playerDraw(img, imgx, imgy):
    setDisplay.blit(img, (imgx,imgy))
def getKey(direction):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = 'left'
            elif event.key == K_RIGHT:
                direction = 'right'           
        elif event.type == KEYUP:
            direction = 'null'
    return direction

def bGuyMoveDown(bGuyY, pixMove):
    pixMove = 2
    return bGuyY + pixMove    
def bGuyDraw(bguy, bGuyX, bGuyY):
    if bGuyY < height-32:
        setDisplay.blit(bguy, (bGuyX, bGuyY))
while True:
    setDisplay.fill(black)
    
    movement = getKey(movement)
    
    
    if movement == 'right' and imgx < width-36:
        imgx += pixMove      
    
    elif movement == 'left' and imgx > 0:
        imgx -= pixMove
        
    playerDraw(img, imgx,imgy)
    bGuyDraw(bguy, bGuyX, bGuyY)
    bGuyY = bGuyMoveDown(bGuyY, pixMove)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(fps)
