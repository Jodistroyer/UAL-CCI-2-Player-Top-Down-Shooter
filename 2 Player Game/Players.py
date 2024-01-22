import pygame

from Settings import *

# Create the players
player1 = pygame.Rect(PLAYER1_XSPAWN, PLAYER1_YSPAWN, PLAYER_SIZE, PLAYER_SIZE)
player2 = pygame.Rect(PLAYER2_XSPAWN, PLAYER2_YSPAWN, PLAYER_SIZE, PLAYER_SIZE)

def handle_players():

    keys = pygame.key.get_pressed()

    # Player 1 Controls
    if keys[pygame.K_a]:
        player1.x -= PLAYER1_SPEED
    if keys[pygame.K_d]:
        player1.x += PLAYER1_SPEED
    if keys[pygame.K_w]:
        player1.y -= PLAYER1_SPEED
    if keys[pygame.K_s]:
        player1.y += PLAYER1_SPEED
    
    # Player 2 Controls
    if keys[pygame.K_LEFT]:
        player2.x -= PLAYER2_SPEED
    if keys[pygame.K_RIGHT]:
        player2.x += PLAYER2_SPEED
    if keys[pygame.K_UP]:
        player2.y -= PLAYER2_SPEED
    if keys[pygame.K_DOWN]:
        player2.y += PLAYER2_SPEED

    # Set maximum player boundaries
    player1.x = max(0, min(player1.x, SCREEN_WIDTH - PLAYER_SIZE))
    player1.y = max(0, min(player1.y, SCREEN_HEIGHT * UNPLAYABLE_AREA - PLAYER_SIZE))
    player2.x = max(0, min(player2.x, SCREEN_WIDTH - PLAYER_SIZE))
    player2.y = max(0, min(player2.y, SCREEN_HEIGHT * UNPLAYABLE_AREA - PLAYER_SIZE))
