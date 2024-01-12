import pygame
from pygame.locals import *
import random
import math
from assets import background_assets
from player import Player
from obstacle import Obstacle
from projectile import Projectile
from window import game
from window import pause_music
from config import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from game_variables import score, speed
from background_manager import background_manager
from sprite import Sprite

# set the image for the sky
sky = pygame.image.load('images/bg/sky.png').convert_alpha()
num_bg_tiles = math.ceil(WINDOW_WIDTH / sky.get_width()) + 1
biomes = ['day', 'sky'] * 6
biome = 'day' 
# for the parallax effect, determine how much each layer will scroll
parallax = []
for x in range(len(background_assets(pygame,'day'))):
    parallax.append(0)

# create the player
player_width, player_height = 105, 105
player_x_pos, player_y_pos = 25, WINDOW_HEIGHT - player_height
player = Player(player_x_pos, player_y_pos, player_width, player_height, 2)
player.add_sprite(Sprite("running_animation", [
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_1.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_2.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_3.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_4.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_5.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_6.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_7.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_8.png').convert_alpha(), (player_width, player_height)),
]))

player.add_sprite(Sprite("jumping_animation", [
        pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump1.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump2.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump3.png').convert_alpha(), (player_width, player_height))
    ]))

player.add_sprite(Sprite("ducking_animation", [
        pygame.transform.scale(pygame.image.load('images/player/duck_animation/student_duck1.png').convert_alpha(), (player_width, player_height)),
        pygame.transform.scale(pygame.image.load('images/player/duck_animation/student_duck2.png').convert_alpha(), (player_width, player_height))
    ]))

# create the obstacle
obstacles_group = pygame.sprite.Group()
obstacle = Obstacle(73, 73, 10)
obstacles_group.add(obstacle)

projectile_group = pygame.sprite.Group()
projectile = Projectile()
projectile_group.add(projectile)

# load the heart images for representing health
heart_sprites = []
heart_sprite_index = 0
for i in range(8):
    heart_sprite = pygame.image.load(f'images/heart/heart{i}.png').convert_alpha()
    scale = 30 / heart_sprite.get_height()
    new_width = heart_sprite.get_width() * scale
    new_height = heart_sprite.get_height() * scale
    heart_sprite = pygame.transform.scale(heart_sprite, (new_width, new_height))
    heart_sprites.append(heart_sprite)


