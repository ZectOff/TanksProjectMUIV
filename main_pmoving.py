import pygame
import sys
import time
import random
from constants import BLOCK_SIZE
from bullet import Bullet
from enemy import Enemy
from block import Block
from pygame.sprite import Group
from hearts import Hearts
from enemy_bullet import EnemyBullet
from scene_run import scene_manager


brik_dead = pygame.mixer.Sound('Sounds/bricks_break.mp3')
bullet_spawn = pygame.mixer.Sound('Sounds/shot.wav')
tank_died = pygame.mixer.Sound('Sounds/dead.wav')
enemy_dead = pygame.mixer.Sound('Sounds/destroy.wav')
win_sound = pygame.mixer.Sound('Sounds/win_game.mp3')
lose_sound = pygame.mixer.Sound('Sounds/lose_game.mp3')


def events(screen, tank, bullets, all_objects):
    """Обработка события"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Если кнопка нажата (активна)
            # Вправо
            if event.key == pygame.K_d:
                tank.mright = True
                tank.LastMove = "Right"
                tank.mtop = False
                tank.mbottom = False
                tank.mleft = False
            # Влево
            elif event.key == pygame.K_a:
                tank.mleft = True
                tank.LastMove = "Left"
                tank.mtop = False
                tank.mbottom = False
                tank.mright = False
            # Вверх
            elif event.key == pygame.K_w:
                tank.mtop = True
                tank.LastMove = "Up"
                tank.mleft = False
                tank.mbottom = False
                tank.mright = False
            # Вниз
            elif event.key == pygame.K_s:
                tank.mbottom = True
                tank.LastMove = "Down"
                tank.mtop = False
                tank.mleft = False
                tank.mright = False
            # Выстрел
            elif event.key == pygame.K_SPACE:
                # Каждый раз при нажатии пробел - создается пуля и добавляется в контейнер bullets
                if len(bullets) < 1:
                    new_bullet = Bullet(screen, tank, all_objects)
                    pygame.mixer.Sound.play(bullet_spawn)
                    if tank.mbottom or tank.LastMove == "Down":
                        new_bullet.btDown = True
                    elif tank.mtop or tank.LastMove == "Up":
                        new_bullet.btUp = True
                    elif tank.mright or tank.LastMove == "Right":
                        new_bullet.btRight = True
                    elif tank.mleft or tank.LastMove == "Left":
                        new_bullet.btLeft = True

                    bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:  # Если кнопка отжата (неактивна)
            # Вправо
            if event.key == pygame.K_d:
                tank.mright = False
            # Влево
            elif event.key == pygame.K_a:
                tank.mleft = False
            # Вверх
            elif event.key == pygame.K_w:
                tank.mtop = False
            # Вниз
            elif event.key == pygame.K_s:
                tank.mbottom = False


def update(bg_color, screen, tank, bullets,
           enemies, blocks, bangs, sc, hearts,
           en_bullets, base):
    """Обновление экрана игры - отрисовываем все объекты"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for en_bull in en_bullets:
        en_bull.draw()
    tank.own_tank_draw()
    base.draw()
    for enemy in enemies:
        enemy.draw_enemy()
    for block in blocks.sprites():
        block.draw_block()
    for bang in bangs.sprites():
        bang.draw()
    for heart in hearts.sprites():
        heart.draw()
    sc.show_score()
    pygame.display.flip()


def hearts_update(screen, stats, hearts):
    """Обновляем сердечки танка"""
    hearts.update(stats)
    if len(hearts) < stats.tank_lifes:
        for _ in range(stats.tank_lifes):
            heart1 = Hearts(screen)
            hearts.add(heart1)
            for heart in hearts:
                heart.pos_x += 40


def bullets_update(screen, bullets, enemies, stats,
                   delta_ms, all_objects, bangs, blocks, sc):
    """Обновление пули (для танка игрока)"""
    bullets.update(delta_ms, screen, all_objects, bangs,
                   enemies, blocks)
    for enemy in enemies:
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                pygame.mixer.Sound.play(enemy_dead)
                stats.killed_enemies += 1
                stats.score += 400
                sc.image_score()
                print(str(stats.killed_enemies) + " Врагов убито.")


def update_blocks(blocks, bullets):
    """Обновление блоков"""
    blocks.update()
    for block in blocks:
        for bullet in bullets:
            if block.rect.colliderect(bullet.rect):
                pygame.mixer.Sound.play(brik_dead)


def update_bangs(bangs):
    """Обновление взрывов после столкновения пули"""
    bangs.update(bangs)


def update_base(base):
    """Обновление базы"""
    base.update()


