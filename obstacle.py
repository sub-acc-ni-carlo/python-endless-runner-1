from config import WINDOW_HEIGHT as game_height
from config import WINDOW_WIDTH as game_width
from window import game
from game_variables import speed
from window import pygame
import random


class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = {}
        self.width = width
        self.height = height
        
        # load images used for the obstacles
        self.obstacle_images = []
        for image_name in ['television']:
            image = pygame.image.load(f'images/obstacles/{image_name}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.width, self.height))
            self.obstacle_images.append(image)
            
        # assign a random image
        self.image = random.choice(self.obstacle_images)
        
        # position the obstacle just off the right side of the screen
        self.x = game_width
        self.y = game_height - self.image.get_height()
        
        # set the initial rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self):
        game.blit(self.image, (self.x, self.y))
        
    def update(self):
        ''' move obstacle to the left '''
        
        # move left
        self.x -= speed
        
        # update the rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        # update the mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)
        
    def reset(self):
        ''' assign a new image and reset back to original position '''
        
        self.image = random.choice(self.obstacle_images)
        self.x = game_width
        self.y = game_height - self.image.get_height()
