import pygame
import math
import random

from Settings import *
from Obstacles import *
from Players import *
from Healthbar import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("1v1 Portal War")

# Default Game state
game_state = "start_menu"

# Player Health
player1_health = 100
player2_health = 100

# Powerup List
medkits = []

# Bullets 1 Directions List
player1_bullets_list_left = []
player1_bullets_list_left_up = []
player1_bullets_list_left_down = []

player1_bullets_list_right= []
player1_bullets_list_right_up= []
player1_bullets_list_right_down= []

player1_bullets_list_up = []
player1_bullets_list_down = []

# Bullets 2 Directions Lists
player2_bullets_list_left = []
player2_bullets_list_left_up = []
player2_bullets_list_left_down = []

player2_bullets_list_right= []
player2_bullets_list_right_up= []
player2_bullets_list_right_down= []

player2_bullets_list_up = []
player2_bullets_list_down = []

def handle_powerups():

    global player1_health
    global player2_health
    # This makes sure that the obstacles generate randomly, 
    # While also not spawning at the player spawn, and also not making it create portals infinitely when run in Main Game loop
    if not medkits:
        for _ in range(MEDKIT_AMOUNT):
            medkit = pygame.Rect(random.randint(0, SCREEN_WIDTH - 100) 
                    + 50, random.randint(0, SCREEN_HEIGHT * UNPLAYABLE_AREA - 100) 
                    + 50, MEDKIT_WIDTH, MEDKIT_HEIGHT)
            medkits.append(medkit)

    # Portal Teleportation
    for medkit in medkits:

        if pygame.Rect(medkit).colliderect(player1) and player1_health < MAX_HP:
            player1_health += MEDKIT_HEAL
            medkits.remove(medkit)
            # Set health cap for max hp
            if player1_health > MAX_HP:
                player1_health = MAX_HP 

        if pygame.Rect(medkit).colliderect(player2) and player2_health < MAX_HP:
            player2_health += MEDKIT_HEAL
            medkits.remove(medkit)
            # Set health cap for max hp
            if player2_health > MAX_HP:
                player2_health = MAX_HP

