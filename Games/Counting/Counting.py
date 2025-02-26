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
cube = pg.image.load('Games/Counting/Images/cube.png')
cubeSize = (150,150)
cube = pg.transform.scale(cube, cubeSize)

#Set Framerate
clock = pg.time.Clock()

#Create the number of squares to generate
numOfCubes = random.randint(1,10)

while True:
    #Event Loop to check for player input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(bg, (0,0))

    offsetX = 0
    offsetY = 0
    for i in range(numOfCubes):
        screen.blit(cube, (500 + offsetX, 300 + offsetY))
        offsetX += 55
        offsetY += 28

    pg.display.update()
    clock.tick(60)