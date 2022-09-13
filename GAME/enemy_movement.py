import pygame
import random
from GAME.model import Enemy1, Enemy2, BonusPoints,Poison


class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.enemy_group.update()
        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(30, 120)

        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
        new_enemy1 = Enemy1()
        new_enemy2 = Enemy2()
        self.enemy_group.add(new_enemy1)
        self.enemy_group.add(new_enemy2)


class BonusSpawner:
    def __init__(self):
        self.bonus_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.bonus_group.update()
        if self.spawn_timer == 0:
            self.spawn_bonus()
            self.spawn_timer = random.randrange(30, 120)

        else:
            self.spawn_timer -= 1

    def spawn_bonus(self):
        new_bonus = BonusPoints()

        self.bonus_group.add(new_bonus)


class PoisonSpawner:
    def __init__(self):
        self.poison_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.poison_group.update()
        if self.spawn_timer == 0:
            self.spawn_poison()
            self.spawn_timer = random.randrange(30, 120)

        else:
            self.spawn_timer -= 1

    def spawn_poison(self):
        new_poison = Poison()

        self.poison_group.add(new_poison)

