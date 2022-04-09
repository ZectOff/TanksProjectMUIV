import pygame
import random as rd

class Block(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Block, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Images/bricks.png")
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(10, 1590), rd.randint(300, 850))

    def update(self):
        pass

    def draw_block(self):
        self.screen.blit(self.image, self.rect)

    def damage(self):
        pass


