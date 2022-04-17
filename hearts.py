import pygame
from game_stats

class Hearts():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Heart.png')
        self.screen_rect = self.screen.get_rect()
        self.pos_x = self.screen_rect.left + 20
        self.pos_y = self.screen_rect.top + 20
        self.rect = (self.pos_x, self.pos_y)


    def update(self):
        pass # Доделать вывод сердечек

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.pos_x += 40