import time
import  pygame, sys
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


def update(bg_color, screen, tank, bullets,
           enemies, blocks, bangs):
    """Обновление экрана игры"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.own_tank_draw()
    for enemy in enemies.sprites():
        enemy.draw_enemy()
    for block in blocks.sprites():
        block.draw_block()
    for bang in bangs.sprites():
        bang.draw()
    pygame.display.flip()


def bullets_update(screen, bullets, enemies, stats,
                   delta_ms, all_objects, bangs, blocks):
    bullets.update(delta_ms, screen, all_objects, bangs,
                   enemies, blocks)
    # if pygame.sprite.groupcollide(bullets, enemies, True, True):
        # for bullet in bullets:
        #     new_bang1 = Bang(screen, all_objects, bullet.rect.centerx, bullet.rect.centery)
        #     bangs.add(new_bang1)
        #     bullet.kill()
    for enemy in enemies:
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                pygame.mixer.Sound.play(enemy_dead)
                stats.killed_enemies += 1
                print(str(stats.killed_enemies) + " Врагов убито.")


def update_blocks(screen, all_objects, blocks, bullets, bangs):
    blocks.update()
    # if pygame.sprite.groupcollide(bullets, blocks, True, True):
    # pygame.mixer.Sound.play(brik_dead)
    #     print("Hhhja")
    #     for bullet in bullets:
    #         print("ssdd")
    #         new_bang2 = Bang(screen, bullet.rect.centex, bullet.rect.centey)
    #         bangs.add(new_bang2)
    #         break
    for block in blocks:
        for bullet in bullets:
            if block.rect.colliderect(bullet.rect):
                pygame.mixer.Sound.play(brik_dead)


def update_bangs(bangs):
    bangs.update(bangs)


def update_enemies(enemies, delta_ms, tank, stats,
                   screen, bullets, all_objects, blocks,
                   bangs):
    """Обновление врагов"""
    cruths1 = Group()
    cruths1.add(tank)
    enemies.update(delta_ms, blocks, bangs, bullets,
                   screen, all_objects, enemies)
    if len(enemies) == 0:
        print('Вы выиграли, победив всех врагов!')
        pygame.mixer.Sound.play(win_sound)
        time.sleep(2)
        sys.exit()
    if pygame.sprite.groupcollide(cruths1, enemies, False, True):
        if stats.tank_lifes == 1:
            tank_die(stats, screen, tank, enemies,
                     bullets, all_objects, blocks)
        elif stats.tank_lifes != 0:
            print('Вы потеряли одну жизнь!')
            tank_die(stats, screen, tank, enemies,
                     bullets, all_objects, blocks)


def tank_die(stats, screen, tank, enemies,
             bullets, all_objects, blocks):
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
        blocks.empty()
        draw_level(screen, blocks, all_objects, enemies, tank)
        time.sleep(0.75)
        tank.create_tank(8, 7)


def create_enemies(screen, enemies, all_objects):
    """Создание нескольких врагов"""
    x = 150
    y = 200
    for e_num in range(3):
        if len(enemies) < 1:
            x = 150
            enemy = Enemy(screen, all_objects, x, y)
            enemies.add(enemy)
        else:
            x += 350
            enemy = Enemy(screen, all_objects, x, y)
            enemies.add(enemy)

'''
def no_tank(rect, enemies, tank, all_objects):
    if rect.colliderect(tank.rect):
        print(f"Столкнулись: tank - {tank.rect} и block - {rect}")
        return False
    # for enemy in enemies:
    #     if rect.colliderect(enemy.rect):
    #         print(f"Столкнулись: enemy - {enemy.rect} и block - {rect}")
    #         return False
    for object in all_objects:
        if rect.colliderect(object.rect):
            print(f"Столкнулись: object - {object.rect} {object.type} и block - {rect}")
            return False
    print(f"Проверено, блок заспавнен на: {rect}")
    return True


def create_blocks(screen, blocks, enemies, tank, all_objects):
    coord_set = set()
    while len(coord_set) < 10:
        #x = randint(0, WEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        x = randint(0, WEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        y = randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        if x > 0 or y > 0:
            if (x, y) not in coord_set:
                rect_1 = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                if no_tank(rect_1, enemies, tank, all_objects):
                    coord_set.add((x, y))
    for x, y in coord_set:
        block = Block(screen, all_objects, x, y)
        blocks.add(block)
'''

def load_level():
    with open("Levels/level_1_map.txt", "r") as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map


def draw_level(screen, blocks, all_objects,
               enemies, tank):
    level_map = load_level()
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '#':
                block = Block(screen, all_objects, x, y)
                blocks.add(block)
            elif level_map[y][x] == 'E':
                enemy = Enemy(screen, all_objects, x, y)
                enemies.add(enemy)
            elif level_map[y][x] == '@':
                tank.create_tank(x, y)

