# Coding Diary

## Date: [11/27/2023]

### Today's Goals:

- Make Bullets Shoot at an angle

### What I Learned Today:

- I learned how to use math radians to make the bullets be able to shoot at an angle


### Challenges Faced:

- Thinking of a way to shoot the bullets at an angle

### Code Snippets:
### This makes sure that the bullets shoot at an angle
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and len(bullets2rightdown) < MAX_BULLETS and keys[pygame.K_RSHIFT]:
        bullet2rightdown = {"x" : player2.x, "y" : player2.y, "angle" : math.radians(75)}
        bullets2rightdown.append(bullet2rightdown)
        
    #Set Player 2 Bullet Bounds and Bullet Speed
    for bullet2rightdown in bullets2rightdown:
        bullet2rightdown["x"] += BULLET_SPEED * bullet2rightdown["angle"]
        bullet2rightdown["y"] += BULLET_SPEED * bullet2rightdown["angle"]
        

### What I May Improve:

- The code is getting really messy now. I need to know how to make it more readable man. 