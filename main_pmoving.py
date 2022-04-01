import  pygame, sys
from bullet import Bullet
from enemy import Enemy



def events (screen, tank, bullets):
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
                new_bullet = Bullet(screen, tank)
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
    for enem in enemies.sprites():
        enem.draw_enemy()
    pygame.display.flip()

def create_enemies(screen, enemies):
    """Создание нескольких врагов"""
    for enemy_number in range(1):
        enemy = Enemy(screen)
        if len(enemies) < 5:
            enemies.add(enemy)
        else:
            enemies.remove(enemy)