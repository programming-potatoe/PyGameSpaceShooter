import pygame
import os

# constants in capital letters
# window constants
WIDTH, HEIGHT = 2000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("the name of my window")
FPS = 60

# color constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# spaceship constants
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 150,100

SHIP_TYPE_YELLOW = 0
SHIP_TYPE_RED = 1

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

SPACESHIP_STEP_SIZE = 10

# background constants
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

# bullet constants
MAX_BULLETS = 4
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_STEP_SIZE = 20
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-small-hit-in-a-game-2072.wav"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-short-laser-gun-shot-1670.wav"))

# border constants
BORDER = pygame.Rect(WIDTH//2-10, 0, 20, HEIGHT)

# health constants
MAX_HEALTH = 10
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)


# custom events
YELLOW_LOST = pygame.USEREVENT + 1
RED_LOST = pygame.USEREVENT + 2
