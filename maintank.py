import pygame
from constants import TANK_SIZE, BLOCK_SIZE

pygame.init()

# Загрузка всех изображений для анимации движений танка (движение гусениц):
MT_img_up1 = pygame.image.load('Images/Anim_Up/MainTank_Up_1.png').convert_alpha()  # При движении вверх
MT_up1 = pygame.transform.scale(MT_img_up1, (TANK_SIZE, TANK_SIZE))  # 1
MT_img_up2 = pygame.image.load('Images/Anim_Up/MainTank_Up_2.png').convert_alpha()
MT_up2 = pygame.transform.scale(MT_img_up2, (TANK_SIZE, TANK_SIZE))  # 2
MT_img_up3 = pygame.image.load('Images/Anim_Up/MainTank_Up_3.png').convert_alpha()
MT_up3 = pygame.transform.scale(MT_img_up3, (TANK_SIZE, TANK_SIZE))  # 3
MT_img_up4 = pygame.image.load('Images/Anim_Up/MainTank_Up_4.png').convert_alpha()
MT_up4 = pygame.transform.scale(MT_img_up4, (TANK_SIZE, TANK_SIZE))  # 4
MT_img_up5 = pygame.image.load('Images/Anim_Up/MainTank_Up_5.png').convert_alpha()
MT_up5 = pygame.transform.scale(MT_img_up5, (TANK_SIZE, TANK_SIZE))  # 5
MT_img_up6 = pygame.image.load('Images/Anim_Up/MainTank_Up_6.png').convert_alpha()
MT_up6 = pygame.transform.scale(MT_img_up6, (TANK_SIZE, TANK_SIZE))  # 6
MT_img_up7 = pygame.image.load('Images/Anim_Up/MainTank_Up_7.png').convert_alpha()
MT_up7 = pygame.transform.scale(MT_img_up5, (TANK_SIZE, TANK_SIZE))  # 7
MT_img_up8 = pygame.image.load('Images/Anim_Up/MainTank_Up_8.png').convert_alpha()
MT_up8 = pygame.transform.scale(MT_img_up6, (TANK_SIZE, TANK_SIZE))  # 8
MT_img_up9 = pygame.image.load('Images/Anim_Up/MainTank_Up_9.png').convert_alpha()
MT_up9 = pygame.transform.scale(MT_img_up6, (TANK_SIZE, TANK_SIZE))  # 9

# При движении вправо:
MT_img_right1 = pygame.image.load('Images/Anim_Right/MainTank_Right_1.png').convert_alpha()
MT_right1 = pygame.transform.scale(MT_img_right1, (TANK_SIZE, TANK_SIZE))  # 1
MT_img_right2 = pygame.image.load('Images/Anim_Right/MainTank_Right_2.png').convert_alpha()
MT_right2 = pygame.transform.scale(MT_img_right2, (TANK_SIZE, TANK_SIZE))  # 2
MT_img_right3 = pygame.image.load('Images/Anim_Right/MainTank_Right_3.png').convert_alpha()
MT_right3 = pygame.transform.scale(MT_img_right3, (TANK_SIZE, TANK_SIZE))  # 3
MT_img_right4 = pygame.image.load('Images/Anim_Right/MainTank_Right_4.png').convert_alpha()
MT_right4 = pygame.transform.scale(MT_img_right4, (TANK_SIZE, TANK_SIZE))  # 4
MT_img_right5 = pygame.image.load('Images/Anim_Right/MainTank_Right_5.png').convert_alpha()
MT_right5 = pygame.transform.scale(MT_img_right5, (TANK_SIZE, TANK_SIZE))  # 5
MT_img_right6 = pygame.image.load('Images/Anim_Right/MainTank_Right_6.png').convert_alpha()
MT_right6 = pygame.transform.scale(MT_img_right6, (TANK_SIZE, TANK_SIZE))  # 6
MT_img_right7 = pygame.image.load('Images/Anim_Right/MainTank_Right_7.png').convert_alpha()
MT_right7 = pygame.transform.scale(MT_img_right7, (TANK_SIZE, TANK_SIZE))  # 7
MT_img_right8 = pygame.image.load('Images/Anim_Right/MainTank_Right_8.png').convert_alpha()
MT_right8 = pygame.transform.scale(MT_img_right8, (TANK_SIZE, TANK_SIZE))  # 8
MT_img_right9 = pygame.image.load('Images/Anim_Right/MainTank_Right_9.png').convert_alpha()
MT_right9 = pygame.transform.scale(MT_img_right9, (TANK_SIZE, TANK_SIZE))  # 9

