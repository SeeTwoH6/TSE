import tkinter as tk
import pygame as pg
from sys import exit

#The functionality of this game will depend on creating a random number of 3D cubes in a configuration then asking the user how many blocks there are whilst being timed.
#The game will start easy, blocks may only spawn on a 2D plane
#Difficulty can be increase by increasing the number of blocks the user has to count or by moving into the 3D plane

#Initialise Pygame
pg.init()

#Define screen 
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Counting Game")

#Set Framerate
clock = pg.time.Clock()

while True:
    #Event Loop to check for player input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    clock.tick(60)