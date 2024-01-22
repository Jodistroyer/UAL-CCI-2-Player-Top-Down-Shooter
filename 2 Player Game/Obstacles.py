import pygame
import random

from Settings import *
from Players import *

# Obstacle List
portals = []

def handle_obstacles():
    # This makes sure that the obstacles generate randomly, 
    # While also not spawning at the player spawn, and also not making it create portals infinitely when run in Main Game loop
    if not portals:
        for _ in range(PORTAL_AMOUNT):
            
            portal = pygame.Rect(random.randint(0, SCREEN_WIDTH - 100) 
                    + 50, random.randint(0, SCREEN_HEIGHT * UNPLAYABLE_AREA - 100) 
                    + 50, PORTAL_WIDTH, PORTAL_HEIGHT)
            portals.append(portal)

    # Portal Teleportation
    for portal in portals:
        if pygame.Rect(portal).colliderect(player1):
            player1.x = random.randint(0, SCREEN_WIDTH)
            player1.y = random.randint(0, SCREEN_HEIGHT)

        if pygame.Rect(portal).colliderect(player2):
            player2.x = random.randint(0, SCREEN_WIDTH)
            player2.y = random.randint(0, SCREEN_HEIGHT)