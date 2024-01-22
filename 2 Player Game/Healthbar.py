import pygame

from Settings import *

# Health Bar Area
healthbar_area = pygame.Rect(min(0, SCREEN_WIDTH) , SCREEN_HEIGHT * UNPLAYABLE_AREA, SCREEN_WIDTH, SCREEN_HEIGHT - UNPLAYABLE_AREA)

def handle_healthbar(surface, x, y, w, h, current_hp, max_hp):
    # I got the idea from: http://www.codingwithruss.com/pygame/how-to-create-a-health-bar-in-pygame/
    # But because the original code was written as OOP, I rewrote the whole code to make it functional

    # Calculate health ratio
    ratio = current_hp / max_hp
    pygame.draw.rect(surface, "red", (x, y, w, h))
    pygame.draw.rect(surface, "green", (x, y, w * ratio, h))