# game loop
score = 0
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
quit = False
pause = False
while not quit:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
            
        # press SPACE to jump
        if event.type == KEYDOWN and event.key == K_SPACE:
            player.jump()
        # press SPACE to jump
        if event.type == KEYDOWN and event.key == K_w:
            player.jump()
        # press key 'D' to walk forward
        if event.type == KEYDOWN and event.key == K_d:
            player.set_action('walk_forward')
        # press key 'A' to walk forward
        if event.type == KEYDOWN and event.key == K_a:
            player.set_action('walk_backward')
        
        
        # press key 'S' to duck
        if event.type == KEYDOWN and event.key == K_s:
            player.set_action('ducking')

        # press key 'S' to duck
        if event.type == KEYUP and event.key == K_s:
            player.set_action('running')
        
        if event.type == KEYDOWN and event.key == K_p:
            pause = not pause
            
    # loads the background
    background_manager(
        game,                           # pygame display
        parallax,                       # array of assets in the background
        background_assets(pygame,biome),      # images object
        sky                             # sky
    )
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    total_score = elapsed_time + score
    
    #change biome
    index = min(total_score // 100, len(biomes) - 1)
    biome = biomes[index]
    
    projectile_timing = 0
    if total_score > 5:
        projectile.draw()
        projectile.update()
        
    #change biome
    index = min(total_score // 100, len(biomes) - 1)
    biome = biomes[index]
    projectile_timing = 0
    if total_score > 5:
        projectile.draw()
        projectile.update()
        projectile_timing = 5
    
    
    if projectile_timing == 5:
        obstacle_new = Obstacle(73, 73, 10)
        obstacles_group.add(obstacle)
        projectile_timing = 5
        projectile_timing = 5
    
    if projectile_timing == 5:
        obstacle_new = Obstacle(73, 73, 10)
        obstacles_group.add(obstacle)
        projectile_timing = 5
        
    # draw the player
    player.draw()
    
    # update the sprite and position of the player
    player.update()
    projectile.update()
    # draw the obstacle
    obstacle.draw()
    
    if total_score > 5 and obstacle.x in [0, 80, 160, 260, 360, 460, 760, 950]:
        projectile.draw()
       
    # update the position of the obstacle
    obstacle.update()
    
    #reset the projectile
    if projectile.x <= 0:
        projectile.reset()
        speed += 1
    #reset the obstacle 
    if obstacle.x <= 0:
        obstacle.reset()
        speed += 1

    # check if player collides with the obstacle
    if pygame.sprite.spritecollide(player, obstacles_group, True, pygame.sprite.collide_mask):
        player.health -= 1
        player.invincibility_frame = 30
        
        # remove obstacle and replace with a new one
        obstacles_group.type = ''
        obstacles_group.image_name = ''
        obstacles_group.type = ''
        obstacles_group.image_name = ''
        obstacles_group.remove(obstacle)
        obstacle = Obstacle(73, 73, 10)
        obstacles_group.add(obstacle)
    
    if pygame.sprite.spritecollide(player, projectile_group, True, pygame.sprite.collide_mask):
        player.invincibility_frame = 30

        # remove projectile and replace with a new one
        if projectile.type == 'book':
            player.health += 1
            score += 100
        else:
            player.health -= 1
        projectile.type = ''
        projectile.image_name = ''
        projectile_group.remove(projectile)
        projectile = Projectile()
        projectile_group.add(projectile)    
    
  
    # display a heart per remaining health
    for life in range(player.health):
        heart_sprite = heart_sprites[int(heart_sprite_index)]
        x_pos = 10 + life * (heart_sprite.get_width() + 10)
        y_pos = 10
        game.blit(heart_sprite, (x_pos, y_pos))
        
    # increment the index for the next heart sprite
    # use 0.1 to make the sprite change after 10 frames
    heart_sprite_index += 0.1
    
    # set index back to 0 after the last heart sprite is drawn
    if heart_sprite_index >= len(heart_sprites):
        heart_sprite_index = 0
        
    # display the score
    black = (255, 255, 255)
    font = pygame.font.Font("PixelGameFont.ttf", 16)
    text = font.render(f'SCORE: {total_score}', True, black)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH - 50, 20)
    game.blit(text, text_rect)
            
    pygame.display.update()

    while pause:

        pause_color = (0, 255, 0)
        pygame.draw.rect(game, pause_color, (0, 50, WINDOW_WIDTH, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game is paused. Press P to continue...', True, black)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 100)
        game.blit(text, text_rect)


        for event in pygame.event.get():
                
            # get the player's input (Y or N)
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause = not pause
                    
        pygame.display.update()


    # gameover
    gameover = player.health == 0
    while gameover and not quit:
        pause_music()
        # display game over message
        game_over_color = (0, 0, 0)
        pygame.draw.rect(game, game_over_color, (0, 50, WINDOW_WIDTH, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, black)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 100)
        game.blit(text, text_rect)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                quit = True
                
            # get the player's input (Y or N)
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # reset the game
                    pygame.mixer.music.play(-1)
                    gameover = False
                    speed = 3
                    score = 0
                    player = Player(player_x_pos, player_y_pos, player_width, player_height, 2)
                    player.add_sprite(Sprite('running_animation', [
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_1.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_2.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_3.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_4.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_5.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_6.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_7.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/run_animation/sti_student_8.png').convert_alpha(), (player_width, player_height)),
                    ]))

                    player.add_sprite(Sprite("jumping_animation", [
                    pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump1.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump2.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/jump_animation/student_jump3.png').convert_alpha(), (player_width, player_height))
                    ]))
                    player.add_sprite(Sprite("ducking_animation", [
                    pygame.transform.scale(pygame.image.load('images/player/duck_animation/student_duck1.png').convert_alpha(), (player_width, player_height)),
                    pygame.transform.scale(pygame.image.load('images/player/duck_animation/student_duck2.png').convert_alpha(), (player_width, player_height))
                    ]))
                    obstacle = Obstacle(73, 73, 10)
                    obstacles_group.empty()
                    obstacles_group.add(obstacle)
                    projectile = Projectile()
                    projectile_group.empty()
                    projectile_group.add(projectile)
                elif event.key == K_n:
                    pygame.mixer.music.stop()
                    quit = True
                    
        pygame.display.update()
    
pygame.quit()