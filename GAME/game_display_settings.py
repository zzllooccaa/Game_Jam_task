import pygame
from main import path_icon_menu, path_background_game

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


def Display_game():
    display_surface_game = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Time does not exist")
    Icon = pygame.image.load(path_icon_menu)
    pygame.display.set_icon(Icon)
    background = pygame.image.load(path_background_game)
    display_surface_game.blit(background, (z, d))
