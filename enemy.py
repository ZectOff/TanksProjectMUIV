import pygame
import random as rd


pygame.init()
E_Right = pygame.image.load('Images/EnemyTank_Right.png')
right_e = pygame.transform.scale(E_Right, (80, 80))
E_Left = pygame.image.load('Images/EnemyTank_Left.png')
left_e = pygame.transform.scale(E_Left, (80, 80))
E_Up = pygame.image.load('Images/EnemyTank_Up.png')
up_e = pygame.transform.scale(E_Up, (80, 80))
E_Down = pygame.image.load('Images/EnemyTank_Down.png')
down_e = pygame.transform.scale(E_Down, (80, 80))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects):
        super(Enemy, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = 'Enemy'
        self.image = pygame.image.load("Images/EnemyTank_Up.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(100, 1500), rd.randint(85, 250))
        self.rect_x = float(self.rect.centerx)
        self.rect_y = float(self.rect.centery)
        self.next_turn = 0
        self.turn = ""

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)


    def update(self, delta_ms, blocks):
        """Перемещение врагов"""
        self.speed = 125 * delta_ms / 1000
        ticks = pygame.time.get_ticks()
        ticks_of_next_turn = ticks - self.next_turn
        if ticks > self.next_turn:
            if ticks_of_next_turn > 1000:
                self.next_turn = ticks - 1000
            self.turn = rd.choice(("Up", "Down", "Left", "Right"))
            self.next_turn += 1000

        oldX, oldY = self.rect.topleft

        if self.turn == "Right":
            self.image = right_e
            if self.rect.right < self.screen_rect.right:
                self.rect.x += self.speed
            else:
                self.next_turn = ticks
        if self.turn == "Down":
            self.image = down_e
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += self.speed
            else:
                self.next_turn = ticks
        elif self.turn == "Left":
            self.image = left_e
            if self.rect.left > self.screen_rect.left:
                self.rect.x -= self.speed
            else:
                self.next_turn = ticks
        elif self.turn == "Up":
            self.image = up_e
            if self.rect.top > self.screen_rect.top:
                self.rect.y -= self.speed
            else:
                self.next_turn = ticks

        for block in blocks:
            if block != self and self.rect.colliderect(block.rect):
                self.rect.topleft = oldX, oldY #Дополнить: Враги не должны проходить сквозь друг друга
