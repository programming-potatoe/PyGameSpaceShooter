# Tutorial: https://youtu.be/jO6qQDNa2UY

import pygame
import os
pygame.font.init()
pygame.mixer.init()

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
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    """
    test_function does blah blah blah
    
    :param p1: describe about parameter p1
    :return: describe what it returns
    """
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, RED)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, YELLOW)
    WIN.blit(red_health_text, ((WIDTH - red_health_text.get_width() - 10), 10))
    WIN.blit(yellow_health_text, (0, 10))
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    
    pygame.display.update()

def handle_yellow_movement(keys_pressed, spaceship):
    """
    test_function does blah blah blah
    
    :param p1: describe about parameter p1
    :return: describe what it returns
    """
    if keys_pressed[pygame.K_a] and (spaceship.x - SPACESHIP_STEP_SIZE) >= 0:
        spaceship.x -= SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_d] and ((spaceship.x + spaceship.width) + SPACESHIP_STEP_SIZE) <= BORDER.x + 40:
        spaceship.x += SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_s] and ((spaceship.y + spaceship.height) + SPACESHIP_STEP_SIZE) <= HEIGHT - 40:
        spaceship.y += SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_w] and (spaceship.y - SPACESHIP_STEP_SIZE) >= 0:
        spaceship.y -= SPACESHIP_STEP_SIZE


def handle_red_movement(keys_pressed, spaceship):
    """
    test_function does blah blah blah
    
    :param p1: describe about parameter p1
    :return: describe what it returns
    """
    if keys_pressed[pygame.K_LEFT] and (spaceship.x - SPACESHIP_STEP_SIZE) >= (BORDER.x + BORDER.width):
        spaceship.x -= SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_RIGHT] and ((spaceship.x + spaceship.width) + SPACESHIP_STEP_SIZE) <= WIDTH + 40:
        spaceship.x += SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_DOWN] and ((spaceship.y + spaceship.height) + SPACESHIP_STEP_SIZE) <= HEIGHT - 40:
        spaceship.y += SPACESHIP_STEP_SIZE
    if keys_pressed[pygame.K_UP] and (spaceship.y - SPACESHIP_STEP_SIZE) >= 0:
        spaceship.y -= SPACESHIP_STEP_SIZE

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    test_function does blah blah blah
    
    :param p1: describe about parameter p1
    :return: describe what it returns
    """
    for bullet in yellow_bullets:
        bullet.x += BULLET_STEP_SIZE
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))
    
    for bullet in red_bullets:
        bullet.x -= BULLET_STEP_SIZE
        if (bullet.x + BULLET_WIDTH) < 0:
            red_bullets.remove(bullet)
        elif yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))    

def draw_winner(text):
    """
    test_function does blah blah blah
    
    :param p1: describe about parameter p1
    :return: describe what it returns
    """
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, ((WIDTH/2 - draw_text.get_width()/2), HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    """
    runs the main loop
    """
    # define rects for ships
    yellow = pygame.Rect(0, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    # init health
    red_health = MAX_HEALTH
    yellow_health = MAX_HEALTH
    
    # create bullet lists
    yellow_bullets= []
    red_bullets = []
    
    # set up clock
    clock = pygame.time.Clock()
    
    run = True
    
    pygame.event.clear()
    
    # start game loop
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # check for shooting controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 20, BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 20, BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
            # check for hit events
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        
        # handle movement controls
        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)
        
        # handle bullet movement and collision
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        
        winner_text = ""
        
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
            
        if winner_text != "":
            draw_winner(winner_text)
            break 


        
    main()

# run main only if this file is run directly
if __name__ == "__main__":
    main()