import pygame
from constants import TANK_SIZE, BLOCK_SIZE

pygame.init()
Right_t = pygame.image.load('Images/MainTank_Right.png').convert_alpha()
goRight = pygame.transform.scale(Right_t, (TANK_SIZE, TANK_SIZE))
Up_t = pygame.image.load('Images/MainTank_Up.png').convert_alpha()
goUp = pygame.transform.scale(Up_t, (TANK_SIZE, TANK_SIZE))
Left_t = pygame.image.load('Images/MainTank_Left.png').convert_alpha()
goLeft = pygame.transform.scale(Left_t, (TANK_SIZE, TANK_SIZE))
Down_t = pygame.image.load('Images/MainTank_Down.png').convert_alpha()
goDown = pygame.transform.scale(Down_t, (TANK_SIZE, TANK_SIZE))


class MainTank(pygame.sprite.Sprite):
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen, all_objects):
        super(MainTank, self).__init__()
        all_objects.add(self)  # Добавляем наш танк в группу всех объектов
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.type = 'Tank'
        self.image = goUp
        self.rect = self.image.get_rect()
        self.perm_rect = self.rect
        self.r_center_x = float(self.rect.centerx)  # Floating, для плавности движений
        self.r_center_y = float(self.rect.centery)
        self.mright = False  # Переменные для отслеживания поворотов
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.LastMove = "Up"

    def own_tank_draw(self):
        """Отрисовывавем сам танк"""
        self.screen.blit(self.image, self.rect)

    def create_tank(self, pos_x, pos_y):
        """Размещение танка игрока"""
        spawn = (BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)  # Размещение через *.txt файл
        print(spawn)
        self.rect = self.perm_rect.move(spawn)
        print('Tank spawned')

    def update_tank(self, delta_ms, blocks):
        """Обновляем позицию танка"""
        speed = 125 * delta_ms / 1000
        oldx, oldy = self.rect.topleft

        if self.mright and self.rect.right < self.screen_rect.right:
            self.image = goRight
            self.rect.x += speed
        elif self.mleft and self.rect.left > 0:
            self.image = goLeft
            self.rect.x -= speed
        elif self.mtop and self.rect.top > 0:
            self.image = goUp
            self.rect.y -= speed
        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.image = goDown
            self.rect.y += speed

        for block in blocks:
            if block != self and self.rect.colliderect(block.rect):
                self.rect.topleft = oldx, oldy
