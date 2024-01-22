# Coding Diary

## Date: [11/27/2023]

### Today's Goals:

- Making Healthbars for the players

### Challenges Faced:

- Today the biggest challenge was sensing the collision and reporting it back to the healthbar

### What I Learned Today:

- understanding OOP and changing it into functional programming

- I also found out that the order in which collisions happen when writing the code for collisions matters ALOT.
- This caused me alot of frustration because sometimes the collisions wouldn't register, and the healthbar did not decrease
- Only for me to find out that the reason was because I kept on removing the bullets from the list BEFORE it registered for
health reduction

- I also changed up the code abit for the bullets to make it neater


### Code Snippets:
def handle_healthbar(surface, x, y, w, h, current_hp, max_hp):
    # I got the idea from: http://www.codingwithruss.com/pygame/how-to-create-a-health-bar-in-pygame/
    # But because the original code was written as OOP, I rewrote the whole code to make it functional

    # Calculate health ratio
    ratio = current_hp / max_hp
    pygame.draw.rect(surface, "red", (x, y, w, h))
    pygame.draw.rect(surface, "green", (x, y, w * ratio, h))

### What I May Improve:

- I like how this game is going. It seems cooler now with the portals.