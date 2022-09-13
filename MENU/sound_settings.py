import pygame
import os
from main import path_sound_menu

sound_on = True
s = 'sound'
music = pygame.mixer.music.load(os.path.join(s, path_sound_menu))


def sound_menu():
    music = pygame.mixer.music.load(os.path.join(s, path_sound_menu))
    pygame.mixer.init()
    pygame.mixer.music.play(-1)
