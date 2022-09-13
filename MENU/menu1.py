import sys, pygame
import time
import GAME.game
import ABOUT.about
import button, display_settings, sound_settings

from main import path_button_play, path_button_about, path_button_quit, path_game_entry_image, path_icon_menu


def Menu():
    pygame.init()
    display_settings.Display()
    play_img = pygame.image.load(path_button_play).convert_alpha()
    about_img = pygame.image.load(path_button_about).convert_alpha()
    quit_img = pygame.image.load(path_button_quit).convert_alpha()

    start_button = button.Button(140, 120, play_img)
    about_button = button.Button(225, 220, about_img)
    quit_button = button.Button(320, 300, quit_img)
    display_settings.Display()
    pygame.mixer.music
    sound_settings.sound_menu()

    running = True

    while running:

        if start_button.draw(display_settings.display_surface):
            # print("start")
            pygame.mixer.music.stop()
            GAME.game.RUN()
            running = False

        if about_button.draw(display_settings.display_surface):
            # print("about")
            ABOUT.about.RUN_about()
            running = False

        if quit_button.draw(display_settings.display_surface):
            pygame.mixer.music.stop()
            running = False
            pygame.mixer.music.unload()
            pygame.quit()
            # print("exit")
        pygame.display.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            pygame.display.update()

    pygame.quit()


pygame.init()

X = 600
Y = 400
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Time does not exist")
Icon = pygame.image.load(path_icon_menu)
pygame.display.set_icon(Icon)
image = pygame.image.load(path_game_entry_image)

running = True

while running:

    running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
display_surface.blit(image, (0, 0))
pygame.display.update()
time.sleep(3)

Menu()
