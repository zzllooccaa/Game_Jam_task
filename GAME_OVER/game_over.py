import time
import pygame
import sys

from main import path_icon_menu, path_game_over, path_game_over2, path_game_over_sound

pygame.init()
white = (255, 255, 255)
blue = (0, 0, 128)
green = (0, 255, 0)
black = (0, 0, 0)
color_light = (170, 170, 170)
ALPHA = (0, 255, 0)
color_dark = (100, 100, 100)
X = 600
Y = 400
display_surface_game = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont("arialblack", 40)
z = 0
d = 0
snd_over = pygame.mixer.Sound(path_game_over_sound)


def Display_game():
    display_surface_game_over = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Time does not exist")
    Icon = pygame.image.load(path_icon_menu)
    pygame.display.set_icon(Icon)
    background = pygame.image.load(path_game_over)
    display_surface_game_over.blit(background, (z, d))


def Over():
    pygame.init()
    Display_game()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        snd_over.play()
        pygame.display.update()
        time.sleep(3)
        play_img = pygame.image.load(path_game_over2).convert_alpha()
        display_surface_game.blit(play_img, [0, 0])
        pygame.display.update()
        time.sleep(2)
        snd_over.stop()
        running = False
        from MENU.menu1 import Menu
        Menu()

Over()