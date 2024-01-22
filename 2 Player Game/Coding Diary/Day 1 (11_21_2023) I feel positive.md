# Coding Diary

## Date: [11/21/2023]

### Today's Goals:

- Create 2 playable characters
- Create Basic Framework for characters

### Challenges Faced:

- Trying to find a way to keep players within bounds

### What I Learned Today:

- How min and max can be helpful for video game logic, especially in spawn points and boundaries


### Code Snippets:
### This makes sure that the maximum possible movement is always higher than 0, but not bigger than the Screen Size
    player1.x = max(0, min(player1.x, SCREEN_WIDTH - CHARACTER_SIZE))
    player1.y = max(0, min(player1.y, SCREEN_HEIGHT - CHARACTER_SIZE))
    player2.x = max(0, min(player2.x, SCREEN_WIDTH - CHARACTER_SIZE))
    player2.y = max(0, min(player2.y, SCREEN_HEIGHT - CHARACTER_SIZE))