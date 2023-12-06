from config import WINDOW_HEIGHT as game_height
from window import game
from window import pygame


class Player(pygame.sprite.Sprite): 


    def __init__(self, x, y, width, height, jump_height=1.5):
        
        pygame.sprite.Sprite.__init__(self)
        self.sprites = {}
        self.height = height
        self.x, self.y = x, y
        self.jump_height = jump_height
        self.action = 'running'
        self.health = 5
        # number of frames player is invincible after getting hurt
        self.invincibility_frame = 0

        
    def draw(self):
        ''' draw the sprite based on the character action and index '''

        # one instantiaion of jump and run animation.
        running_sprite = self.sprites['running_animation']['animation'][int(self.sprites['running_animation']['index'])]
        jumping_sprite = self.sprites["jumping_animation"]['animation'][int(self.sprites["jumping_animation"]["index"])]
        
        if self.action == 'running':
            
            # add invincibility effect when hurt
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                game.blit(running_sprite, (self.x, self.y))
                self.sprites["jumping_animation"]['index'] = 0

        elif self.action == 'jumping' or self.action == 'landing':
            
            # add invincibility effect when hurt
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                game.blit(jumping_sprite, (self.x, self.y))
        
        elif self.action == 'walk_forward':
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                self.x += 1
                game.blit(running_sprite, (self.x, self.y))
                
        elif self.action == 'walk_backward':
            if self.x - 1 <= 1:
                self.x = 1
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                self.x -= 1
                game.blit(running_sprite, (self.x, self.y))

    def add_sprite(self, sprite_object):
        self.sprites[sprite_object.group_name] = {'animation': sprite_object.animation, 'index': sprite_object.index}

    def update(self):
        ''' update the sprite index so the next sprite image is drawn '''
        ''' also update the y position when jumping or landing '''
        
        if self.action == 'running' or self.action == 'walk_forward' or self.action == 'walk_backward':
            
            # increment the sprite index by 0.2
            # so it takes 5 frames to get to the next index
            self.sprites['running_animation']['index'] += 0.2

            print(self.sprites['running_animation']['index'])
            
            # go back to index 0 after the last sprite image is drawn
            if self.sprites['running_animation']['index'] >= len(self.sprites['running_animation']['animation']):
                self.sprites['running_animation']['index'] = 0

            # update the rect
            self.rect = self.sprites['running_animation']['animation'][int(self.sprites['running_animation']['index'])].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # update the mask for collision detection
            self.mask = pygame.mask.from_surface(self.sprites['running_animation']['animation'][int(self.sprites['running_animation']['index'])])
            
        elif self.action == 'jumping' or self.action == 'landing':
            
            # increment the sprite index by 0.1
            # so it takes 5 frames to get to the next index
            self.sprites['jumping_animation']['index'] += 0.05
            
            # go back to index 0 after the last sprite image is drawn
            if self.sprites['jumping_animation']['index'] >= len(self.sprites['jumping_animation']['animation']):
                self.sprites['jumping_animation']['index'] = 0
                
            # move position up if jumping or down if landing
            if self.action == 'jumping':
                self.y -= 3
                
                # change to landing when peak of jump is reached
                if self.y <= game_height - self.height * self.jump_height:
                    self.action = 'landing'
                    
            elif self.action == 'landing':
                self.y += 3
                
                # change to running when character touches the ground
                if self.y == game_height - self.height:
                    self.action = 'running'

            # update the rect
            self.rect = self.sprites['jumping_animation']['animation'][int(self.sprites['jumping_animation']['index'])].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            
            # update the mask for collision detection
            self.mask = pygame.mask.from_surface(self.sprites['jumping_animation']['animation'][int(self.sprites['jumping_animation']['index'])])
            
    def jump(self):
        ''' make the player go to jumping action when not already jumping or landing '''
        if self.action not in ['jumping', 'landing']:
            self.action = 'jumping'
    
    def set_action(self, action):
        if self.action not in ['jumping', 'landing']:
            self.action = action