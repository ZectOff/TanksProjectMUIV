import pygame
import random as rd

class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("Images/enemy_tank.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (150, 150)
        self.rect_x = float(self.rect.centerx)
        self.rect_y = float(self.rect.centery)
        self.next_turn = 1000
        self.turn = ""

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)

    def update_enemy(self, delta_ms):
        ticks = pygame.time.get_ticks()
        if ticks > self.next_turn:
            self.turn = rd.choice(("Up", "Down", "Left", "Right"))
            self.next_turn += 5000
            print(self.turn)

        if self.turn == "Right":
            if self.rect.right < self.screen_rect.right:
                self.rect_x += 100 * delta_ms / 1000
            else:
                self.next_turn = ticks
        if self.turn == "Down":
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect_y += 100 * delta_ms / 1000
            else:
                self.next_turn = ticks
        elif self.turn == "Left":
            if self.rect.left > self.screen_rect.left:
                self.rect_x -= 100 * delta_ms / 1000
            else:
                self.next_turn = ticks
        elif self.turn == "Up":
            if self.rect.top > self.screen_rect.top:
                self.rect_y -= 100 * delta_ms / 1000
                print(self.rect_y)
            else:
                self.next_turn = ticks

        self.rect.centerx = self.rect_x
        self.rect.centery = self.rect_y





