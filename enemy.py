import pygame
import random as rd
from constants import TANK_SIZE, BLOCK_SIZE

pygame.init()
# Загрузка всех изображений для анимации движений вражеских танков (движение гусениц):
ET_img_up1 = pygame.image.load('Images/Anim_Up/EnemyTank_Up_1.png').convert_alpha()
ET_up1 = pygame.transform.scale(ET_img_up1, (TANK_SIZE, TANK_SIZE))  # 1
ET_img_up2 = pygame.image.load('Images/Anim_Up/EnemyTank_Up_2.png').convert_alpha()
ET_up2 = pygame.transform.scale(ET_img_up2, (TANK_SIZE, TANK_SIZE))  # 2
ET_img_up3 = pygame.image.load('Images/Anim_Up/EnemyTank_Up_3.png').convert_alpha()
ET_up3 = pygame.transform.scale(ET_img_up3, (TANK_SIZE, TANK_SIZE))  # 3
ET_img_up4 = pygame.image.load('Images/Anim_Up/EnemyTank_Up_4.png').convert_alpha()
ET_up4 = pygame.transform.scale(ET_img_up4, (TANK_SIZE, TANK_SIZE))  # 4

# При движении вправо:
ET_img_right1 = pygame.image.load('Images/Anim_Right/EnemyTank_Right_1.png').convert_alpha()
ET_right1 = pygame.transform.scale(ET_img_right1, (TANK_SIZE, TANK_SIZE))  # 1
ET_img_right2 = pygame.image.load('Images/Anim_Right/EnemyTank_Right_2.png').convert_alpha()
ET_right2 = pygame.transform.scale(ET_img_right2, (TANK_SIZE, TANK_SIZE))  # 2
ET_img_right3 = pygame.image.load('Images/Anim_Right/EnemyTank_Right_3.png').convert_alpha()
ET_right3 = pygame.transform.scale(ET_img_right3, (TANK_SIZE, TANK_SIZE))  # 3
ET_img_right4 = pygame.image.load('Images/Anim_Right/EnemyTank_Right_4.png').convert_alpha()
ET_right4 = pygame.transform.scale(ET_img_right4, (TANK_SIZE, TANK_SIZE))  # 4

# При движении вниз:
ET_img_down1 = pygame.image.load('Images/Anim_Down/EnemyTank_Down_1.png').convert_alpha()
ET_down1 = pygame.transform.scale(ET_img_down1, (TANK_SIZE, TANK_SIZE))  # 1
ET_img_down2 = pygame.image.load('Images/Anim_Down/EnemyTank_Down_2.png').convert_alpha()
ET_down2 = pygame.transform.scale(ET_img_down2, (TANK_SIZE, TANK_SIZE))  # 2
ET_img_down3 = pygame.image.load('Images/Anim_Down/EnemyTank_Down_3.png').convert_alpha()
ET_down3 = pygame.transform.scale(ET_img_down3, (TANK_SIZE, TANK_SIZE))  # 3
ET_img_down4 = pygame.image.load('Images/Anim_Down/EnemyTank_Down_4.png').convert_alpha()
ET_down4 = pygame.transform.scale(ET_img_down4, (TANK_SIZE, TANK_SIZE))  # 4

# При движении влево:
ET_img_left1 = pygame.image.load('Images/Anim_Left/EnemyTank_Left_1.png').convert_alpha()
ET_left1 = pygame.transform.scale(ET_img_left1, (TANK_SIZE, TANK_SIZE))  # 1
ET_img_left2 = pygame.image.load('Images/Anim_Left/EnemyTank_Left_2.png').convert_alpha()
ET_left2 = pygame.transform.scale(ET_img_left2, (TANK_SIZE, TANK_SIZE))  # 2
ET_img_left3 = pygame.image.load('Images/Anim_Left/EnemyTank_Left_3.png').convert_alpha()
ET_left3 = pygame.transform.scale(ET_img_left3, (TANK_SIZE, TANK_SIZE))  # 3
ET_img_left4 = pygame.image.load('Images/Anim_Left/EnemyTank_Left_4.png').convert_alpha()
ET_left4 = pygame.transform.scale(ET_img_left4, (TANK_SIZE, TANK_SIZE))  # 4

anim_left = [ET_left1, ET_left2, ET_left3, ET_left4]
anim_right = [ET_right1, ET_right2, ET_right3, ET_right4]
anim_up = [ET_up1, ET_up2, ET_up3, ET_up4]
anim_down = [ET_down1, ET_down2, ET_down3, ET_down4]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects, pos_x, pos_y):
        """Инициализация вражеских танков"""
        super(Enemy, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = 'Enemy'
        self.image = ET_up1
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect().move((BLOCK_SIZE * pos_x), (BLOCK_SIZE * pos_y))  # Размещение *.txt файл
        self.px = pos_x
        self.py = pos_y
        self.rect_x = float(self.rect.centerx)
        self.rect_y = float(self.rect.centery)
        self.ticks = 0  # Переменные для движения
        self.speed = 0
        self.shotTimer = 0
        self.animCount = 0
        self.next_turn = 0
        self.turn = "Up"

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)

    def update(self, delta_ms, blocks, bangs, bullets,
               screen, all_objects, enemies):
        """Перемещение врагов"""
        self.speed = 125 * delta_ms / 1000
        if self.shotTimer > 0:
            self.shotTimer -= 1

        if self.animCount >= 60:
            self.animCount = 0

        self.ticks = pygame.time.get_ticks()
        ticks_of_next_turn = self.ticks - self.next_turn

        if self.ticks > self.next_turn:
            if ticks_of_next_turn > 1000:
                self.next_turn = self.ticks - 1000
            self.turn = rd.choice(("Up", "Down", "Left", "Right"))
            self.next_turn += 1000

        oldx, oldy = self.rect.topleft

        if self.turn == "Right":
            self.animCount += 3
            self.image = anim_right[int(self.animCount // 20)]
            if self.rect.right < self.screen_rect.right:
                self.rect.x += self.speed
            else:
                self.next_turn = self.ticks
        if self.turn == "Down":
            self.animCount += 3
            self.image = anim_down[int(self.animCount // 20)]
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += self.speed
            else:
                self.next_turn = self.ticks
        elif self.turn == "Left":
            self.animCount += 3
            self.image = anim_left[int(self.animCount // 20)]
            if self.rect.left > self.screen_rect.left:
                self.rect.x -= self.speed
            else:
                self.next_turn = self.ticks
        elif self.turn == "Up":
            self.animCount += 3
            self.image = anim_up[int(self.animCount // 20)]
            if self.rect.top > self.screen_rect.top:
                self.rect.y -= self.speed
            else:
                self.next_turn = self.ticks

        for block in blocks:
            if block != self and self.rect.colliderect(block.rect) \
                    and self.rect.colliderect(self.rect):
                self.rect.topleft = oldx, oldy
                self.next_turn = self.ticks

        for enemy in enemies:
            if enemy != self and self.rect.colliderect(enemy.rect):
                self.rect.topleft = oldx, oldy
                self.next_turn = self.ticks
