import pygame
from constants import BORDER, BULLET_FIRE_SOUND, BULLET_HIT_SOUND, HEIGHT, MAX_BULLETS, MAX_HEALTH, RED_LOST, SHIP_TYPE_YELLOW, SPACESHIP_HEIGHT, SPACESHIP_STEP_SIZE, SPACESHIP_WIDTH, WIDTH, YELLOW_LOST
import bullet

class Ship:
    def __init__(self, type):
        """
        constructor for Ship
        
        :param type: type of the ship, yellow or red
        :return: nothing
        """
        self.width = SPACESHIP_WIDTH
        self.height = SPACESHIP_HEIGHT
        self.type = type
        self.health = MAX_HEALTH
        self.bullets = []
        
        # starting position (width and height are switched since the spaceships where rotated!)
        if self.type == SHIP_TYPE_YELLOW:
            self.rect = pygame.Rect(0, HEIGHT//2, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
        else:
            self.rect = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT//2, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)

    def handle_movement(self, keys_pressed):
        """
        handles the movement of the ship
        
        :param keys_pressed: list of all the keys pressed in the current cycle
        :return: nothing
        """
        if self.type == SHIP_TYPE_YELLOW:
            if keys_pressed[pygame.K_a] and (self.rect.x - SPACESHIP_STEP_SIZE) >= 0:
                self.rect.x -= SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_d] and ((self.rect.x + self.width) + SPACESHIP_STEP_SIZE) <= BORDER.x + 40:
                self.rect.x += SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_s] and ((self.rect.y + self.height) + SPACESHIP_STEP_SIZE) <= HEIGHT - 40:
                self.rect.y += SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_w] and (self.rect.y - SPACESHIP_STEP_SIZE) >= 0:
                self.rect.y -= SPACESHIP_STEP_SIZE
        else:
            if keys_pressed[pygame.K_LEFT] and (self.rect.x - SPACESHIP_STEP_SIZE) >= (BORDER.x + BORDER.width):
                self.rect.x -= SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_RIGHT] and ((self.rect.x + self.width) + SPACESHIP_STEP_SIZE) <= WIDTH + 40:
                self.rect.x += SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_DOWN] and ((self.rect.y + self.height) + SPACESHIP_STEP_SIZE) <= HEIGHT - 40:
                self.rect.y += SPACESHIP_STEP_SIZE
            if keys_pressed[pygame.K_UP] and (self.rect.y - SPACESHIP_STEP_SIZE) >= 0:
                self.rect.y -= SPACESHIP_STEP_SIZE

    def shoot(self):
        """
        shoots a bullet from the spaceship
        
        :return: nothing
        """
        if len(self.bullets) < MAX_BULLETS:
            self.bullets.append(bullet.Bullet(self))
            BULLET_FIRE_SOUND.play()
    
    def move_bullets(self):
        """
        iterates through all the bullets from this ship and calls the move method of those
        
        :return: nothing
        """
        for bullet in self.bullets:
            bullet.move()
    
    
    def check_for_hit(self, enemy_bullets):
        """
        checks if the ship collides with any of the given bullets and reduces health if hit
        
        :param enemy_bullets: list of the bullets which needs to be checked
        :return: nothing
        """
        for bullet in enemy_bullets:
            if self.rect.colliderect(bullet):
                self.health -= 1
                BULLET_HIT_SOUND.play()
                bullet.to_be_removed = True
                
                # send custom event if health is 0
                if self.health <= 0:
                    if self.type == SHIP_TYPE_YELLOW:
                        pygame.event.post(pygame.event.Event(YELLOW_LOST))
                    else:
                        pygame.event.post(pygame.event.Event(RED_LOST))
    
    def remove_useless_bullets(self):
        """
        removes all bullets that are marked to be removed
        
        :return: nothing
        """
        for bullet in self.bullets:
            if bullet.to_be_removed:
                self.bullets.remove(bullet)