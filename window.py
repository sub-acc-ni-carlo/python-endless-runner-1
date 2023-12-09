import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('images/bg/music/bgmusicgame.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

def pause_music():
    pygame.mixer.music.pause()

# create the game window
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Endless Runner')