def handle_player1_bullets():
    # Got the idea of append + remove bullets from this pygame zero course
    # https://electronstudio.github.io/pygame-zero-book/chapters/shooter.html#player-bullets
    # But I rewrote the code completely to fit pygame and my code

    global player2_health
    keys = pygame.key.get_pressed()

    # Player 1 Bullets Left
    if keys[pygame.K_a] and len(player1_bullets_list_left) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_left = {"x" : player1.x, "y" : player1.y}
        player1_bullets_list_left.append(player1_bullet_left)
    for player1_bullet_left in player1_bullets_list_left:
            #Set Player 1 Bullet Bounds and Bullet Speed
            player1_bullet_left["x"] -= BULLET_SPEED
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_left["x"], player1_bullet_left["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_left.remove(player1_bullet_left)
            elif (
                player1_bullet_left["x"] > SCREEN_WIDTH
                or player1_bullet_left["x"] < 0 
                or player1_bullet_left["y"] > SCREEN_WIDTH
                or player1_bullet_left["y"] < 0
            ):
                player1_bullets_list_left.remove(player1_bullet_left)
            # Check Portal to Player collision
            for portal in portals:
                #This avoids ValueError by always checking if there is a bullet in the list to remove
                if player1_bullet_left in player1_bullets_list_left:
                    if pygame.Rect(player1_bullet_left["x"], player1_bullet_left["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_left.remove(player1_bullet_left)        

    # Player 1 Bullets Left, Up
    if keys[pygame.K_a] and keys[pygame.K_w] and len(player1_bullets_list_left_up) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_left_up = {"x" : player1.x, "y" : player1.y, "angle" : math.radians(75)}
        player1_bullets_list_left_up.append(player1_bullet_left_up)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_left_up in player1_bullets_list_left_up:
            player1_bullet_left_up["x"] -= BULLET_SPEED * player1_bullet_left_up["angle"]
            player1_bullet_left_up["y"] -= BULLET_SPEED * player1_bullet_left_up["angle"]
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_left_up["x"], player1_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_left_up.remove(player1_bullet_left_up)
            elif (
                player1_bullet_left_up["x"] > SCREEN_WIDTH 
                or player1_bullet_left_up["x"] < 0 
                or player1_bullet_left_up["y"] > SCREEN_WIDTH 
                or player1_bullet_left_up["y"] < 0
            ):
                player1_bullets_list_left_up.remove(player1_bullet_left_up) 
            # Check Portal to Player collision
            for portal in portals:
                #This avoids ValueError by always checking if there is a bullet in the list to remove
                if player1_bullet_left_up in player1_bullets_list_left_up:
                    if pygame.Rect(player1_bullet_left_up["x"], player1_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_left_up.remove(player1_bullet_left_up)

    # Player 1 Bullets Left, Down
    if keys[pygame.K_a] and keys[pygame.K_s] and len(player1_bullets_list_left_down) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_left_down = {"x" : player1.x, "y" : player1.y, "angle" : math.radians(105)}
        player1_bullets_list_left_down.append(player1_bullet_left_down)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_left_down in player1_bullets_list_left_down:
            # Bullet Angle
            player1_bullet_left_down["x"] -= BULLET_SPEED * player1_bullet_left_down["angle"]
            player1_bullet_left_down["y"] += BULLET_SPEED * player1_bullet_left_down["angle"]
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_left_down["x"], player1_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_left_down.remove(player1_bullet_left_down)
            elif (
                player1_bullet_left_down["x"] > SCREEN_WIDTH 
                or player1_bullet_left_down["x"] < 0 
                or player1_bullet_left_down["y"] > SCREEN_WIDTH 
                or player1_bullet_left_down["y"] < 0
                or pygame.Rect(player1_bullet_left_down["x"], player1_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)
            ):
                player1_bullets_list_left_down.remove(player1_bullet_left_down) 
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_left_down in player1_bullets_list_left_down:
                    if pygame.Rect(player1_bullet_left_down["x"], player1_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_left_down.remove(player1_bullet_left_down)

    # Player 1 Bullets Right
    if keys[pygame.K_d] and len(player1_bullets_list_right) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_right = {"x" : player1.x, "y" : player1.y}
        player1_bullets_list_right.append(player1_bullet_right)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_right in player1_bullets_list_right:
            # Bullet Angle
            player1_bullet_right["x"] += BULLET_SPEED
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_right["x"], player1_bullet_right["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_right.remove(player1_bullet_right)
            elif (
                player1_bullet_right["x"] > SCREEN_WIDTH 
                or player1_bullet_right["x"] < 0 
                or player1_bullet_right["y"] > SCREEN_WIDTH 
                or player1_bullet_right["y"] < 0
            ):
                player1_bullets_list_right.remove(player1_bullet_right) 
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_right in player1_bullets_list_right:
                    if pygame.Rect(player1_bullet_right["x"], player1_bullet_right["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_right.remove(player1_bullet_right)

    # Player 1 Bullets Right, Up
    if keys[pygame.K_d] and keys[pygame.K_w] and len(player1_bullets_list_right_up) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_right_up = {"x" : player1.x, "y" : player1.y, "angle" : math.radians(75)}
        player1_bullets_list_right_up.append(player1_bullet_right_up)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_right_up in player1_bullets_list_right_up:
            player1_bullet_right_up["x"] += BULLET_SPEED * player1_bullet_right_up["angle"]
            player1_bullet_right_up["y"] -= BULLET_SPEED * player1_bullet_right_up["angle"]
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_right_up["x"], player1_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_right_up.remove(player1_bullet_right_up)
            elif (
                player1_bullet_right_up["x"] > SCREEN_WIDTH 
                or player1_bullet_right_up["x"] < 0 
                or player1_bullet_right_up["y"] > SCREEN_WIDTH 
                or player1_bullet_right_up["y"] < 0
            ):
                player1_bullets_list_right_up.remove(player1_bullet_right_up) 
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_right_up in player1_bullets_list_right_up:
                    if pygame.Rect(player1_bullet_right_up["x"], player1_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_right_up.remove(player1_bullet_right_up)

    # Player 1 Bullets Right, Down
    if keys[pygame.K_d] and keys[pygame.K_s] and len(player1_bullets_list_right_down) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_right_down = {"x" : player1.x, "y" : player1.y, "angle" : math.radians(75)}
        player1_bullets_list_right_down.append(player1_bullet_right_down)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_right_down in player1_bullets_list_right_down:
            player1_bullet_right_down["x"] += BULLET_SPEED * player1_bullet_right_down["angle"]
            player1_bullet_right_down["y"] += BULLET_SPEED * player1_bullet_right_down["angle"]
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_right_down["x"], player1_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_right_down.remove(player1_bullet_right_down)
            elif (
                player1_bullet_right_down["x"] > SCREEN_WIDTH 
                or player1_bullet_right_down["x"] < 0 
                or player1_bullet_right_down["y"] > SCREEN_WIDTH 
                or player1_bullet_right_down["y"] < 0
                or pygame.Rect(player1_bullet_right_down["x"], player1_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)
            ):
                player1_bullets_list_right_down.remove(player1_bullet_right_down) 
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_right_down in player1_bullets_list_right_down:
                    if pygame.Rect(player1_bullet_right_down["x"], player1_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_right_down.remove(player1_bullet_right_down)

    # Player 1 Bullets Up
    if keys[pygame.K_w] and len(player1_bullets_list_up) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_up = {"x" : player1.x, "y" : player1.y}
        player1_bullets_list_up.append(player1_bullet_up)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_up in player1_bullets_list_up:
            player1_bullet_up["y"] -= BULLET_SPEED
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_up["x"], player1_bullet_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_up.remove(player1_bullet_up)
            elif (
                player1_bullet_up["x"] > SCREEN_WIDTH 
                or player1_bullet_up["x"] < 0 
                or player1_bullet_up["y"] > SCREEN_WIDTH 
                or player1_bullet_up["y"] < 0
            ):
                player1_bullets_list_up.remove(player1_bullet_up)
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_up in player1_bullets_list_up:
                    if pygame.Rect(player1_bullet_up["x"], player1_bullet_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_up.remove(player1_bullet_up)

    # Player 1 Bullets Down
    if keys[pygame.K_s] and len(player1_bullets_list_down) < PLAYER1_MAX_BULLETS and keys[pygame.K_q]:
        player1_bullet_down = {"x" : player1.x, "y" : player1.y}
        player1_bullets_list_down.append(player1_bullet_down)
    #Set Player 1 Bullet Bounds and Bullet Speed
    for player1_bullet_down in player1_bullets_list_down:
            player1_bullet_down["y"] += BULLET_SPEED
            # Player 1 Bullet Damage
            if pygame.Rect(player1_bullet_down["x"], player1_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
                player2_health -= PLAYER1_BULLET_DAMAGE
                player1_bullets_list_down.remove(player1_bullet_down)
            elif (
                player1_bullet_down["x"] > SCREEN_WIDTH 
                or player1_bullet_down["x"] < 0 
                or player1_bullet_down["y"] > SCREEN_WIDTH 
                or player1_bullet_down["y"] < 0
                or pygame.Rect(player1_bullet_down["x"], player1_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)
            ):
                player1_bullets_list_down.remove(player1_bullet_down)
            # Check Portal to Player collision
            for portal in portals:
                if player1_bullet_down in player1_bullets_list_down:
                    if pygame.Rect(player1_bullet_down["x"], player1_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player1_bullets_list_down.remove(player1_bullet_down)
    
def handle_player2_bullets():
    global player1_health
    keys = pygame.key.get_pressed()
    
    # Player 2 Bullets Left
    if keys[pygame.K_LEFT] and len(player2_bullets_list_left) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_left = {"x" : player2.x, "y" : player2.y}
        player2_bullets_list_left.append(player2_bullet_left)
    # Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_left in player2_bullets_list_left:
            player2_bullet_left["x"] -= BULLET_SPEED
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_left["x"], player2_bullet_left["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_left.remove(player2_bullet_left)
            elif (
                player2_bullet_left["x"] > SCREEN_WIDTH 
                or player2_bullet_left["x"] < 0 
                or player2_bullet_left["y"] > SCREEN_WIDTH 
                or player2_bullet_left["y"] < 0
            ):
                player2_bullets_list_left.remove(player2_bullet_left)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_left in player2_bullets_list_left:
                    if pygame.Rect(player2_bullet_left["x"], player2_bullet_left["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_left.remove(player2_bullet_left)

    # Player 2 Bullets Left, Up
    if keys[pygame.K_LEFT] and keys[pygame.K_UP] and len(player2_bullets_list_left_up) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_left_up = {"x" : player2.x, "y" : player2.y, "angle" : math.radians(75)}
        player2_bullets_list_left_up.append(player2_bullet_left_up)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_left_up in player2_bullets_list_left_up:
            player2_bullet_left_up["x"] -= BULLET_SPEED * player2_bullet_left_up["angle"]
            player2_bullet_left_up["y"] -= BULLET_SPEED * player2_bullet_left_up["angle"]
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_left_up["x"], player2_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_left_up.remove(player2_bullet_left_up)
            elif (
                player2_bullet_left_up["x"] > SCREEN_WIDTH 
                or player2_bullet_left_up["x"] < 0 
                or player2_bullet_left_up["y"] > SCREEN_WIDTH 
                or player2_bullet_left_up["y"] < 0
            ):
                player2_bullets_list_left_up.remove(player2_bullet_left_up)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_left_up in player2_bullets_list_left_up:
                    if pygame.Rect(player2_bullet_left_up["x"], player2_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_left_up.remove(player2_bullet_left_up)

    # Player 2 Bullets Left, Down
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and len(player2_bullets_list_left_down) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_left_down = {"x" : player2.x, "y" : player2.y, "angle" : math.radians(75)}
        player2_bullets_list_left_down.append(player2_bullet_left_down)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_left_down in player2_bullets_list_left_down:
            player2_bullet_left_down["x"] -= BULLET_SPEED * player2_bullet_left_down["angle"]
            player2_bullet_left_down["y"] += BULLET_SPEED * player2_bullet_left_down["angle"]
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_left_down["x"], player2_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_left_down.remove(player2_bullet_left_down)
            elif (
                player2_bullet_left_down["x"] > SCREEN_WIDTH 
                or player2_bullet_left_down["x"] < 0 
                or player2_bullet_left_down["y"] > SCREEN_WIDTH 
                or player2_bullet_left_down["y"] < 0 
                or pygame.Rect(player2_bullet_left_down["x"], player2_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)
            ):
                player2_bullets_list_left_down.remove(player2_bullet_left_down)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_left_down in player2_bullets_list_left_down:
                    if pygame.Rect(player2_bullet_left_down["x"], player2_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_left_down.remove(player2_bullet_left_down)


    # Player 2 Bullets Right
    if keys[pygame.K_RIGHT] and len(player2_bullets_list_right) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_right = {"x" : player2.x, "y" : player2.y}
        player2_bullets_list_right.append(player2_bullet_right)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_right in player2_bullets_list_right:
            player2_bullet_right["x"] += BULLET_SPEED
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_right["x"], player2_bullet_right["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_right.remove(player2_bullet_right)
            elif (
                player2_bullet_right["x"] > SCREEN_WIDTH 
                or player2_bullet_right["x"] < 0 
                or player2_bullet_right["y"] > SCREEN_WIDTH 
                or player2_bullet_right["y"] < 0
            ):
                player2_bullets_list_right.remove(player2_bullet_right)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_right in player2_bullets_list_right:
                    if pygame.Rect(player2_bullet_right["x"], player2_bullet_right["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_right.remove(player2_bullet_right)

    # Player 2 Bullets Right, Up
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP] and len(player2_bullets_list_right_up) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_right_up = {"x" : player2.x, "y" : player2.y, "angle" : math.radians(75)}
        player2_bullets_list_right_up.append(player2_bullet_right_up)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_right_up in player2_bullets_list_right_up:
            player2_bullet_right_up["x"] += BULLET_SPEED * player2_bullet_right_up["angle"]
            player2_bullet_right_up["y"] -= BULLET_SPEED * player2_bullet_right_up["angle"]
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_right_up["x"], player2_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_right_up.remove(player2_bullet_right_up)
            elif (
                player2_bullet_right_up["x"] > SCREEN_WIDTH 
                or player2_bullet_right_up["x"] < 0 
                or player2_bullet_right_up["y"] > SCREEN_WIDTH 
                or player2_bullet_right_up["y"] < 0
            ):
                player2_bullets_list_right_up.remove(player2_bullet_right_up)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_right_up in player2_bullets_list_right_up:
                    if pygame.Rect(player2_bullet_right_up["x"], player2_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_right_up.remove(player2_bullet_right_up)

    # Player 2 Bullets Right, Down
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and len(player2_bullets_list_right_down) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_right_down = {"x" : player2.x, "y" : player2.y, "angle" : math.radians(75)}
        player2_bullets_list_right_down.append(player2_bullet_right_down)
        #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_right_down in player2_bullets_list_right_down:
                player2_bullet_right_down["x"] += BULLET_SPEED * player2_bullet_right_down["angle"]
                player2_bullet_right_down["y"] += BULLET_SPEED * player2_bullet_right_down["angle"]
                # Player 2 Bullet Damage
                if pygame.Rect(player2_bullet_right_down["x"], player2_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                    player1_health -= PLAYER2_BULLET_DAMAGE
                    player2_bullets_list_right_down.remove(player2_bullet_right_down)
                elif (
                    player2_bullet_right_down["x"] > SCREEN_WIDTH 
                    or player2_bullet_right_down["x"] < 0 
                    or player2_bullet_right_down["y"] > SCREEN_WIDTH 
                    or player2_bullet_right_down["y"] < 0
                    or pygame.Rect(player2_bullet_right_down["x"], player2_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)
                ):
                    player2_bullets_list_right_down.remove(player2_bullet_right_down)
                # Check Portal to Player collision
                for portal in portals:
                    if player2_bullet_right_down in player2_bullets_list_right_down:
                        if pygame.Rect(player2_bullet_right_down["x"], player2_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                            player2_bullets_list_right_down.remove(player2_bullet_right_down)


    # Player 2 Bullets Up
    if keys[pygame.K_UP] and len(player2_bullets_list_up) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_up = {"x" : player2.x, "y" : player2.y}
        player2_bullets_list_up.append(player2_bullet_up)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_up in player2_bullets_list_up:
            player2_bullet_up["y"] -= BULLET_SPEED
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_up["x"], player2_bullet_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_up.remove(player2_bullet_up)
            elif (
                player2_bullet_up["x"] > SCREEN_WIDTH 
                or player2_bullet_up["x"] < 0 
                or player2_bullet_up["y"] > SCREEN_WIDTH 
                or player2_bullet_up["y"] < 0
            ):
                player2_bullets_list_up.remove(player2_bullet_up)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_up in player2_bullets_list_up:
                    if pygame.Rect(player2_bullet_up["x"], player2_bullet_up["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_up.remove(player2_bullet_up)

    # Player 2 Bullets Down
    if keys[pygame.K_DOWN] and len(player2_bullets_list_down) < PLAYER2_MAX_BULLETS and keys[pygame.K_RSHIFT]:
        player2_bullet_down = {"x" : player2.x, "y" : player2.y}
        player2_bullets_list_down.append(player2_bullet_down)
    #Set Player 2 Bullet Bounds and Bullet Speed
    for player2_bullet_down in player2_bullets_list_down:
            player2_bullet_down["y"] += BULLET_SPEED
            # Player 2 Bullet Damage
            if pygame.Rect(player2_bullet_down["x"], player2_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player1):
                player1_health -= PLAYER2_BULLET_DAMAGE
                player2_bullets_list_down.remove(player2_bullet_down)
            elif (
                player2_bullet_down["x"] > SCREEN_WIDTH 
                or player2_bullet_down["x"] < 0 
                or player2_bullet_down["y"] > SCREEN_WIDTH 
                or player2_bullet_down["y"] < 0
                or pygame.Rect(player2_bullet_down["x"], player2_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(healthbar_area)

            ):
                player2_bullets_list_down.remove(player2_bullet_down)
            # Check Portal to Player collision
            for portal in portals:
                if player2_bullet_down in player2_bullets_list_down:
                    if pygame.Rect(player2_bullet_down["x"], player2_bullet_down["y"], BULLET_SIZE, BULLET_SIZE).colliderect(portal):
                        player2_bullets_list_down.remove(player2_bullet_down)

def draw_game_start_menu():
    screen.fill(WHITE)

    # Highlighted Word
    font_highlight = pygame.font.SysFont('arial', 36, True)
    highlighted_word = font_highlight.render('PLAYER 1 vs PLAYER 2', True, GREEN)
    screen.blit(highlighted_word, (SCREEN_WIDTH / 2 - highlighted_word.get_width() / 2, SCREEN_HEIGHT * 0.1 - highlighted_word.get_height() / 2))

    # Player 1 Instructions (Left Side)
    font = pygame.font.SysFont('arial', 24)
    player1_instructions = font.render('Player 1:', True, RED)
    player1_move_instructions = font.render('WASD to move', True, BLACK)
    player1_shoot_instructions = font.render('WASD + Q to shoot', True, BLACK)
    screen.blit(player1_instructions, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.2 - player1_instructions.get_height()))
    screen.blit(player1_move_instructions, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.2))
    screen.blit(player1_shoot_instructions, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.2 + player1_shoot_instructions.get_height()))
    
    # Player 2 Instructions (Right Side)
    player2_instructions = font.render('Player 2:', True, BLUE)
    player2_move_instructions = font.render('Arrow keys to move', True, BLACK)
    player2_shoot_instructions = font.render('Arrow keys + Shift to shoot', True, BLACK)
    screen.blit(player2_instructions, (SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.2 - player2_instructions.get_height()))
    screen.blit(player2_move_instructions, (SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.2))
    screen.blit(player2_shoot_instructions, (SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.2 + player2_shoot_instructions.get_height()))
    
    # Title and Start Button
    font_title = pygame.font.SysFont('arial', 40)
    title = font_title.render('Portal War', True, BLACK)
    start_button = font_title.render('Press SPACE to play', True, BLACK)
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_HEIGHT * 0.2 - title.get_height() / 2))
    screen.blit(start_button, (SCREEN_WIDTH / 2 - start_button.get_width() / 2, SCREEN_HEIGHT * 0.8 - start_button.get_height() / 2))
    
    
    # Game Rules Square Sizes
    square_size = 100
    num_squares = 4
    spacing = 60

    # Total width between squares
    total_width = num_squares * square_size + (num_squares - 1) * spacing

    # Starting x-coordinate for first square
    start_x = (SCREEN_WIDTH - total_width) / 2

    # Draw Square 1 (Red)
    pygame.draw.rect(screen, RED, (start_x, SCREEN_HEIGHT * 0.5, square_size, square_size))
    square1_text = font.render('Player 1', True, RED)
    screen.blit(square1_text, (start_x + square_size / 2 - square1_text.get_width() / 2, SCREEN_HEIGHT * 0.5 + square_size + 10))

    # Draw Square 2 (Green)
    start_x += square_size + spacing
    pygame.draw.rect(screen, GREEN, (start_x, SCREEN_HEIGHT * 0.5, square_size, square_size))
    square2_text = font.render('Heal Health', True, BLACK)
    screen.blit(square2_text, (start_x + square_size / 2 - square2_text.get_width() / 2, SCREEN_HEIGHT * 0.5 + square_size + 10))

    # Draw Square 3 (Black)
    start_x += square_size + spacing
    pygame.draw.rect(screen, BLACK, (start_x, SCREEN_HEIGHT * 0.5, square_size, square_size))
    square3_text = font.render('Teleport Randomly', True, BLACK)
    screen.blit(square3_text, (start_x + square_size / 2 - square3_text.get_width() / 2, SCREEN_HEIGHT * 0.5 + square_size + 10))

    # Draw Square 4 (Blue)
    start_x += square_size + spacing
    pygame.draw.rect(screen, BLUE, (start_x, SCREEN_HEIGHT * 0.5, square_size, square_size))
    square4_text = font.render('Player 2', True, BLUE)
    screen.blit(square4_text, (start_x + square_size / 2 - square4_text.get_width() / 2, SCREEN_HEIGHT * 0.5 + square_size + 10))

    pygame.display.update()

def draw_game_over_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)

   # Winner Screens
   if player1_health == 0:
        title = font.render('Player 2 wins', True, BLUE)
   if player2_health == 0:
        title = font.render('Player 1 wins', True, RED)
   if player2_health == 0 and player1_health == 0:
        title = font.render('DRAW', True, WHITE)

   # Draw Game Over Screen
   restart_button = font.render('Press R to Restart', True, WHITE)
   quit_button = font.render('Press X to Quit', True, WHITE)
   screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
   screen.blit(restart_button, (SCREEN_WIDTH/2 - restart_button.get_width()/2, SCREEN_HEIGHT/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 + quit_button.get_height()/2))
   pygame.display.update()

def draw_game_select_screen():
    # Fill the screen with a black background
    screen.fill(BLACK)

    # Set up font
    font = pygame.font.SysFont('arial', 40)

    # Draw Player 1 and Player 2 titles
    player1_title = font.render('Player 1', True, WHITE)
    player2_title = font.render('Player 2', True, WHITE)
    screen.blit(player1_title, (50, 20))
    screen.blit(player2_title, (SCREEN_WIDTH - player2_title.get_width() - 50, 20))

    # Draw a line in the middle
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    # Draw Player 1 Boxes
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.2, 100, 80, 80))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.2, 220, 80, 80))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.2, 340, 80, 80))

    # Draw Player 2 Boxes
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.7, 100, 80, 80))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.7, 220, 80, 80))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH * 0.7, 340, 80, 80))

    # Player 1 Boxes
    number1 = font.render('1', True, BLACK)
    screen.blit(number1, (SCREEN_WIDTH * 0.2 + 80 / 2 - number1.get_width() / 2, 100 + 80 / 2 - number1.get_height() / 2))
    number2 = font.render('2', True, BLACK)
    screen.blit(number2, (SCREEN_WIDTH * 0.2 + 80 / 2 - number2.get_width() / 2, 220 + 80 / 2 - number2.get_height() / 2))
    number3 = font.render('3', True, BLACK)
    screen.blit(number3, (SCREEN_WIDTH * 0.2 + 80 / 2 - number3.get_width() / 2, 340 + 80 / 2 - number3.get_height() / 2))

    # Player 2 Boxes
    number4 = font.render('4', True, BLACK)
    screen.blit(number4, (SCREEN_WIDTH * 0.7 + 80 / 2 - number4.get_width() / 2, 100 + 80 / 2 - number4.get_height() / 2))
    number5 = font.render('5', True, BLACK)
    screen.blit(number5, (SCREEN_WIDTH * 0.7 + 80 / 2 - number5.get_width() / 2, 220 + 80 / 2 - number5.get_height() / 2))
    number6 = font.render('6', True, BLACK)
    screen.blit(number6, (SCREEN_WIDTH * 0.7 + 80 / 2 - number6.get_width() / 2, 340 + 80 / 2 - number6.get_height() / 2))

    # Update the display
    pygame.display.update()

def handle_game_draw():
    
    # Background Color
    screen.fill(BACKGROUND)

    # Draw Players
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    # Healthbar area
    pygame.draw.rect(screen, BLACK, healthbar_area)

    # Draw Healthbars
    handle_healthbar(screen, HEALTHBAR1_XSPAWN, HEALTHBAR1_YSPAWN, 300, 40, player1_health, MAX_HP)
    handle_healthbar(screen, HEALTHBAR2_XSPAWN, HEALTHBAR2_YSPAWN, 300, 40, player2_health, MAX_HP)

    # Draw Portals
    for portal in portals:
        pygame.draw.rect(screen, BLACK, portal)

    # Draw Medkits
    for medkit in medkits:
        pygame.draw.rect(screen, GREEN, medkit)
        pygame.draw.rect(screen, GREEN, medkit)
        

    # Update Bullets for Player 1
    for player1_bullet_left in player1_bullets_list_left:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_left["x"], player1_bullet_left["y"], BULLET_SIZE, BULLET_SIZE))
    for player1_bullet_left_up in player1_bullets_list_left_up:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_left_up["x"], player1_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player1_bullet_left_down in player1_bullets_list_left_down:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_left_down["x"], player1_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE))

    for player1_bullet_right in player1_bullets_list_right:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_right["x"], player1_bullet_right["y"], BULLET_SIZE, BULLET_SIZE))
    for player1_bullet_right_up in player1_bullets_list_right_up:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_right_up["x"], player1_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player1_bullet_right_down in player1_bullets_list_right_down:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_right_down["x"], player1_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE))

    for player1_bullet_up in player1_bullets_list_up:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_up["x"], player1_bullet_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player1_bullet_down in player1_bullets_list_down:
        pygame.draw.rect(screen, RED, pygame.Rect(player1_bullet_down["x"], player1_bullet_down["y"], BULLET_SIZE, BULLET_SIZE))

    # Update Bullets for Player 2
    for player2_bullet_left in player2_bullets_list_left:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_left["x"], player2_bullet_left["y"], BULLET_SIZE, BULLET_SIZE))
    for player2_bullet_left_up in player2_bullets_list_left_up:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_left_up["x"], player2_bullet_left_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player2_bullet_left_down in player2_bullets_list_left_down:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_left_down["x"], player2_bullet_left_down["y"], BULLET_SIZE, BULLET_SIZE))

    for player2_bullet_right in player2_bullets_list_right:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_right["x"], player2_bullet_right["y"], BULLET_SIZE, BULLET_SIZE))
    for player2_bullet_right_up in player2_bullets_list_right_up:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_right_up["x"], player2_bullet_right_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player2_bullet_right_down in player2_bullets_list_right_down:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_right_down["x"], player2_bullet_right_down["y"], BULLET_SIZE, BULLET_SIZE))

    for player2_bullet_up in player2_bullets_list_up:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_up["x"], player2_bullet_up["y"], BULLET_SIZE, BULLET_SIZE))
    for player2_bullet_down in player2_bullets_list_down:
        pygame.draw.rect(screen, BLUE, pygame.Rect(player2_bullet_down["x"], player2_bullet_down["y"], BULLET_SIZE, BULLET_SIZE))

    # Display
    pygame.time.Clock().tick(FRAME_RATE)
    pygame.display.flip()

