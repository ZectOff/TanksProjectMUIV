import pygame

pygame.init()
b_Up = pygame.image.load('Images/Bullet_up.png')
UpBull = pygame.transform.scale(b_Up, (30, 30))
b_Right = pygame.image.load('Images/Bullet_right.png')
RightBull = pygame.transform.scale(b_Right, (30, 30))
b_Left = pygame.image.load('Images/Bullet_left.png')
LeftBull = pygame.transform.scale(b_Left, (30, 30))
b_Down = pygame.image.load('Images/Bullet_down.png')
DownBull = pygame.transform.scale(b_Down, (30, 30))
bullet_explosion = pygame.mixer.Sound('Sounds/bullet_exp.mp3')


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, tank, all_objects):
        """Создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = 'Bullet'
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('Images/Bullet_up.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = tank.rect.centerx - 30
        self.rect.centery = tank.rect.centery - 30
        self.y = float(self.rect.centery) + 15
        self.x = float(self.rect.centerx) + 15
        self.sound_exp = bullet_explosion
        self.btUp = False  # bt - BulletTurn
        self.btRight = False
        self.btLeft = False
        self.btDown = False

    def draw_bullet(self):
        """Отрисовка пули на экране"""
        self.screen.blit(self.image, (self.x, self.y))#(self.rect.centerx, self.rect.centery)) # Костыльный спавн пули...

    def update(self, delta_ms):
        """Перемещение пули"""
        self.speed = 350 * delta_ms / 1000
        #Пуля летит вниз
        if self.btDown == True:
            self.image = DownBull
            self.y += self.speed
            if self.rect.bottom > self.screen_rect.bottom:
                self.kill()
                pygame.mixer.Sound.play(self.sound_exp)
        # Пуля летит вверх
        if self.btUp == True:
            self.image = UpBull
            self.y -= self.speed
            if self.rect.top <= self.screen_rect.top:
                self.kill()
                pygame.mixer.Sound.play(self.sound_exp)
        # Пуля летит вправо
        if self.btRight == True:
            self.image = RightBull
            self.x += self.speed
            if self.rect.right > self.screen_rect.right:
                self.kill()
                pygame.mixer.Sound.play(self.sound_exp)
        # Пуля летит влево
        if self.btLeft == True:
            self.image = LeftBull
            self.x -= self.speed
            if self.rect.left < self.screen_rect.left:
                self.kill()
                pygame.mixer.Sound.play(self.sound_exp)

        self.rect.y = self.y
        self.rect.x = self.x # Из-за отрисовки по х, расположение пули сдвигается