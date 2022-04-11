import pygame


pygame.init()
Right_t = pygame.image.load('Images/MainTank_Right.png')
goRight = pygame.transform.scale(Right_t, (80, 80))
Up_t = pygame.image.load('Images/MainTank_Up.png')
goUp = pygame.transform.scale(Up_t, (80, 80))
Left_t = pygame.image.load('Images/MainTank_Left.png')
goLeft = pygame.transform.scale(Left_t, (80, 80))
Down_t = pygame.image.load('Images/MainTank_Down.png')
goDown = pygame.transform.scale(Down_t, (80, 80))

class MainTank(pygame.sprite.Sprite):
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen, all_objects):
        super(MainTank, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = 'Tank'
        self.image = pygame.image.load('Images/MainTank_Up.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.r_center_x = float(self.rect.centerx) #Floating, для плавности движений
        self.r_center_y = float(self.rect.centery)
        self.rect.center = self.screen_rect.center
        print(self.rect.center)
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.LastMove = "Up"

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


    def create_tank(self):
        """Размещение танка игрока по центру"""
        self.rect.center = self.screen_rect.center
        print("Встал по центру")
