import pygame
from constants import BULLET_HEIGHT, BULLET_STEP_SIZE, BULLET_WIDTH, SHIP_TYPE_YELLOW, WIDTH

class Bullet():
    def __init__(self, ship):
        """
        constructor of Bullet
        
        :param ship: instance of the ship that fired the bullet
        :return: nothing
        """
        self.type = ship.type
        self.to_be_removed = False
        
        if self.type == SHIP_TYPE_YELLOW:
            self.rect = pygame.Rect(ship.rect.x + ship.width, ship.rect.y + ship.height//2 + 20, BULLET_WIDTH, BULLET_HEIGHT)
        else:
            self.rect = pygame.Rect(ship.rect.x, ship.rect.y + ship.height//2 + 20, BULLET_WIDTH, BULLET_HEIGHT)
    
    def move(self):
        """
        moves the bullet and checks if it's out of bounds
                
        :return: nothing
        """
        if self.type == SHIP_TYPE_YELLOW:
            self.rect.x += BULLET_STEP_SIZE
            if self.rect.x > WIDTH:
                self.to_be_removed = True
        else:
            self.rect.x -= BULLET_STEP_SIZE
            if (self.rect.x + BULLET_WIDTH) < 0:
                self.to_be_removed = True