import time
import  pygame, sys
from bullet import Bullet
from enemy import Enemy


bullet_spawn = pygame.mixer.Sound('Sounds/shot.wav')
tank_died = pygame.mixer.Sound('Sounds/dead.wav')
enemy_dead = pygame.mixer.Sound('Sounds/destroy.wav')
win_sound = pygame.mixer.Sound('Sounds/win_game.mp3')

def events (screen, tank, bullets, all_sprites):
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
                    new_bullet = Bullet(screen, tank)
                    all_sprites.add(new_bullet)
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


def update(bg_color, screen, tank, bullets, enemies):
    """Обновление экрана игры"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.own_tank_draw()
    for enemy in enemies.sprites():
        enemy.draw_enemy()
    pygame.display.flip()

def bullets_update(bullets, enemies, stats):
    bullets.update()
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        pygame.mixer.Sound.play(enemy_dead)
        stats.killed_enemies += 1
        print(str(stats.killed_enemies) + " Врагов убито.")

def update_enemies(enemies, delta_ms, tank, stats, screen, bullets):
    """Обновление врагов"""
    enemies.update(delta_ms)
    if len(enemies) == 0:
        print('Вы выиграли, победив всех врагов!')
        pygame.mixer.Sound.play(win_sound)
        time.sleep(2)
        sys.exit()
    if pygame.sprite.spritecollideany(tank, enemies):
        print(enemies)
        if stats.tank_lifes == 1:
            tank_die(stats, screen, tank, enemies, bullets)
        elif stats.tank_lifes != 0:
            print('Вы потеряли одну жизнь!')
            tank_die(stats, screen, tank, enemies, bullets)

def tank_die(stats, screen, tank, enemies, bullets):
    """Столкновение врагов с игроком"""
    stats.tank_lifes -= 1
    pygame.mixer.Sound.play(tank_died)
    if stats.tank_lifes == 0:
        print('Вы проиграли, потеряв все жизни!')
        sys.exit()
    else:
        print(str(stats.tank_lifes) + " Жизней осталось.")
        enemies.empty()
        bullets.empty()
        create_enemies(screen, enemies)
        time.sleep(2)
        tank.create_tank()

def create_enemies(screen, enemies):
    """Создание нескольких врагов"""
    for enemy_number in range(5):
        if len(enemies) < 5:
            enemy = Enemy(screen)
            enemies.add(enemy)