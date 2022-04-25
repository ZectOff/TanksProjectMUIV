import pygame
from bang import Bang

pygame.init()
b_Up = pygame.image.load('Images/EnBull_up.png')
UpEnBull = pygame.transform.scale(b_Up, (30, 30))
b_Right = pygame.image.load('Images/EnBull_right.png')
RightEnBull = pygame.transform.scale(b_Right, (30, 30))
b_Left = pygame.image.load('Images/EnBull_left.png')
LeftEnBull = pygame.transform.scale(b_Left, (30, 30))
b_Down = pygame.image.load('Images/EnBull_down.png')
DownEnBull = pygame.transform.scale(b_Down, (30, 30))
bullet_explosion = pygame.mixer.Sound('Sounds/bullet_exp.mp3')


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects, enemy):
        super(EnemyBullet, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Images/EnBull_up.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx - 15
        self.rect.centery = enemy.rect.centery - 15
        # print(f"{enemy.rect} - Танк для пули")
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        # print(f"{self.rect} - Вражеская пуля (должна быть на вражеском танке)")
        self.sound_exp = bullet_explosion
        self.btUp = False
        self.btRight = False
        self.btLeft = False
        self.btDown = False

    def update(self, delta_ms, blocks, bangs, screen):
        """Перемещение пули врагов"""
        self.speed = 350 * delta_ms / 1000

        if self.btDown:
            self.image = DownEnBull
            self.y += self.speed
        # Пуля летит вверх
        elif self.btUp:
            self.image = UpEnBull
            self.y -= self.speed
        # Пуля летит вправо
        elif self.btRight:
            self.image = RightEnBull
            self.x += self.speed
        # Пуля летит влево
        elif self.btLeft:
            self.image = LeftEnBull
            self.x -= self.speed

        for block in blocks:
            if self.rect.colliderect(block.rect):
                self.kill()
                block.kill()
                new_bang = Bang(screen, self.rect.centerx, self.rect.centery)
                bangs.add(new_bang)
                break

        if self.rect.bottom > self.screen_rect.bottom or \
                self.rect.top <= self.screen_rect.top or \
                self.rect.right > self.screen_rect.right or \
                self.rect.left < self.screen_rect.left:
            pygame.mixer.Sound.play(self.sound_exp)
            new_bang = Bang(screen, self.rect.centerx, self.rect.centery)
            bangs.add(new_bang)
            self.kill()

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)
