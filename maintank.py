import pygame


class MainTank():
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Main_Tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False



    def own_tank_draw(self):
        """Отрисовывавем сам танк"""
        self.screen.blit(self.image, self.rect)

    def update_tank(self):
        """Обновляем позицию танка"""
        goRight = pygame.image.load('Images/Main_Tank_Right.png')
        goUp = pygame.image.load('Images/Main_Tank.png')
        goLeft = pygame.image.load('Images/Main_Tank_Left.png')
        goDown = pygame.image.load('Images/Main_Tank_Down.png')

        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.image = goRight
            #self.rect = self.image.get_rect()
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.image = goLeft
            #self.rect = self.image.get_rect()
            self.rect.centerx -= 1
        elif self.mtop and self.rect.top > 0:
            self.image = goUp
            #self.rect = self.image.get_rect()
            self.rect.centery -= 1
        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.image = goDown
            #self.rect = self.image.get_rect()
            self.rect.centery += 1