def handle_game():
    # I got the logic of the different game screens from https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/#:~:text=the%20user's%20choice.-,You%20can%20add%20an%20if%20statement%20to%20the%20main%20game,the%20restart%20or%20quit%20button.&text=With%20this%20code%2C%20the%20game%20will%20restart%20when%20the%20user,Q'%20button%20on%20the%20keyboard.&text=The%20code%20starts%20by%20importing%20the%20pygame%20module%20and%20initializing%20it
    
    global game_state
    
    # Game Start Screen
    if game_state == "start_menu":
       draw_game_start_menu()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_SPACE]:
            game_state = "game"
            game_over = False
    
    # Game Over Screen
    elif game_state == "game_over":
       draw_game_over_screen()

       keys = pygame.key.get_pressed()
       # Replay Screen
       if keys[pygame.K_r]:
           game_state = "start_menu"
           handle_game_restart()

       # Quit Screen
       if keys[pygame.K_x]:
           pygame.quit()
           quit()

    # Game Playing Screen
    elif game_state == "game":
        handle_game_draw()
        handle_players()
        handle_player1_bullets()
        handle_player2_bullets()
        handle_obstacles()
        handle_powerups()

        # Call Game Over State
        if player2_health == 0 or player1_health == 0:
            game_over = True
            game_state = "game_over"           

        # Update Display
        pygame.display.update()
  
    elif game_over:
       game_state = "game_over"
       game_over = False

