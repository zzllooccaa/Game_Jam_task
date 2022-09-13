import pygame
from main import path_icon_menu, path_background_menu

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
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont("arialblack", 40)
TEXT_COLOURS = (255, 255, 255)


def draw_text(text, font, text_colours, x, y):
    img = font.render(text, True, text_colours)
    display_surface.blit(img, (x, y))


def Display():
    X = 600
    Y = 400
    display_surface = pygame.display.set_mode((X, Y))
    width = display_surface.get_width()
    pygame.display.set_caption("Time does not exist")
    Icon = pygame.image.load(path_icon_menu)
    pygame.display.set_icon(Icon)
    background = pygame.image.load(path_background_menu)
    display_surface.blit(background, (0, 0))
