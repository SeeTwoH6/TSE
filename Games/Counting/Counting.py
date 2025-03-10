import tkinter as tk
import pygame as pg
import os
from sys import exit
import random

#The functionality of this game will depend on creating a random number of 3D cubes in a configuration then asking the user how many blocks there are whilst being timed.
#The game will start easy, blocks may only spawn on a 2D plane
#Difficulty can be increase by increasing the number of blocks the user has to count or by moving into the 3D plane

#Initialise Pygame
pg.init()

#Control Screen Size
os.environ['SDL_VIDEO_CENTERED'] = '1' #Called before pg.init()
info = pg.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h

#Define Screen 
screen = pg.display.set_mode((screenWidth - 10, screenHeight - 50), pg.RESIZABLE)
pg.display.set_caption("Counting Game")
bg = pg.Surface((screenWidth, screenHeight))
bg.fill('lightblue')

#Load the main image
cubeColours = ["redcube", "bluecube", "orangecube", "yellowcube", "pinkcube", "purplecube", "greencube", "cyancube", "lightbluecube"]

#Set Framerate
clock = pg.time.Clock()


#Create the number of squares to generate
level = 10
numOfCubes = random.randint(1,level)
answer = numOfCubes
blockLength = random.randint(1,10)
blockWidth = random.randint(1,5)
blockHeight = random.randint(1,4)
print(f"numOfCubes: {numOfCubes}" + '\n' +  f"blocklength: {blockLength}" + '\n' +  f"blockWidth: {blockWidth}" + '\n' + f"blockHeight: {blockHeight}")

class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cubeType = random.choice(cubeColours)  # Choose a fixed color at creation
        self.image = pg.image.load(f'Games/Counting/Images/{self.cubeType}.png')
        cubeSize = (275,150)
        self.image = pg.transform.scale(self.image, cubeSize)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

#Origin point for construction is (750, 300)
lineOffsetX = 55
lineOffsetY = 26
rowOffsetX = 0
rowOffsetY = 0
layerOffsetX = 0
layerOffsetY = 0
cubes = []

#startingX = 750
#startingY = 300
cubesPlaced = False
for layer in range(blockHeight):
    #print(f"Layer: {layer}")
    layerStartingX = 750
    layerStartingY = 300 - (64 * layer)
    for row in range(blockWidth):
        #print(f"Row: {row}")
        startingX = layerStartingX - (lineOffsetX * row)
        #print(f"Layer starting x: {layerStartingX}")
        startingY = layerStartingY + (lineOffsetY * row)
        #print(f"Starting X for the second layer: {startingX}")
        for line in range(blockLength):
            #print(f"Line: {line}")
            cubes.append(Cube(startingX + line * lineOffsetX, startingY + line * lineOffsetY))
            #print(f"Adding cube with positions: {startingX + line * lineOffsetX} and {startingY + line * lineOffsetY}")
            numOfCubes -= 1
            #print(f"Num of cubes remaining: {numOfCubes}")
            if numOfCubes <= 0:
                cubesPlaced = True
                break
        if cubesPlaced:
            break
    if cubesPlaced:
        break
        

'''
Testing Initial Positions
cube = pg.image.load(f'Games/Counting/Images/greencube.png')
cube = pg.transform.scale(cube, (275,150))
'''


while True:
    #Event Loop to check for player input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    '''
    Testing initial positions
    screen.blit(cube, (750,300))
    screen.blit(cube, (695,326))
    screen.blit(cube, (750,236))  
    '''
    screen.blit(bg, (0,0))
    
    for cube in cubes:
        cube.draw(screen)

    pg.display.update()
    clock.tick(60)