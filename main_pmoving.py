import  pygame, sys
from bullet import Bullet

def events (screen, tank, bullets):
    """Обработка события"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Если кнопка нажата (активна)
            #Вправо
            if event.key == pygame.K_d:
               tank.mright = True
            #Влево
            elif event.key == pygame.K_a:
               tank.mleft = True
            #Вверх
            elif event.key == pygame.K_w:
                tank.mtop = True
            #Вниз
            elif event.key == pygame.K_s:
                tank.mbottom = True
            #Выстрел
            elif event.key == pygame.K_SPACE:
                # Каждый раз при нажатии пробел - создается пуля и добавляется в контейнер bullets
                new_bullet = Bullet(screen, tank)
                if tank.mbottom == True:
                    new_bullet.btDown = True
                elif tank.mtop == True:
                    new_bullet.btUp = True
                elif tank.mright == True:
                    new_bullet.btRight = True
                elif tank.mleft == True:
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

def update(bg_color, screen, tank, bullets):
    """Обновление экрана игры"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.own_tank_draw()
    pygame.display.flip()