def update_enemies(enemies, delta_ms, tank, stats,
                   screen, bullets, all_objects, blocks,
                   bangs, hearts, en_bullets, base):
    """Обновление врагов"""
    cruths1 = Group()
    cruths1.add(tank)
    for enemy in enemies:
        enemy.update(delta_ms, blocks, bangs, bullets,
                     screen, all_objects, enemies)
    if len(enemies) == 0:
        print(f'Вы выиграли, победив всех врагов! Заработано {stats.score} очков.')
        pygame.mixer.Sound.play(win_sound)
        time.sleep(2)
        scene_manager.change_scene(scene_manager.menu)
    for enemy in enemies:
        if enemy.rect.colliderect(tank.rect):
            enemy.kill()
            if stats.tank_lifes == 1:
                tank_die(stats, screen, tank, enemies,
                         bullets, all_objects, blocks, hearts, en_bullets, base)
            elif stats.tank_lifes != 0:
                print('Вы потеряли одну жизнь!')
                tank_die(stats, screen, tank, enemies,
                         bullets, all_objects, blocks, hearts, en_bullets, base)
    for en_bull in en_bullets:
        if en_bull.rect.colliderect(tank.rect):
            en_bull.kill()
            if stats.tank_lifes == 1:
                tank_die(stats, screen, tank, enemies,
                         bullets, all_objects, blocks, hearts, en_bullets, base)
            elif stats.tank_lifes != 0:
                print('Вы потеряли одну жизнь! (Вражеский снаряд убил вас!)')
                tank_die(stats, screen, tank, enemies,
                         bullets, all_objects, blocks, hearts, en_bullets, base)


def en_bullet_update(screen, all_objects, en_bullets, delta_ms,
                     enemies, blocks, bangs):
    for _ in enemies:
        enemy_i = random.choice(enemies)
        crutch = enemy_i.ticks
        if crutch > 5000 and len(en_bullets) < len(enemies):
            enemy_bullet = EnemyBullet(screen, all_objects, enemy_i)
            pygame.mixer.Sound.play(bullet_spawn)
            if enemy_i.turn == "Up":
                enemy_bullet.btUp = True
                enemy_bullet.btDown = False
                enemy_bullet.btRight = False
                enemy_bullet.btLeft = False
            elif enemy_i.turn == "Right":
                enemy_bullet.btRight = True
                enemy_bullet.btUp = False
                enemy_bullet.btDown = False
                enemy_bullet.btLeft = False
            elif enemy_i.turn == "Left":
                enemy_bullet.btLeft = True
                enemy_bullet.btUp = False
                enemy_bullet.btDown = False
                enemy_bullet.btRight = False
            elif enemy_i.turn == "Down":
                enemy_bullet.btDown = True
                enemy_bullet.btUp = False
                enemy_bullet.btRight = False
                enemy_bullet.btLeft = False

            en_bullets.add(enemy_bullet)
    en_bullets.update(delta_ms, blocks, bangs, screen)


def tank_die(stats, screen, tank, enemies, bullets,
             all_objects, blocks, hearts, en_bullets, base):
    """Столкновение врагов с игроком"""
    stats.tank_lifes -= 1
    pygame.mixer.Sound.play(tank_died)
    if stats.tank_lifes == 0:
        print('Вы проиграли, потеряв все жизни!')
        pygame.mixer.Sound.play(lose_sound)
        time.sleep(2)  # Попытка при проигрыше вернутся в меню (не работает).
        scene_manager.change_scene(scene_manager.menu)
    else:
        print(str(stats.tank_lifes) + " Жизней осталось.")
        en_bullets.empty()
        bullets.empty()
        blocks.empty()
        enemies.clear()
        hearts.empty()
        tank.kill()
        base.kill()
        draw_level(screen, blocks, all_objects, enemies, tank, base)
        hearts_update(screen, stats, hearts)
        time.sleep(0.6)


def load_level():
    """Загрузка карты уровня"""
    with open("Levels/level_1_map.txt", "r") as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map


def create_obstacle_block(screen, all_objects, blocks,
                          pos_x, pos_y):
    """Создание стены состоящей из 4 блоков"""
    shape = [  # Зададим форму для нашей стены
        'xx',
        'xx'
    ]
    for row_index, row in enumerate(shape):  # Проверим весь список shape и расставим блоки там где есть "х"
        for col_index, col in enumerate(row):
            if col == 'x':
                x = pos_x + (col_index * (BLOCK_SIZE / 2))
                y = pos_y + (row_index * (BLOCK_SIZE / 2))
                block = Block(screen, all_objects, x, y)
                blocks.add(block)


def draw_level(screen, blocks, all_objects,
               enemies, tank, base):
    """Отрисовка карты уровня"""
    level_map = load_level()
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '#':
                nx = x * BLOCK_SIZE
                ny = y * BLOCK_SIZE
                create_obstacle_block(screen, all_objects, blocks, nx, ny)
            elif level_map[y][x] == 'E':
                enemy = Enemy(screen, all_objects, x, y)
                enemies.append(enemy)
            elif level_map[y][x] == '@':
                tank.create_tank(x, y)
            elif level_map[y][x] == 'B':
                for objects in all_objects:
                    if objects.type == "Base":
                        base.create_base(x, y)
