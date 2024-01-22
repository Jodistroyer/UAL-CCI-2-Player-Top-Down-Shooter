# Coding Diary

## Date: [11/27/2023]

### Today's Goals:

- Make Bullets dissapear when hit opponent

### What I Learned Today:

- How if projectiles are too small, they can pass through players
- Make projectiles bigger to avoid complications


### Challenges Faced:

- Trying to understand why the heck the bullets didn't dissapear on collision

### Code Snippets:
### This makes sure that the bullets follow the direction that the player wants
        for bullet1left in bullets1left:
        if pygame.Rect(bullet1left["x"], bullet1left["y"], BULLET_SIZE, BULLET_SIZE).colliderect(player2):
            bullets1left.remove(bullet1left)

### What I May Improve:

- The code is getting really messy now. I need to know how to make it more readable man. 