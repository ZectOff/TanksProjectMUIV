import pygame
from constants import BLOCK_SIZE


class Block(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects, pos_x, pos_y):
        """Инициализация кирпичных блоков"""
        super(Block, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = "Block"
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Images/bricks.png").convert()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE / 2, BLOCK_SIZE / 2))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))  # Размещение по координатам из *.txt файла

    def draw_block(self):
        self.screen.blit(self.image, self.rect)
