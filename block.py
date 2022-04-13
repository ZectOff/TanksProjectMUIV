import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects, px, py):
        super(Block, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.type = "Block"
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Images/bricks.png")
        self.image = pygame.transform.scale(self.image, (86, 86))
        self.rect = self.image.get_rect()
        self.rect.topleft = (px, py)
        self.rect.bottomright = (px, py)

    def update(self):
        pass

    def draw_block(self):
        self.screen.blit(self.image, self.rect)

    def damage(self):
        pass


