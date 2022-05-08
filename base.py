import pygame
from constants import BLOCK_SIZE, TANK_SIZE


class Base(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects):
        super(Base, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = "Base"
        self.image = pygame.image.load('Images/base.png').convert_alpha()  # Пока что тестовая картинка
        self.image = pygame.transform.scale(self.image, (TANK_SIZE, TANK_SIZE))
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def create_base(self, pos_x, pos_y):
        """Размещение танка игрока"""
        spawn = (BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)  # Размещение через *.txt файл
        print('Base spawned')
        self.rect = self.rect.move(spawn)
