import pygame as pg
import random
from sys import exit

pg.init()
pg.font.init()

info = pg.display.Info()
window_w = info.current_w
window_h = info.current_h

#sets the screen size and name of window
display_surface = pg.display.set_mode((window_w - 10, window_h - 50), pg.RESIZABLE)
pg.display.set_caption("Reaction Game")

# Colors
BLUE = (52,131,191)
RED = (204,0,0)
GREEN = (128,189,102)
WHITE = (255,255,255)

# Fonts
font_big = pg.font.SysFont('arial', 180)
font_dot = pg.font.SysFont('arial', 550)
font_small = pg.font.SysFont('arial', 50)

# Helper function to center text
def draw_centered_text(surface, text, font, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 + y_offset))
    surface.blit(text_surface, text_rect)

clock = pg.time.Clock()
game_state = "intro"
start_time = 0
reaction_time = 0
delay_time = 0
loop = 0
average_time = 0
reaction_times = []

while True and loop < 5:
    display_surface.fill(BLUE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if game_state == "intro":
                delay_time = random.randint(2000, 4000)
                trigger_time = pg.time.get_ticks() + delay_time
                game_state = "waiting"
            elif game_state == "ready":
                reaction_time = pg.time.get_ticks() - start_time
                game_state = "result"
            elif game_state == "result":
                game_state = "intro"

    if game_state == "intro":
        display_surface.fill(BLUE)
        draw_centered_text(display_surface, "Reaction Time Test", font_big, WHITE, y_offset=-40)
        draw_centered_text(display_surface, "When the red box turns green, click as quickly as you can.", font_small, WHITE, y_offset=70)
        draw_centered_text(display_surface, "Click anywhere to start", font_small, WHITE, y_offset=120)

    elif game_state == "waiting":
        display_surface.fill(RED)
        draw_centered_text(display_surface, "...", font_dot, WHITE, y_offset=-200)
        draw_centered_text(display_surface, "Wait for green", font_big, WHITE, y_offset=100)
        
        if pg.time.get_ticks() >= trigger_time:
            display_surface.fill(GREEN)
            draw_centered_text(display_surface, "CLICK NOW!", font_big, WHITE)
            start_time = pg.time.get_ticks()
            game_state = "ready"

    elif game_state == "ready":
        display_surface.fill(GREEN)
        draw_centered_text(display_surface, "CLICK NOW!", font_big, WHITE)

    elif game_state == "result":
        display_surface.fill(BLUE)
        draw_centered_text(display_surface, f"{reaction_time} ms", font_big, WHITE, y_offset=-20)
        reaction_times.append(reaction_time)
        
        if len(reaction_times) < 5:
            reaction_times.append(reaction_time)
            loop = len(reaction_times)
        
        if loop == 5:
            average_time = sum(reaction_times) / len(reaction_times)
            draw_centered_text(display_surface, "Reaction Time", font_small, WHITE, y_offset=-40)
            draw_centered_text(display_surface, f"{average_time:.2f} ms", font_big, WHITE, y_offset=80)
            draw_centered_text(display_surface, "Save your score to see how you compare", font_small, WHITE, y_offset=140)
        else:
            draw_centered_text(display_surface, "Click to keep going", font_small, WHITE, y_offset=80)
    pg.display.update()
    clock.tick(60)
