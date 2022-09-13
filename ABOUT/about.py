import sys, pygame
from main import path_button_back
from ABOUT import about_display_settings
import button


color_light = (170, 170, 170)
back_img = pygame.image.load(path_button_back).convert_alpha()
back_button = button.Button(0, 350, back_img)


def RUN_about():
    pygame.init()

    about_display_settings.Display_about()
    def About_play():
        runs = True
        while runs:
            # if back_button.draw(about_display_settings.display_surface_about):
            #     print("Back")
            #     from MENU.menu1 import Menu
            #     Menu()

                # pygame.display.update()
                # about_display_settings.display_surface_about
                # about_display_settings.display_surface_about
                # pygame.display.update()

                # runs = False
                # pygame.quit()
                # return Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if back_button.draw(about_display_settings.display_surface_about):
                    print("Back")
                    from MENU.menu1 import Menu
                    Menu()
                # pygame.display.update()
                # about_display_settings.display_surface_about
                # about_display_settings.display_surface_about
                # pygame.display.update()
                    runs = False

        # pygame.display.update()

        # pygame.quit()

    About_play()
