# Coding Diary

## Date: [11/22/2023]

### Today's Goals:

- Create Bullets for Characters

### What I Learned Today:

- How to use lists to store for game items
- Append and Remove are useful

### Challenges Faced:

- Finding out how to do it

### Code Snippets:

    # Create the bullets storage
    bullets1 = []

    # Function to handle the bullets
    def handle_bullets():
    # Got the logic of appending and removing bullets from https://electronstudio.github.io/pygame-zero-book/chapters/shooter.html#player-bullets
    # But changed it up to fit pygame and my code
    global bullets

    # Player 1 Bullets 
    if keys[pygame.K_e] and len(bullets1) < MAX_BULLETS:
        # Put in Dictionary for readability compared to list
        bullet1 = {"x" : player1.x, "y" : player1.y}
        bullets1.append(bullet1)

    for bullet1 in bullets1:
        bullet1["y"] -= BULLET_SPEED
        # Remove Bullets
        if bullet1["y"] < 0:
            bullets1.remove(bullet1)