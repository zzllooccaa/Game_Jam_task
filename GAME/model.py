import pygame
import os
from main import path_player, path_zvezda, path_enemy, path_bonus, path_scary, path_game_poison_bottle
import random



ALPHA = (255, 255, 255)
ani = 4  # animation cycles
text_x = 100
text_y = 100
playarea = pygame.Rect((0, 0), (600, 400))

score = 0


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.frames = 0
        self.score_stats = 0
        self.hp = 3
        self.max_hp = 8
        self.hp_bar_lenght = 4
        self.hp_ratio = self.max_hp / self.hp_bar_lenght
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join((path_player), 'ninja' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            # print(self.rect.center)
    def control(self, x, y):
        """
        control player movement"""

        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        pygame.Rect.clamp_ip(self.rect, playarea)
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey


        # levo
        if self.movex < 0 :
            print(self.movex)
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # desno
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

    def create_stars(self):
        return Stars(self.rect.x + 25, self.rect.y)




class Stars(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(path_zvezda)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 5


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.image = pygame.image.load(path_enemy).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600 - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 1
        self.vel_x = 0
        self.vel_y = random.randrange(3, 9)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()
        self.hp -= 1

    def destroy(self):
        self.kill()


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.image = pygame.image.load(path_scary).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600 - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 2
        self.vel_x = 0
        self.vel_y = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()
        self.hp -= 1

    def destroy(self):
        self.kill()


class BonusPoints(pygame.sprite.Sprite):
    def __init__(self):
        super(BonusPoints, self).__init__()
        self.image = pygame.image.load(path_bonus).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600 - self.rect.width)
        self.rect.y = -self.rect.height
        self.score = 2
        self.vel_x = 0
        self.vel_y = random.randrange(2, 8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()
        self.hp -= 1

    def destroy(self):
        self.kill()


class Poison(pygame.sprite.Sprite):
    def __init__(self):
        super(Poison, self).__init__()
        self.image = pygame.image.load(path_game_poison_bottle).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600 - self.rect.width)
        self.rect.y = -self.rect.height
        self.score = 2
        self.vel_x = 0
        self.vel_y = random.randrange(2, 9)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()
        self.hp -= 1

    def destroy(self):
        self.kill()


