import pygame
from constants import BLOCK_SIZE, BASE_SIZE


base = pygame.image.load('Images/base.png').convert_alpha()
base_img = pygame.transform.scale(base, (BASE_SIZE, BASE_SIZE))
surr = pygame.image.load('Images/surrend_flag.png').convert_alpha()
surr_flag = pygame.transform.scale(surr, (BASE_SIZE, BASE_SIZE))


class Base(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects):
        super(Base, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = "Base"
        self.image = base_img
        self.rect = self.image.get_rect()
        self.perm_rect = self.rect
        self.ok = True

    def update(self):
        if not self.ok:
            self.image = surr_flag

    def base_draw(self):
        self.screen.blit(self.image, self.rect)

    def create_base(self, pos_x, pos_y):
        """Размещение базы игрока"""
        spawn = ((BLOCK_SIZE * pos_x) + 4, (BLOCK_SIZE * pos_y) + 4)  # Размещение через *.txt файл
        self.rect = self.perm_rect.move(spawn)