def handle_game_restart():
    global player1_health
    global player2_health
    global portals
    global medkits

# Reset players health to maximum
    player1_health = MAX_HP
    player2_health = MAX_HP

# Reset player spawn
    player1.x = PLAYER1_XSPAWN
    player1.y = PLAYER1_YSPAWN
    player2.x = PLAYER2_XSPAWN
    player2.y = PLAYER2_YSPAWN

# Empty portal list and call portals again
    portals = []
    for _ in range(PORTAL_AMOUNT):
        portal = pygame.Rect(random.randint(0, SCREEN_WIDTH - 100) 
            + 50, random.randint(0, SCREEN_HEIGHT * UNPLAYABLE_AREA - 100)
            + 50, PORTAL_WIDTH, PORTAL_HEIGHT)
        portals.append(portal)

# Empty medkit list and call medkits again
    medkits = []
    for _ in range(MEDKIT_AMOUNT):
        medkit = pygame.Rect(random.randint(0, SCREEN_WIDTH - 100) 
            + 50, random.randint(0, SCREEN_HEIGHT * UNPLAYABLE_AREA - 100)
            + 50, MEDKIT_WIDTH, MEDKIT_HEIGHT)
        medkits.append(medkit)

# Clear all bullets from screen
    player1_bullets_list_left.clear()
    player1_bullets_list_left_up.clear()
    player1_bullets_list_left_down.clear()
    player1_bullets_list_right.clear()
    player1_bullets_list_right_up.clear()
    player1_bullets_list_right_down.clear()
    player1_bullets_list_up.clear()
    player1_bullets_list_down.clear()

    player2_bullets_list_left.clear()
    player2_bullets_list_left_up.clear()
    player2_bullets_list_left_down.clear()
    player2_bullets_list_right.clear()
    player2_bullets_list_right_up.clear()
    player2_bullets_list_right_down.clear()
    player2_bullets_list_up.clear()
    player2_bullets_list_down.clear()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    handle_game()






