# from config import WINDOW_HEIGHT as game_height
# from window import game
# from window import pygame
# from abc import abstractclassmethod


# class Entity(pygame.sprite.Sprite): 

#     def __init__(self, x, y, width, height):
#         pygame.sprite.Sprite.__init__(self)
#         self.sprites = {}
#         self.height = height
#         self.width = width
#         self.x, self.y = x, y
#         self.action = None
    
#     @abstractclassmethod
#     def draw(self):
#         pass

#     @abstractclassmethod
#     def update(self):
#         pass

#     def add_sprite(self, sprite_object):
#         self.sprites[sprite_object.group_name] = {'animation': sprite_object.animation, 'index': sprite_object.index}
    
#     @abstractclassmethod
#     def set_action(self, action):
#         pass

