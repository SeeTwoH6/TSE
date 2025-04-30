import tkinter as tk
import pygame as pg
from sys import exit
import random

#initialising module
pg.init()
pg.font.init()


info = pg.display.Info()
window_w = info.current_w
window_h = info.current_h

#sets the screen size and name of window
display_surface = pg.display.set_mode((window_w - 10, window_h - 50), pg.RESIZABLE)
pg.display.set_caption("Reaction Game")

#first background colour
colour1 = (52,131,191)
colour2 = (204,0,0)
colour3 = (128,189,102)
display_surface.fill(colour1)
pg.display.flip()

#intro text - reaction time 
font1 = pg.font.SysFont('arial', 150)
text1 = font1.render("Reaction Time Test", True, (255,255,255))
textRect1 = text1.get_rect()
textRect1.center = (window_w //2, window_h // 1.9)

#instructions text
font2 = pg.font.SysFont('arial', 40)
text2= font2.render("When the red box turns green, click as quickly as you can.", True, (255,255,255))
textRect2 = text1.get_rect()
textRect2.center = (window_w //1.86, window_h // 1.47)

#begin text
font3 = pg.font.SysFont('arial', 40)
text3= font3.render("Click anywhere to start.", True, (255,255,255))
textRect3 = text1.get_rect()
textRect3.center = (window_w //1.54, window_h // 1.38)

#red screen text
text4 = font1.render("Wait for green", True, (255,255,255))
textRect4 = text4.get_rect()
textRect4.center = (window_w //2, window_h // 1.7)

#red screen text
font4 = pg.font.SysFont('arial', 1000)
text5 = font4.render("...", True, (255,255,255))
textRect5 = text5.get_rect()
textRect5.center = (window_w //2, window_h // 7)

# Green screen text 
text6 = font1.render("Click Now", True, (255,255,255))
textRect6 = text6.get_rect()
textRect6.center = (window_w // 2, window_h // 1.7)

# Green screen text 
text7 = font4.render("...", True, (255,255,255))
textRect7 = text7.get_rect()
textRect7.center = (window_w // 2, window_h // 7)

#Result & Repeat Screen


running = True
red_screen = False
green_screen = False
repeat_screen = False

green_popup_time = random.randint(0,4000)
start_time = None


#keeps game running till exit
while running:

    if pg.mouse.get_pressed()[0]:
        red_screen = True
        
    display_surface.fill(colour1)  # Prevents overlapping text
    display_surface.blit(text1, textRect1)  # Draw the text
    display_surface.blit(text2, textRect2)  # Draw the text
    display_surface.blit(text3, textRect3)  # Draw the text
    pg.display.update()  # Update display after rendering text

    while red_screen:
        display_surface.fill(colour2)  # Prevents overlapping text
        display_surface.blit(text4, textRect4)  # Draw the text
        display_surface.blit(text5, textRect5)  # Draw the text
        pg.display.update()

        pg.time.wait(green_popup_time)
        red_screen = False
        green_screen = True
        break

    while green_screen:
        display_surface.fill(colour3)  # Green background
        display_surface.blit(text6, textRect6)  # "Click Now"
        display_surface.blit(text7, textRect7)  # "..."
        pg.display.update()
        
        start_time = pg.time.get_ticks()
       
        
        #if pg.mouse.get_pressed()[0]:
            #repeat_screen = True
            #green_screen = False
        #break
        
    while repeat_screen:
       display_surface.fill(colour1) 
       pg.display.update() 
   

        

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
