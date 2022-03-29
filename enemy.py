import pygame
import random as rd


pygame.init()
E_Right = pygame.image.load('Images/EnemyTank_Right.png')
right_e = pygame.transform.scale(E_Right, (85, 85))
E_Left = pygame.image.load('Images/EnemyTank_Left.png')
left_e = pygame.transform.scale(E_Left, (85, 85))
E_Up = pygame.image.load('Images/EnemyTank_Up.png')
up_e = pygame.transform.scale(E_Up, (85, 85))
E_Down = pygame.image.load('Images/EnemyTank_Down.png')
down_e = pygame.transform.scale(E_Down, (85, 85))

class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("Images/EnemyTank_Up.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (150, 150)
        self.rect_x = float(self.rect.centerx)
        self.rect_y = float(self.rect.centery)
        self.next_turn = 0
        self.turn = ""

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)

    def update_enemy(self, delta_ms):
        ticks = pygame.time.get_ticks()
        if ticks > self.next_turn:
            self.turn = rd.choice(("Up", "Down", "Left", "Right"))
            self.next_turn += 1000
            print(self.turn)

        if self.turn == "Right":
            self.image = right_e
            if self.rect.right < self.screen_rect.right:
                self.rect_x += 250 * delta_ms / 1000
            else:
                self.next_turn = ticks
        if self.turn == "Down":
            self.image = down_e
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect_y += 250 * delta_ms / 1000
            else:
                self.next_turn = ticks
        elif self.turn == "Left":
            self.image = left_e
            if self.rect.left > self.screen_rect.left:
                self.rect_x -= 250 * delta_ms / 1000
            else:
                self.next_turn = ticks
        elif self.turn == "Up":
            self.image = up_e
            if self.rect.top > self.screen_rect.top:
                self.rect_y -= 250 * delta_ms / 1000
            else:
                self.next_turn = ticks


        self.rect.centerx = self.rect_x
        self.rect.centery = self.rect_y





