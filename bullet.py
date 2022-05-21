import pygame
from bang import Bang
from constants import BULLET_SIZE

pygame.init()
b_Up = pygame.image.load('Images/Bullet_up.png').convert_alpha()
UpBull = pygame.transform.scale(b_Up, (BULLET_SIZE, BULLET_SIZE))
b_Right = pygame.image.load('Images/Bullet_right.png').convert_alpha()
RightBull = pygame.transform.scale(b_Right, (BULLET_SIZE, BULLET_SIZE))
b_Left = pygame.image.load('Images/Bullet_left.png').convert_alpha()
LeftBull = pygame.transform.scale(b_Left, (BULLET_SIZE, BULLET_SIZE))
b_Down = pygame.image.load('Images/Bullet_down.png').convert_alpha()
DownBull = pygame.transform.scale(b_Down, (BULLET_SIZE, BULLET_SIZE))
bullet_explosion = pygame.mixer.Sound('Sounds/bullet_exp.mp3')


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, tank, all_objects):
        """Создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = 'Bullet'
        self.screen_rect = screen.get_rect()
        self.image = UpBull
        self.rect = self.image.get_rect()
        self.rect.centerx = tank.rect.centerx - (BULLET_SIZE / 2)
        self.rect.centery = tank.rect.centery - (BULLET_SIZE / 2)
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        self.sound_exp = bullet_explosion
        self.btUp = False  # bt - BulletTurn
        self.btRight = False
        self.btLeft = False
        self.btDown = False

    def draw_bullet(self):
        """Отрисовка пули на экране"""
        self.screen.blit(self.image, (self.x, self.y))

    def update(self, delta_ms, screen, all_objects,
               bangs, enemies, blocks, base):
        """Перемещение пули"""
        speed = 350 * delta_ms / 1000
        # Пуля летит вниз
        if self.btDown:
            self.image = DownBull
            self.y += speed
        # Пуля летит вверх
        elif self.btUp:
            self.image = UpBull
            self.y -= speed
        # Пуля летит вправо
        elif self.btRight:
            self.image = RightBull
            self.x += speed
        # Пуля летит влево
        elif self.btLeft:
            self.image = LeftBull
            self.x -= speed

        for block in blocks:  # При столкновении с блоком - взорвалась
            if self.rect.colliderect(block.rect):
                self.kill()
                block.kill()
                new_bang1 = Bang(screen, self.rect.centerx, self.rect.centery)
                bangs.add(new_bang1)
                break

        for enemy in enemies:  # При столкновении с врагом - взорвалась
            if self.rect.colliderect(enemy.rect):
                self.kill()
                enemy.kill()
                enemies.remove(enemy)
                new_bang2 = Bang(screen, self.rect.centerx, self.rect.centery)
                bangs.add(new_bang2)
                break

        if self.rect.bottom > self.screen_rect.bottom or \
                self.rect.top <= self.screen_rect.top or \
                self.rect.right > self.screen_rect.right or \
                self.rect.left < self.screen_rect.left:
            pygame.mixer.Sound.play(self.sound_exp)  # Врезалась в экран - взорвалась
            new_bang3 = Bang(screen, self.rect.centerx, self.rect.centery)
            bangs.add(new_bang3)
            self.kill()

        if self.rect.colliderect(base.rect):
            base.kill()
            print("База умерла твоя все конечик")
            pygame.mixer.Sound.play(self.sound_exp)  # Врезалась в базу - взорвалась
            new_bang4 = Bang(screen, self.rect.centerx, self.rect.centery)
            bangs.add(new_bang4)
            self.kill()

        self.rect.y = self.y
        self.rect.x = self.x  # Из-за отрисовки по х, расположение пули сдвигается
