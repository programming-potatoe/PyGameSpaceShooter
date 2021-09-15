# Tutorial: https://youtu.be/jO6qQDNa2UY

import pygame
pygame.font.init()
pygame.mixer.init()

from constants import *

import ship


def draw_window(yellow, red):
    """
    draws background and all objects
    
    :param yellow: instance of the yellow ship
    :param red: instance of the red ship
    :return: describe what it returns
    """
    # draw background
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    # draw health text
    red_health_text = HEALTH_FONT.render("Health: " + str(red.health), 1, RED)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow.health), 1, YELLOW)
    WIN.blit(red_health_text, ((WIDTH - red_health_text.get_width() - 10), 10))
    WIN.blit(yellow_health_text, (0, 10))
    
    # draw ships
    WIN.blit(YELLOW_SPACESHIP, (yellow.rect.x, yellow.rect.y))
    WIN.blit(RED_SPACESHIP, (red.rect.x, red.rect.y))
    
    # draw bullets
    for bullet in red.bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow.bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    
    pygame.display.update()

def draw_winner(text):
    """
    draws the text in case someone won
    
    :param text: the text to be displayed
    :return: nothing
    """
    
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, ((WIDTH/2 - draw_text.get_width()/2), HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    """
    main loop of our game
    
    :return: nothing
    """
    
    # create ship instances
    yellow = ship.Ship(SHIP_TYPE_YELLOW)
    red = ship.Ship(SHIP_TYPE_RED)
    
    # set up clock
    clock = pygame.time.Clock()
    
    run = True
    
    winner_text = ""

    
    # clear events in case something got stuck from last loop
    pygame.event.clear()
    
    # start game loop
    while run:
        clock.tick(FPS)
        
        # iterate through all events that happend
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            # check if someone lost and set text
            if event.type == YELLOW_LOST:
                winner_text = "Red Wins!"
            if event.type == RED_LOST:
                winner_text = "Yellow Wins!"

            # check for shooting controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    yellow.shoot()
            
                if event.key == pygame.K_RCTRL:
                    red.shoot()
            
        # did someone win?
        if winner_text != "":
            draw_winner(winner_text)
            break

        
        # handle movement controls
        keys_pressed = pygame.key.get_pressed()
        yellow.handle_movement(keys_pressed)
        red.handle_movement(keys_pressed)
        
        # handle bullet movement and collision
        yellow.move_bullets()
        red.move_bullets()
        yellow.check_for_hit(red.bullets)
        red.check_for_hit(yellow.bullets)
        yellow.remove_useless_bullets()
        red.remove_useless_bullets()
                
        # draw everything
        draw_window(yellow, red)




    # start mainloop again to create endless game   
    main()

# run main only if this file is run directly
if __name__ == "__main__":
    main()