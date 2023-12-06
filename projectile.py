from config import WINDOW_HEIGHT as game_height
from config import WINDOW_WIDTH as game_width
from window import game
from game_variables import speed
from window import pygame
import random


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # load images used for the projectiles
        self.projectile_images = []
        for image_name in ['rock1', 'rock2', 'rock3', 'spikes']:
            image = pygame.image.load(f'images/obstacles/{image_name}.png').convert_alpha()
            scale = 50 / image.get_width()
            new_width = image.get_width() * scale
            new_height = image.get_height() * scale
            image = pygame.transform.scale(image, (new_width, new_height))
            self.projectile_images.append(image)

        # assign a random image
        self.image = random.choice(self.projectile_images)

        self.x = game_width
        self.y = random.randint(int(0.5 * game_height), int(0.9 * game_height))
        
        # set the initial rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = self.y


    def draw(self):
        game.blit(self.image, (self.x, self.y))
        
    def update(self):
        ''' move obstacle to the left '''
        
        # move left
        self.x -= speed
        
        # update the rect
        #self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        # update the mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)
        
    def reset(self):
        ''' assign a new image and reset back to original position '''
        
        self.image = random.choice(self.projectile_images)
        self.x = game_width
        self.y = random.randint(int(0.5 * game_height), int(0.9 * game_height))
