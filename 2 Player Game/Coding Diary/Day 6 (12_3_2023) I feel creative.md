# Coding Diary

## Date: [11/27/2023]

### Today's Goals:

- I tried to make randomly generating rocks that the player can't pass through

### What I Learned Today:

- How to make a bug a feature


### Challenges Faced:

- Idk why pygame collision .left and .right doesn't really work with my randomly generated rocks. I spent like 1 hour trying to figure this out bro.
- So instead of making the player unable to pass through the rocks, i just teleport the player to a random location on collision.
- And hey! It's alot more fun to play
- Let's call them portals

### Code Snippets:
### This makes sure that the obstacles generate randomly, while also not spawning at the player spawn, and also not making it loop infinitely
def obstacles():
    global PLAYER_SPEED
    if not portals:
        for _ in range(10):
            portal = pygame.Rect(random.randint(0, SCREEN_WIDTH - 50), random.randint(0, SCREEN_HEIGHT - 50), 50, 50)
            portals.append(portal)
    for portal in portals:
        if pygame.Rect(portal).colliderect(player1):
            player1.x = random.randint(0, SCREEN_WIDTH)
            player1.y = random.randint(0, SCREEN_HEIGHT)
    for portal in portals:
        if pygame.Rect(portal).colliderect(player2):
            player2.x = random.randint(0, SCREEN_WIDTH)
            player2.y = random.randint(0, SCREEN_HEIGHT)

### What I May Improve:

- I like how this game is going. It seems cooler now with the portals.