from config import WINDOW_HEIGHT as game_height
from config import WINDOW_WIDTH as game_width
from window import game
from game_variables import speed
from window import pygame
import random


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.projectile_images = []
        self.image_name = ''
        self.type = ''
        self.projectile_names = ['red_horse_1', 'book']
        for image_name in self.projectile_names:
            image = pygame.image.load(f'images/obstacles/{image_name}.png').convert_alpha()
            scale = 50 / image.get_width()
            new_width = image.get_width() * scale
            new_height = image.get_height() * scale
            image = pygame.transform.scale(image, (new_width, new_height))
            self.projectile_images.append(image)
  
        # assign a random image
        self.image = random.choice(self.projectile_images)
        self.image_name = self.get_image_name()
        
        self.type = 'book' if 'book' in self.image_name else 'red_horse_1'
        
        self.x = game_width
        self.y = random.randint(int(0.5 * game_height), int(0.9 * game_height))
        
        # set the initial rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = self.y

    def get_image_name(self):
        # retrieve the image name from the list based on the index
        index = self.projectile_images.index(self.image)
        return self.projectile_names[index]
    
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
        self.image_name = ''
        self.type = ''
        self.image = random.choice(self.projectile_images)
        self.image_name = self.get_image_name()
        self.type = 'book' if 'book' in self.image_name else 'red_horse_1'

        self.x = game_width
        self.y = random.randint(int(0.5 * game_height), int(0.9 * game_height))

