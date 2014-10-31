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

key = 'null'
pixMove = 5
fps = 30
gShotVisible = False
checkShot = False

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
            direction = 'null'
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
def drawGShot(imgx, imgy):
    gShotX = imgx - 16
    gShotY = imgy + 16
    gShotVisible = True
    setDisplay.blit(gShot, (gShotX, gShotY))#the +/- centers the start position
    return gShotVisible #returns boolean to check and see if the shot is drawn for the main function to see
def gShotMoveUp(gShotY,pixMove):
    pixMove = 5        
    return gShotY - pixMove

        
while True:
    setDisplay.fill(black)
    
    key = getKey(key) 
    
    if key == 'right' and imgx < width-36:
        imgx += pixMove     
    
    elif key == 'left' and imgx > 0:
        imgx -= pixMove
    elif key == 'shot':
        checkShot = True #need to set this to false after 'space' is let go
        
    drawGShot(imgx, imgy) #checks to see if the shot is drawn    
    playerDraw(img, imgx,imgy)
    gShotMoveUp(imgy, pixMove)#Doesn't actually move up yet
    
    if(bGuyY > height + 32):
       bGuyX = random.randrange(0, width)

    if (checkShot == True):
        gShotMoveUp(imgy+16, pixMove)
       
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
