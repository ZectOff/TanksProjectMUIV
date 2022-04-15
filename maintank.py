import pygame
from constants import TANK_SIZE, BLOCK_SIZE

pygame.init()
Right_t = pygame.image.load('Images/MainTank_Right.png')
goRight = pygame.transform.scale(Right_t, (TANK_SIZE, TANK_SIZE))
Up_t = pygame.image.load('Images/MainTank_Up.png')
goUp = pygame.transform.scale(Up_t, (TANK_SIZE, TANK_SIZE))
Left_t = pygame.image.load('Images/MainTank_Left.png')
goLeft = pygame.transform.scale(Left_t, (TANK_SIZE, TANK_SIZE))
Down_t = pygame.image.load('Images/MainTank_Down.png')
goDown = pygame.transform.scale(Down_t, (TANK_SIZE, TANK_SIZE))

class MainTank(pygame.sprite.Sprite):
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen, all_objects):
        super(MainTank, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.type = 'Tank'
        self.image = pygame.image.load('Images/MainTank_Up.png')
        self.image = pygame.transform.scale(self.image, (TANK_SIZE, TANK_SIZE))
        self.rect = self.image.get_rect()#.move(BLOCK_SIZE * 8, BLOCK_SIZE * 7)
        self.perm_rect = self.rect
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        self.r_center_x = float(self.rect.centerx) #Floating, для плавности движений
        self.r_center_y = float(self.rect.centery)
        # self.rect.center = self.screen_rect.center
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.LastMove = "Up"

    def create_tank(self, pos_x, pos_y):
        """Размещение танка игрока по центру"""
        self.spawn = (BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)
        self.rect = self.perm_rect.move(self.spawn)
        print("Ваш танк встал на начальную точку")

    def own_tank_draw(self):
        """Отрисовывавем сам танк"""
        self.screen.blit(self.image, self.rect)#(self.rect.centerx - 30, self.rect.centery - 30))

    def update_tank(self, delta_ms, blocks):
        """Обновляем позицию танка"""
        self.speed = 125 * delta_ms / 1000
        oldX, oldY = self.rect.topleft

        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.image = goRight
            self.rect.x += self.speed
        elif self.mleft and self.rect.left > 0:
            self.image = goLeft
            self.rect.x -= self.speed
        elif self.mtop and self.rect.top > 0:
            self.image = goUp
            self.rect.y -= self.speed
        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.image = goDown
            self.rect.y += self.speed

        for block in blocks:
            if block != self and self.rect.colliderect(block.rect):
                self.rect.topleft = oldX, oldY

    #
    # def create_tank(self, pos_x, pos_y):
    #     """Размещение танка игрока по центру"""
    #     print(pos_x, pos_y)
    #     self.rect = self.rect.move(BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)
    #     print(self.rect)
    #     print("Ваш танк встал на начальную точку")

