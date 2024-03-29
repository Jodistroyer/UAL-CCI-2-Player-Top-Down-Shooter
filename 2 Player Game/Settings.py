# Framerate
FRAME_RATE = 50

# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
UNPLAYABLE_AREA = 85/100

# Player
PLAYER_SIZE = 10

PLAYER1_SPEED = 10
PLAYER2_SPEED = 10

# Health
PLAYER1_HEALTH = 100
PLAYER2_HEALTH = 100
MAX_HP = 100
HEALTHBAR_LENGTH = 300
HEALTHBAR_HEIGHT = 40

HEALTHBAR1_XSPAWN = min(0, SCREEN_WIDTH) + 20
HEALTHBAR1_YSPAWN = SCREEN_HEIGHT * UNPLAYABLE_AREA + 20

HEALTHBAR2_XSPAWN = max(0, SCREEN_WIDTH) - HEALTHBAR_LENGTH - 20
HEALTHBAR2_YSPAWN = SCREEN_HEIGHT * UNPLAYABLE_AREA + 20

# Bullets
BULLET_SPEED = 20
BULLET_SIZE = PLAYER_SIZE * 2

PLAYER1_MAX_BULLETS = 5
PLAYER2_MAX_BULLETS = 5

PLAYER1_BULLET_DAMAGE = 5
PLAYER2_BULLET_DAMAGE = 5

# Players Spawn Points
PLAYER1_XSPAWN = min(0, SCREEN_WIDTH)
PLAYER1_YSPAWN = SCREEN_HEIGHT/2

PLAYER2_XSPAWN = max(0, SCREEN_WIDTH)
PLAYER2_YSPAWN = SCREEN_HEIGHT/2

# Obstacles
PORTAL_AMOUNT = 20
PORTAL_WIDTH = 20
PORTAL_HEIGHT = 20

# Powerups
MEDKIT_AMOUNT = 5
MEDKIT_HEAL = 5
MEDKIT_WIDTH = 15
MEDKIT_HEIGHT = 15

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (224,224,224)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (80, 173, 75)
BROWN = (139,69,19)