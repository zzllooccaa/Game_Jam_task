import pygame
import about_display_settings


class Button():
    def __init__(self, x, y, image, color):
        self.image = image
        self.rect = self.image.get_rect(color)
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("clicked")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw on screen
        about_display_settings.display_surface_about.blit(self.image, (self.rect.x, self.rect.y))

        return action
