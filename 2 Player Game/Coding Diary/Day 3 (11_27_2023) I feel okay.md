# Coding Diary

## Date: [11/27/2023]

### Today's Goals:

- Make Players Rotate and be able to shoot in that direction

### Challenges Faced:

- Trying to find a way for bullets to follow the direction the player wants.
- I still haven't thought of a way to make the bullets be able to shoot at an angle

### What I Learned Today:

- How to think better


### Code Snippets:
### This makes sure that the bullets follow the direction that the player wants
    if keys[pygame.K_d] and len(bullets1right) < MAX_BULLETS and keys[pygame.K_q]:

### What I May Improve:

- I don't really like this type of controls. It is too messy in the code(maybe I just suck), and it is not fun enough. I may change it in the future. Maybe make auto-firing like Vampire Survivors