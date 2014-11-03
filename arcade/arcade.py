import sys
import pygame
from pygame.locals import *
import random

pygame.init()
width = 300
height = 300
setDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Epic Game')

### Import images here###
img = pygame.image.load('good_guy.png')
bguy = pygame.image.load('bad_guy.png')
gShot = pygame.image.load('gGuyShot.png')
############################
imgx = width / 2
imgy = height - 40 

bGuyY = 0
bGuyX = (width/2) - 16

gShotX = imgx
gShotY = imgy

key = 'null'
pixMove = 5
fps = 30
gGuyShoot = False

fpsTime = pygame.time.Clock()

black = (0,0,0)
def playerDraw(img, imgx, imgy):
    setDisplay.blit(img, (imgx,imgy))
def getKey(direction):# gets the key and returns a direction to be processed in main function
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = 'left'
            elif event.key == K_RIGHT:
                direction = 'right'
            elif event.key == K_SPACE:
                direction = 'shot'
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                direction = 'null'
            elif event.key == K_RIGHT:
                direction = 'null'
            elif event.key == K_SPACE:
                direction = direction
                gGuyShoot = False
    return direction

def bGuyMoveDown(bGuyX,bGuyY, pixMove):
    pixMove = 5
    if bGuyY > height+32: #Added to loop BadGuy back to the top of the screen
        bGuyY = -32 #appears off the screen
        bGuyDraw(bguy, bGuyX, bGuyY)
        
    return bGuyY + pixMove

def hitTest(bGuyX, bGuyY, imgx, imgy): #not completed obviously
    return null
    #use this to test for collisions between two objects.. In the future

def bGuyDraw(bguy, bGuyX, bGuyY):
    if bGuyY < height:
        setDisplay.blit(bguy, (bGuyX, bGuyY))
def gShotDrawAndMove(gShot, x, y):
    if y > 0:
        setDisplay.blit(gShot, (x,y))
        
    return y - 1


        
while True:
    setDisplay.fill(black)
    
    key = getKey(key) 
    
    if key == 'right' and imgx < width-36:
        imgx += pixMove     
    
    elif key == 'left' and imgx > 0:
        imgx -= pixMove
    elif key == 'shot':
       gGuyShoot = True
        
      
    playerDraw(img, imgx,imgy)
    
    
    if(bGuyY > height + 32):
       bGuyX = random.randrange(0, width)

    if gGuyShoot == True:
         gShotY = gShotDrawAndMove(gShot, gShotX,gShotY)
       
    bGuyDraw(bguy, bGuyX, bGuyY) #Need to Allow random x positions

    bGuyY = bGuyMoveDown(bGuyX,bGuyY, pixMove)
    
    for event in pygame.event.get():
                
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN: #In theory this should be speeding up the bad guy when the down arrow is held. Doesn't work
            if event.key == K_DOWN:
                pixMove = 7
                print "Test"
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                pixMove = 4

        
    pygame.display.update()
    fpsTime.tick(fps)
