import random

import sys, pygame
import os
import time
# from GAME.sound_game import sound_game_play
# import GAME.model
from GAME import game_display_settings
from GAME.model import Player
from main import path_score_image, path_background_game, path_scary, path_sound_game, path_game_hp_bar_monk
from GAME.enemy_movement import EnemySpawner, BonusSpawner, PoisonSpawner
from GAME.particle_spawner import ParticleSpawner

white = (255, 255, 255)
clock = pygame.time.Clock()
fps = 20
ani = 4
image = pygame.image.load(path_scary)

backdropbox = game_display_settings.display_surface_game.get_rect()

player = Player()  # spawn player
player.rect.x = 300  # go to x
player.rect.y = 347  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 20
enemy_spawner = EnemySpawner()
bonus_spawner = BonusSpawner()
poison_spawner = PoisonSpawner()
particle_spawner = ParticleSpawner()
font = pygame.font.Font('freesansbold.ttf', 32)
x = 10
y = 10


def scary():
    image = pygame.image.load(path_scary)
    time.sleep(random.randint(6, 21))
    game_display_settings.display_surface_game.blit(image, (0, 0))


stars_group = pygame.sprite.Group()

score1 = 0
curent_hp = 50
max_hp = 200
hp_lenght = 100
health_ratio = max_hp / hp_lenght
channel = pygame.mixer.Channel(0)
punch = pygame.mixer.Sound(path_sound_game)
image = pygame.image.load(path_score_image)


def score_stats():
    text = pygame.font.SysFont("comicsansms", 25).render("  Score :" + str(score1), True, (0, 0, 0))
    game_display_settings.display_surface_game.blit(text, [0, 0])


def RUN():
    pygame.init()

    game_display_settings.Display_game()

    def Game_play():
        run = True
        channel.play(punch)
        while run:
            jump = False
            jump_y = 20
            game_display_settings.display_surface_game
            background = pygame.image.load(path_background_game)
            game_display_settings.display_surface_game.blit(background, (0, 0))
            img_monk = pygame.image.load(path_game_hp_bar_monk)
            game_display_settings.display_surface_game.blit(img_monk, (360, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        try:
                            sys.exit()
                        finally:
                            run = False
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        player.control(-steps, 0)
                        # print('levo')
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        player.control(steps, 0)
                        # print('desno')
                    if jump is False and event.key == pygame.K_UP or event.key == ord('w'):
                        jump = True
                    if jump is True:
                        game_display_settings.display_surface_game.blit(background, (0, (0 + jump_y)))
                        game_display_settings.display_surface_game.blit(background, (0, (0 - 1)))
                        game_display_settings.display_surface_game.blit(background, (0, (0 - 2)))
                        jump_y -= 70
                        if jump_y < -70:
                            jump = False
                            jump_y = 20
                        # print('jump')
                    if event.key == pygame.K_SPACE:
                        stars_group.add(player.create_stars())
                        # print('SHOOTS')

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        player.control(steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        player.control(-steps, 0)

                    if event.type == pygame.QUIT:
                        pygame.quit()

            collided = pygame.sprite.groupcollide(stars_group, enemy_spawner.enemy_group, True, False)
            for stars, enemy in collided.items():
                enemy[0].get_hit()
                global score1
                score1 += 1
                particle_spawner.spawn_particles((stars.rect.x, stars.rect.y))
                # print("meta pogodjena")

            if pygame.sprite.groupcollide(bonus_spawner.bonus_group, player_list, True, False):
                score1 += 3
                # print("bonus")

            if pygame.sprite.groupcollide(poison_spawner.poison_group, player_list, True, False):
                channel.stop()
                from GAME_OVER.game_over import Over
                Over()
                run = False
                # print("otrovan")

            if pygame.sprite.groupcollide(enemy_spawner.enemy_group, player_list, True, False):
                global max_hp
                max_hp = max_hp - 50
                print(max_hp)
                if max_hp == 0:
                    max_hp += 200
                    channel.stop()
                    from GAME_OVER.game_over import Over
                    Over()
                    run = False
                    # print("pogodjen")

            stars_group.draw(game_display_settings.display_surface_game)
            player_list.draw(game_display_settings.display_surface_game)
            pygame.draw.rect(game_display_settings.display_surface_game, (255, 0, 0), (400, 10, max_hp, 25))
            bonus_spawner.bonus_group.draw(game_display_settings.display_surface_game)
            enemy_spawner.enemy_group.draw(game_display_settings.display_surface_game)
            poison_spawner.poison_group.draw(game_display_settings.display_surface_game)
            particle_spawner.particle_group.draw(game_display_settings.display_surface_game)
            game_display_settings.display_surface_game.blit(image, (-160, -50))

            score_stats()
            pygame.display.update()
            player.update()
            bonus_spawner.update()
            enemy_spawner.update()
            poison_spawner.update()
            stars_group.update()
            particle_spawner.update()
            player_list.draw(game_display_settings.display_surface_game)

            clock.tick(fps)

        pygame.quit()

    Game_play()
