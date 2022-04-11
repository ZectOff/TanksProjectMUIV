import time
import  pygame, sys
from random import randint
from constants import WEIGHT, HEIGHT
from bullet import Bullet
from enemy import Enemy
from block import Block
from pygame.sprite import Group


brik_dead = pygame.mixer.Sound('Sounds/bricks_break.mp3')
bullet_spawn = pygame.mixer.Sound('Sounds/shot.wav')
tank_died = pygame.mixer.Sound('Sounds/dead.wav')
enemy_dead = pygame.mixer.Sound('Sounds/destroy.wav')
win_sound = pygame.mixer.Sound('Sounds/win_game.mp3')
lose_sound = pygame.mixer.Sound('Sounds/lose_game.mp3')


def events (screen, tank, bullets, all_objects):
    """Обработка события"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Если кнопка нажата (активна)
            #Вправо
            if event.key == pygame.K_d:
               tank.mright = True
               tank.LastMove = "Right"
               tank.mtop = False
               tank.mbottom = False
               tank.mleft = False
            #Влево
            elif event.key == pygame.K_a:
               tank.mleft = True
               tank.LastMove = "Left"
               tank.mtop = False
               tank.mbottom = False
               tank.mright = False
            #Вверх
            elif event.key == pygame.K_w:
                tank.mtop = True
                tank.LastMove = "Up"
                tank.mleft = False
                tank.mbottom = False
                tank.mright = False
            #Вниз
            elif event.key == pygame.K_s:
                tank.mbottom = True
                tank.LastMove = "Down"
                tank.mtop = False
                tank.mleft = False
                tank.mright = False
            #Выстрел
            elif event.key == pygame.K_SPACE:
                # Каждый раз при нажатии пробел - создается пуля и добавляется в контейнер bullets
                if len(bullets) < 1:
                    new_bullet = Bullet(screen, tank, all_objects)
                    pygame.mixer.Sound.play(bullet_spawn)
                    if tank.mbottom == True or tank.LastMove == "Down":
                        new_bullet.btDown = True
                    elif tank.mtop == True or tank.LastMove == "Up":
                        new_bullet.btUp = True
                    elif tank.mright == True or tank.LastMove == "Right":
                        new_bullet.btRight = True
                    elif tank.mleft == True or tank.LastMove == "Left":
                        new_bullet.btLeft = True

                    bullets.add(new_bullet)

        elif event.type == pygame.KEYUP: #Если кнопка отжата (неактивна)
            #Вправо
            if event.key == pygame.K_d:
                tank.mright = False
            #Влево
            elif event.key == pygame.K_a:
               tank.mleft = False
            #Вверх
            elif event.key == pygame.K_w:
                tank.mtop = False
            #Вниз
            elif event.key == pygame.K_s:
                tank.mbottom = False


def update(bg_color, screen, tank, bullets, enemies, blocks):
    """Обновление экрана игры"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.own_tank_draw()
    for enemy in enemies.sprites():
        enemy.draw_enemy()
    for block in blocks.sprites():
        block.draw_block()
    # for obj in all_objects:
    #     obj.draw()
    pygame.display.flip()


def bullets_update(bullets, enemies, stats, delta_ms):
    bullets.update(delta_ms)
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        pygame.mixer.Sound.play(enemy_dead)
        stats.killed_enemies += 1
        print(str(stats.killed_enemies) + " Врагов убито.")


def update_blocks(blocks, bullets, enemies, tank):
    blocks.update()
    cruths = Group()
    cruths.add(tank)
    if pygame.sprite.groupcollide(bullets, blocks, True, True):
        pygame.mixer.Sound.play(brik_dead)
    elif pygame.sprite.groupcollide(enemies, blocks, False, False):
        pass # print("Враг столкнулся с кирпичной стеной")
    elif pygame.sprite.groupcollide(cruths, blocks, False, True):
        pass # print("Вы столкнулись с кирпичной стеной")


def update_enemies(enemies, delta_ms, tank, stats, screen, bullets, all_objects, blocks):
    """Обновление врагов"""
    cruths1 = Group()
    cruths1.add(tank)
    enemies.update(delta_ms, blocks)
    if len(enemies) == 0:
        print('Вы выиграли, победив всех врагов!')
        pygame.mixer.Sound.play(win_sound)
        time.sleep(2)
        sys.exit()
    if pygame.sprite.groupcollide(cruths1, enemies, False, True):
        if stats.tank_lifes == 1:
            tank_die(stats, screen, tank, enemies, bullets, all_objects)
        elif stats.tank_lifes != 0:
            print('Вы потеряли одну жизнь!')
            tank_die(stats, screen, tank, enemies, bullets, all_objects)


def tank_die(stats, screen, tank, enemies, bullets, all_objects):
    """Столкновение врагов с игроком"""
    stats.tank_lifes -= 1
    pygame.mixer.Sound.play(tank_died)
    if stats.tank_lifes == 0:
        print('Вы проиграли, потеряв все жизни!')
        pygame.mixer.Sound.play(lose_sound)
        time.sleep(2)
        sys.exit()
    else:
        print(str(stats.tank_lifes) + " Жизней осталось.")
        enemies.empty()
        bullets.empty()
        create_enemies(screen, enemies, all_objects)
        time.sleep(0.5)
        tank.create_tank()


def create_enemies(screen, enemies, all_objects):
    """Создание нескольких врагов"""
    for e_num in range(5):
        enemy = Enemy(screen, all_objects)
        enemies.add(enemy)


def create_blocks(screen, blocks, enemies, tank, all_objects):
    for _ in range(60):
        while True:
            x = randint(0, WEIGHT // 86) * 86
            y = randint(0, HEIGHT // 86) * 86
            rect1 = pygame.Rect(x, y, 86, 86)
            fined = False
            for enemy in enemies:
                if rect1.colliderect(enemy.rect) or rect1.colliderect(tank.rect): # Проверка столкнулся ли блок с врагом или танком
                    fined = True # Если да тогда цикл по новой, нет: блок спавнится
            if not fined: # Цикл требует доработки ибо блоки все равно спавнятся во врагах или в игроке
                break

        block = Block(screen, all_objects, x, y)
        blocks.add(block)
        print(blocks)
