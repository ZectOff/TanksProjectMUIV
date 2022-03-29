import pygame

pygame.init()
Right_t = pygame.image.load('Images/MainTank_Right.png')
goRight = pygame.transform.scale(Right_t, (85, 85))
Up_t = pygame.image.load('Images/MainTank_Up.png')
goUp = pygame.transform.scale(Up_t, (85, 85))
Left_t = pygame.image.load('Images/MainTank_Left.png')
goLeft = pygame.transform.scale(Left_t, (85, 85))
Down_t = pygame.image.load('Images/MainTank_Down.png')
goDown = pygame.transform.scale(Down_t, (85, 85))

class MainTank():
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/MainTank_Up.png')
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect()
        print(self.rect)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.r_center_x = float(self.rect.centerx) #Floating, для плавности движений
        self.r_center_y = float(self.rect.centery)
        self.rect.center = self.screen_rect.center
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        LastMove = "Up"



    def own_tank_draw(self):
        """Отрисовывавем сам танк"""
        self.screen.blit(self.image, (self.rect.centerx - 30, self.rect.centery -30))

    def update_tank(self, delta_ms):
        """Обновляем позицию танка"""

        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.image = goRight
            self.r_center_x += 250 * delta_ms / 1000
        elif self.mleft and self.rect.left > 0:
            self.image = goLeft
            self.r_center_x -= 250 * delta_ms / 1000
        elif self.mtop and self.rect.top > 0:
            self.image = goUp
            self.r_center_y -= 250 * delta_ms / 1000
        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.image = goDown
            self.r_center_y += 250 * delta_ms / 1000

        self.rect.centerx = self.r_center_x
        self.rect.centery = self.r_center_y
