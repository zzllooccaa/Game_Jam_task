import pygame
import display_settings


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
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

        display_settings.display_surface.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()

        return action