# При движении вниз:
MT_img_down1 = pygame.image.load('Images/Anim_Down/MainTank_Down_1.png').convert_alpha()
MT_down1 = pygame.transform.scale(MT_img_down1, (TANK_SIZE, TANK_SIZE))  # 1
MT_img_down2 = pygame.image.load('Images/Anim_Down/MainTank_Down_2.png').convert_alpha()
MT_down2 = pygame.transform.scale(MT_img_down2, (TANK_SIZE, TANK_SIZE))  # 2
MT_img_down3 = pygame.image.load('Images/Anim_Down/MainTank_Down_3.png').convert_alpha()
MT_down3 = pygame.transform.scale(MT_img_down3, (TANK_SIZE, TANK_SIZE))  # 3
MT_img_down4 = pygame.image.load('Images/Anim_Down/MainTank_Down_4.png').convert_alpha()
MT_down4 = pygame.transform.scale(MT_img_down4, (TANK_SIZE, TANK_SIZE))  # 4
MT_img_down5 = pygame.image.load('Images/Anim_Down/MainTank_Down_5.png').convert_alpha()
MT_down5 = pygame.transform.scale(MT_img_down5, (TANK_SIZE, TANK_SIZE))  # 5
MT_img_down6 = pygame.image.load('Images/Anim_Down/MainTank_Down_6.png').convert_alpha()
MT_down6 = pygame.transform.scale(MT_img_down6, (TANK_SIZE, TANK_SIZE))  # 6
MT_img_down7 = pygame.image.load('Images/Anim_Down/MainTank_Down_7.png').convert_alpha()
MT_down7 = pygame.transform.scale(MT_img_down7, (TANK_SIZE, TANK_SIZE))  # 7
MT_img_down8 = pygame.image.load('Images/Anim_Down/MainTank_Down_8.png').convert_alpha()
MT_down8 = pygame.transform.scale(MT_img_down8, (TANK_SIZE, TANK_SIZE))  # 8
MT_img_down9 = pygame.image.load('Images/Anim_Down/MainTank_Down_9.png').convert_alpha()
MT_down9 = pygame.transform.scale(MT_img_down9, (TANK_SIZE, TANK_SIZE))  # 9

