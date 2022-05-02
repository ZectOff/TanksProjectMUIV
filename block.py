import pygame
from constants import BLOCK_SIZE


class Block(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects, pos_x, pos_y):
        super(Block, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = "Block"
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Images/bricks.png")
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect().move(BLOCK_SIZE * pos_x, BLOCK_SIZE * pos_y)

    def update(self):
        pass

    def draw_block(self):
        self.screen.blit(self.image, self.rect)

    def damage(self):
        pass