# При движении влево:
MT_img_left1 = pygame.image.load('Images/Anim_Left/MainTank_Left_1.png').convert_alpha()
MT_left1 = pygame.transform.scale(MT_img_left1, (TANK_SIZE, TANK_SIZE))  # 1
MT_img_left2 = pygame.image.load('Images/Anim_Left/MainTank_Left_2.png').convert_alpha()
MT_left2 = pygame.transform.scale(MT_img_left2, (TANK_SIZE, TANK_SIZE))  # 2
MT_img_left3 = pygame.image.load('Images/Anim_Left/MainTank_Left_3.png').convert_alpha()
MT_left3 = pygame.transform.scale(MT_img_left3, (TANK_SIZE, TANK_SIZE))  # 3
MT_img_left4 = pygame.image.load('Images/Anim_Left/MainTank_Left_4.png').convert_alpha()
MT_left4 = pygame.transform.scale(MT_img_left4, (TANK_SIZE, TANK_SIZE))  # 4
MT_img_left5 = pygame.image.load('Images/Anim_Left/MainTank_Left_5.png').convert_alpha()
MT_left5 = pygame.transform.scale(MT_img_left5, (TANK_SIZE, TANK_SIZE))  # 5
MT_img_left6 = pygame.image.load('Images/Anim_Left/MainTank_Left_6.png').convert_alpha()
MT_left6 = pygame.transform.scale(MT_img_left6, (TANK_SIZE, TANK_SIZE))  # 6
MT_img_left7 = pygame.image.load('Images/Anim_Left/MainTank_Left_7.png').convert_alpha()
MT_left7 = pygame.transform.scale(MT_img_left7, (TANK_SIZE, TANK_SIZE))  # 7
MT_img_left8 = pygame.image.load('Images/Anim_Left/MainTank_Left_8.png').convert_alpha()
MT_left8 = pygame.transform.scale(MT_img_left8, (TANK_SIZE, TANK_SIZE))  # 8
MT_img_left9 = pygame.image.load('Images/Anim_Left/MainTank_Left_9.png').convert_alpha()
MT_left9 = pygame.transform.scale(MT_img_left9, (TANK_SIZE, TANK_SIZE))  # 9

anim_left = [MT_left1, MT_left2, MT_left3, MT_left4, MT_left5, MT_left6, MT_left7, MT_left8, MT_left9]
anim_right = [MT_right1, MT_right2, MT_right3, MT_right4, MT_right5, MT_right6, MT_right7, MT_right8, MT_right9]
anim_up = [MT_up1, MT_up2, MT_up3, MT_up4, MT_up5, MT_up6, MT_up7, MT_up8, MT_up9]
anim_down = [MT_down1, MT_down2, MT_down3, MT_down4, MT_down5, MT_down6, MT_down7, MT_down8, MT_down9]


class MainTank(pygame.sprite.Sprite):
    """Инициализируем Танк основного игрока"""
    def __init__(self, screen, all_objects):
        super(MainTank, self).__init__()
        all_objects.add(self)  # Добавляем наш танк в группу всех объектов
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.type = 'Tank'
        self.image = MT_up1
        self.rect = self.image.get_rect()
        self.perm_rect = self.rect
        self.r_center_x = float(self.rect.centerx)  # Floating, для плавности движений
        self.r_center_y = float(self.rect.centery)
        self.mright = False  # Переменные для отслеживания поворотов
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.LastMove = "Up"
        self.shotTimer = 0
        self.animCount = 0

    def own_tank_draw(self):
        """Отрисовывавем сам танк"""
        self.screen.blit(self.image, self.rect)

    def create_tank(self, pos_x, pos_y):
        """Размещение танка игрока"""
        spawn = (BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)  # Размещение через *.txt файл
        self.rect = self.perm_rect.move(spawn)

    def update_tank(self, delta_ms, blocks, base):
        """Обновляем позицию танка"""
        speed = 125 * delta_ms / 1000
        oldx, oldy = self.rect.topleft

        if self.shotTimer > 0:
            self.shotTimer -= 1

        if self.animCount >= 60:
            self.animCount = 0

        if self.mright and self.rect.right < self.screen_rect.right:
            self.animCount += 4
            self.image = anim_right[int(self.animCount // 9)]
            self.rect.x += speed

        elif self.mleft and self.rect.left > 0:
            self.animCount += 4
            self.image = anim_left[int(self.animCount // 9)]
            self.rect.x -= speed

        elif self.mtop and self.rect.top > 0:
            self.animCount += 4
            self.image = anim_up[int(self.animCount // 9)]
            self.rect.y -= speed

        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.animCount += 4
            self.image = anim_down[int(self.animCount // 9)]
            self.rect.y += speed

        for block in blocks:
            if block != self and self.rect.colliderect(block.rect):
                self.rect.topleft = oldx, oldy

        if base != self and self.rect.colliderect(base.rect):
            self.rect.topleft = oldx, oldy
